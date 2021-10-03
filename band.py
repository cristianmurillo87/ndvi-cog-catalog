import requests
import rasterio
import numpy as np

class COGImageBand(object):
    __BAND_DATA = None

    def __init__(
        self,
        title='',
        name='',
        url=None,
        band_data=None
        pixel_size=None,
        crs=None,
        bounds=None,
        center_wavelength=None,
        full_width_half_max=None
    ):
        self.__band_title = title
        self.__band_name = name
        self.__band_url = url
        self.__band_shape = pixel_size
        self.__band_crs = crs
        self.__band_bounds = bounds,
        self.__band_center_wavelength = center_wavelength
        self.__band_full_width_half_max = full_width_half_max
        self.init_band_data()

    @property
    def title(self):
        return self.__band_title

    @property
    def name(self):
        return self.__band_name

    @property
    def url(self):
        return self.__band_url

    @property
    def shape(self):
        return (self.width, self.height)

    @property
    def width(self):
        if self.__BAND_DATA:
            return self.__BAND_DATA.shape[1]
        return None

    @property
    def height(self):
        if self.__BAND_DATA:
            return self.__BAND_DATA.shape[0]
        return None

    @property
    def size(self):
        if self.__BAND_DATA:
            return self.__BAND_DATA.size
        return None

    @property(self):
    def crs(self):
        return self.__band_crs

    @property
    def bounds(self):
        return self.__band_bounds
    
    @property
    def type(self):
        if self.__BAND_DATA:
            return self.__BAND_DATA.dtype
        return None
    
    @property
    def transform(self):
        return self.__band_transform

    @property
    def center_wavelength(self):
        return self.__band_center_wavelength
    
    @property
    def full_width_half_max(self):
        return self.__band_full_width_half_max

    @property
    def data(self):
        return self.__BAND_DATA

    @property(self):
    def mean(self):
        if self.__BAND_DATA:
            return np.mean(self.__BAND_DATA, dtype=np.float64)
        return None

    @property
    def std(self):
        if self.__BAND_DATA:
            return np.std(self.__BAND_DATA, dtype=np.float64)
        return None

    @property
    def variance(self):
        if self.__BAND_DATA:
            return np.var(self.__BAND_DATA, dtype=np.float64)
        return None
    
    def init_band_data(self, band_data):
        if isinstance(band_data, np.ndarray):
            self.__BAND_DATA = band_data
        else:
            if self.url:
                with rasterio.open(self.url) as band:
                    self.__BAND_DATA = band.read(1)
                    self.__band_bounds = band.bounds
                    self.__brand_crs = band.crs
                    self.__band_transform  = band.transform

    def set_transform(transform):
        self.__band_transform = transform

