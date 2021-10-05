import requests
import rasterio as rio
import numpy as np

class COGImageBand(object):
    __BAND_DATA = None

    def __init__(
        self,
        title='',
        name='',
        common_name=None,
        url=None,
        band_data=None,
        pixel_size=None,
        crs=None,
        bounds=None,
        center_wavelength=None,
        full_width_half_max=None
    ):
        self.__band_title = title
        self.__band_name = name
        self.__band_common_name = common_name
        self.__band_url = url
        self.__band_pixel_size = pixel_size
        self.__brand_crs = crs
        self.__band_bounds = bounds,
        self.__band_center_wavelength = center_wavelength
        self.__band_full_width_half_max = full_width_half_max
        self.init_band_data(band_data)

    @property
    def title(self):
        return self.__band_title

    @property
    def name(self):
        return self.__band_name

    @property
    def common_name(self):
        return self.__band_common_name

    @property
    def url(self):
        return self.__band_url

    @property
    def shape(self):
        return (self.width, self.height)

    @property
    def width(self):
        return self.__BAND_DATA.shape[1] if self.is_valid() else None

    @property
    def height(self):
        return self.__BAND_DATA.shape[0] if self.is_valid() else None

    @property
    def size(self):
        return self.__BAND_DATA.size if self.is_valid() else None

    @property
    def crs(self):
        return self.__brand_crs

    @property
    def bounds(self):
        return self.__band_bounds
    
    @property
    def type(self):
        return self.__BAND_DATA.dtype if self.is_valid() else None
    
    @property
    def transform(self):
        return self.__band_transform

    @property
    def pixel_size(self):
        return self.__band_pixel_size

    @property
    def center_wavelength(self):
        return self.__band_center_wavelength
    
    @property
    def full_width_half_max(self):
        return self.__band_full_width_half_max

    @property
    def data(self):
        return self.__BAND_DATA

    @property
    def mean(self):
        return np.nanmean(self.__BAND_DATA, dtype=np.float64) if self.is_valid() else None

    @property
    def min(self):
        return np.nanmin(self.__BAND_DATA) if self.is_valid() else None
    
    @property
    def max(self):
        return np.nanmax(self.__BAND_DATA) if self.is_valid() else None

    @property
    def median(self):
        return np.nanmedian(self.__BAND_DATA) if self.is_valid() else None

    @property
    def std(self):
        return np.nanstd(self.__BAND_DATA, dtype=np.float64) if self.is_valid() else None

    @property
    def variance(self):
        return np.nanvar(self.__BAND_DATA, dtype=np.float64) if self.is_valid() else None

    def is_valid(self):
        return isinstance(self.__BAND_DATA, np.ndarray)

    def init_band_data(self, band_data):
        if isinstance(band_data, np.ndarray):
            self.__BAND_DATA = band_data
        else:
            if self.url:
                with rio.open(self.url) as band:
                    self.__BAND_DATA = band.read(1)
                    self.__band_bounds = band.bounds
                    self.__brand_crs = band.crs
                    self.__band_transform  = band.transform

    def set_transform(self, transform):
        self.__band_transform = transform

