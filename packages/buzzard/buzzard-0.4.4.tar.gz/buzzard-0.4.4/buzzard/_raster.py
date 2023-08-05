""">>> help(Raster)"""

from __future__ import division, print_function
import numbers

import numpy as np

from buzzard._footprint import Footprint
from buzzard._proxy import Proxy
from buzzard._raster_utils import RasterUtilsMixin
from buzzard._raster_remap import RemapMixin
from buzzard._raster_getset_data import RasterGetSetMixin
from buzzard._tools import conv, deprecation_pool
from buzzard import _tools

class Raster(Proxy, RasterGetSetMixin, RasterUtilsMixin, RemapMixin):
    """Abstract class to all raster sources"""

    class _Constants(Proxy._Constants):
        """See Proxy._Constants"""

        def __init__(self, ds, **kwargs):
            # GDAL informations
            if 'gdal_ds' in kwargs:
                gdal_ds = kwargs.pop('gdal_ds')
                kwargs['fp_stored'] = Footprint(
                    gt=gdal_ds.GetGeoTransform(),
                    rsize=(gdal_ds.RasterXSize, gdal_ds.RasterYSize),
                )
                kwargs['band_schema'] = Raster._band_schema_of_gdal_ds(gdal_ds)
                kwargs['dtype'] = conv.dtype_of_gdt_downcast(gdal_ds.GetRasterBand(1).DataType)
                kwargs['wkt'] = gdal_ds.GetProjection()
            self.fp_stored = kwargs.pop('fp_stored')
            self.band_schema = kwargs.pop('band_schema')
            self.dtype = kwargs.pop('dtype')

            super(Raster._Constants, self).__init__(ds, **kwargs)

    def __init__(self, ds, consts, gdal_ds=None):
        """Instanciated by DataSource class, instanciation by user is undefined"""
        Proxy.__init__(self, ds, consts, consts.fp_stored)

        if self._to_work is not None:
            fp = self._c.fp_stored.move(*self._to_work([
                self._c.fp_stored.tl, self._c.fp_stored.tr, self._c.fp_stored.br
            ]))
        else:
            fp = self._c.fp_stored

        self._gdal_ds = gdal_ds
        self._fp = fp

        self._shared_band_index = None
        for i, type in enumerate(self._c.band_schema['mask'], 1):
            if type == 'per_dataset':
                self._shared_band_index = i
                break

    # Properties ******************************************************************************** **
    @property
    def band_schema(self):
        """Band schema"""
        return dict(self._c.band_schema)

    @property
    def fp(self):
        """Accessor for inner Footprint instance"""
        return self._fp

    @property
    def fp_stored(self):
        """Accessor for inner Footprint instance"""
        return self._c.fp_stored

    @property
    def dtype(self):
        """Accessor for dtype"""
        return self._c.dtype

    @property
    def nodata(self):
        """Accessor for first band's nodata value"""
        return self.get_nodata(1)

    def get_nodata(self, band=1):
        """Accessor for nodata value"""
        return self._c.band_schema['nodata'][band - 1]

    def __len__(self):
        """Return the number of bands"""
        return len(self._c.band_schema['nodata'])

    @property
    def driver(self):
        """Get the GDAL driver name"""
        return self._c.driver

    # Life control ****************************************************************************** **
    @property
    def close(self):
        """Close a raster with a call or a context management.

        Examples
        --------
        >>> ds.dem.close()
        >>> with ds.dem.close:
                # code...
        >>> with ds.acreate_raster('result.tif', fp, float, 1).close as result:
                # code...
        """
        def _close():
            if self._ds._is_locked_activate(self):
                raise RuntimeError('Attempting to close a `buzz.Raster` before `TBD`')
            self._ds._unregister(self)
            self.deactivate()
            del self._gdal_ds
            del self._ds

        return _RasterCloseRoutine(self, _close)

    # Raster read operations ******************************************************************** **
    @_tools.ensure_activated
    def get_data(self, fp=None, band=1, mask=None, nodata=None, interpolation='cv_area',
                 dtype=None, op=np.rint):
        """Get `data` located at `fp` in raster file.

        If `nodata` is set in raster or provided as an argument, fp can lie partially or fully
        outside of raster.

        If `allow_interpolation` is enabled in the DataSource constructor, it is then possible to
        use a `fp` that is not aligned with the source raster, interpolation in then used to
        remap source to `fp`. `nodata` values are also handled and spreaded to the output through
        remapping.

        (experimental) An optional `mask` may be provided. GDAL band sampling is only performed near
        `True` pixels. Current implementation might be extremely slow.

        Parameters
        ----------
        fp: Footprint of shape (Y, X)
            If None: return the full raster
            If Footprint: return this window from the raster
        band: band index or sequence of band index (see `Band Indices` below)
        mask: numpy array of shape (Y, X)
        nodata: Number
            Override self.get_nodata()
        interpolation: one of ('cv_area', 'cv_nearest', 'cv_linear', 'cv_cubic', 'cv_lanczos4')
            Resampling method
        dtype: type
            Override gdal output type
        op: None or vector function
            Rounding function following an interpolation when output type is integer

        Returns
        -------
        numpy.ndarray
            of shape (Y, X) or (Y, X, B)

        Band Indices
        ------------
        | index type | index value     | meaning          |
        |------------|-----------------|------------------|
        | int        | -1              | All bands        |
        | int        | 1, 2, 3, ...    | Band `i`         |
        | complex    | -1j             | All bands masks  |
        | complex    | 0j              | Shared mask band |
        | complex    | 1j, 2j, 3j, ... | Mask of band `i` |

        """
        # Normalize and check fp parameter
        if fp is None:
            fp = self.fp
        elif not isinstance(fp, Footprint):
            raise ValueError('Bad fp type `%s`' % type(fp)) # pragma: no cover

        # Normalize and check dtype parameter
        if dtype is None:
            dtype = self.dtype
        else:
            dtype = conv.dtype_of_any_downcast(dtype)

        # Normalize and check band parameter
        bands, is_flat = _tools.normalize_band_parameter(band, len(self), self._shared_band_index)
        if is_flat:
            outshape = fp.shape
        else:
            outshape = tuple(fp.shape) + (len(bands),)
        del band

        # Normalize and check nodata
        if nodata is None:
            nodataconv = False
            onodata = self.nodata # May be None
        else:
            if not isinstance(nodata, numbers.Number):
                raise ValueError('Bad nodata type') # pragma: no cover
            onodata = nodata
            nodataconv = self.nodata is not None

        # Check op parameter
        if not isinstance(np.zeros(1, dtype=dtype)[0], numbers.Integral):
            op = None

        # Check mask parameter
        if mask is not None:
            mask = np.asarray(mask).astype(bool)
            if mask.shape != tuple(fp.shape):
                raise ValueError('mask should have the same shape as `fp`') # pragma: no cover

        # Normalize interpolation parameter
        if not self._ds._allow_interpolation:
            interpolation = None

        # Work
        dilate_size = 4 * self.fp.pxsizex / fp.pxsizex # hyperparameter
        dilate_size = max(2, np.ceil(dilate_size))
        samplefp = fp.dilate(dilate_size)
        if not samplefp.share_area(self.fp):
            if onodata is None:
                raise Exception(
                    "Querying data fully outside of file's Footprint, but `nodata` is not known. "
                    "Provide a `nodata` parameter or create a new file with a `nodata` value set."
                )
            return np.full(outshape, onodata, dtype)

        samplefp = self.fp & samplefp
        samplebands = self._sample_bands(fp, samplefp, bands, mask, interpolation, onodata)

        if nodataconv:
            samplebands[samplebands == self.nodata] = onodata

        array = self._remap(
            samplefp,
            fp,
            interpolation=interpolation,
            array=samplebands,
            mask=None,
            nodata=onodata,
            mask_mode='erode',
        )
        del samplebands

        if op is not None:
            array = op(array)
        return array.astype(dtype).reshape(outshape)

    # The end *********************************************************************************** **
    # ******************************************************************************************* **

deprecation_pool.add_deprecated_property(Raster, 'fp_stored', 'fp_origin', '0.4.4')

_RasterCloseRoutine = type('_RasterCloseRoutine', (_tools.CallOrContext,), {
    '__doc__': Raster.close.__doc__,
})
