"""
A class holding both the metadata and the image values of a COG.
"""
import rasterio as rio
import numpy as np

from pathlib import Path
from typing import Union, List, Optional, Tuple


class COGImageBand(object):
    """
    This class hold the metadata as well as the actual data (as a numpy array) asociated
    with a band of a satellite image available throug the Element84 API.
    """
    __BAND_DATA = None

    def __init__(
            self,
            title: str = '',
            name: str = '',
            common_name: Optional[str]= None,
            url: Optional[Path, str] = None,
            band_data: Optional[np.ndarray]= None,
            pixel_size: Optional[int] = None,
            crs: Optional[str] = None,
            bounds: Optional[List[int]] = None,
            center_wavelength: Optional[float] = None,
            full_width_half_max: Optional[float] = None
    ):
        """
        Initializes the instance parameters

        Args:
            title: Title of the band
            name: Name of the band
            common_name: A common name associated with the band
            url:  Path or URL from which the band data (pixel values) must be retrieved. Ignored if band_data is given.
            band_data: A Numpy array with the pixel_values.
            pixel_size: size of the pixel
            crs: Coordinate Reference System of the image
            bounds: Extent of the band in the format [minx, miny, max, maxy]
            center_wavelength:  Wavelength of the image micrometers
            full_width_half_max: Range starting from center_wavelength of the wavelengths captured by the image
        """
        self.__band_title = title
        self.__band_name = name
        self.__band_common_name = common_name
        self.__band_url = url
        self.__band_pixel_size = pixel_size
        self.__brand_crs = crs
        self.__band_bounds = bounds,
        self.__band_center_wavelength = center_wavelength
        self.__band_full_width_half_max = full_width_half_max
        self.__band_transform = None
        self.init_band_data(band_data)

    @property
    def title(self) -> str:
        """
        Returns:
        The band's title
        """
        return self.__band_title

    @property
    def name(self) -> str:
        """
        Returns:
        The band's name
        """
        return self.__band_name

    @property
    def common_name(self) -> str:
        """
        Returns:
        The band's common name
        """
        return self.__band_common_name

    @property
    def url(self) -> Union[Path, str]:
        """
        Returns:
        The URL from where the data must be retrieved
        """
        return self.__band_url

    @property
    def shape(self) -> Tuple[Optional[int], Optional[int]]:
        """
        Returns:
        A tuple with the width and height of the band
        """
        return self.width, self.height

    @property
    def width(self) -> Optional[int]:
        """
        Returns:
            The width of the image
        """
        return self.__BAND_DATA.shape[1] if self.is_valid() else None

    @property
    def height(self) -> Optional[int]:
        """
        Returns:
            The height of the image
        """
        return self.__BAND_DATA.shape[0] if self.is_valid() else None

    @property
    def size(self) -> Optional[int]:
        """
        Returns:
            The total number of pixels of the image
        """
        return self.__BAND_DATA.size if self.is_valid() else None

    @property
    def crs(self) -> str:
        """
        Returns:
            The Coordinate Reference System of the image
        """
        return self.__brand_crs

    @property
    def bounds(self) -> Optional[List[int]]:
        """
        Returns:
            The extent of the image
        """
        return self.__band_bounds

    @property
    def type(self) -> Optional[str]:
        """
        Returns:
            The Numpy array data type
        """
        return self.__BAND_DATA.dtype if self.is_valid() else None

    @property
    def transform(self) -> rio.Affine:
        """
        Returns:
            The transformation parameters
        """
        return self.__band_transform

    @property
    def pixel_size(self) -> int:
        """
        Returns:
            The pixel size
        """
        return self.__band_pixel_size

    @property
    def center_wavelength(self) -> float:
        """
        Returns:
            The center wavelength
        """
        return self.__band_center_wavelength

    @property
    def full_width_half_max(self) -> float:
        """
        Returns:
            The width of the portion of the electromagnetic spectre captured by the image
        """
        return self.__band_full_width_half_max

    @property
    def data(self) -> np.ndarray:
        """
        Returns:
            A Numpy array with the pixel values of the image
        """
        return self.__BAND_DATA

    @property
    def mean(self) -> Optional[Union[float, int]]:
        """
        Returns:
            The mean of the pixel values in the image (NaN values are ignored)
        """
        return np.nanmean(self.__BAND_DATA, dtype=np.float64) if self.is_valid() else None

    @property
    def min(self) -> Optional[Union[float, int]]:
        """
        Returns:
            The minimum pixel value of the image (NaN values are ignored)
        """
        return np.nanmin(self.__BAND_DATA) if self.is_valid() else None

    @property
    def max(self) -> Optional[Union[float, int]]:
        """
        Returns:
            The maximum pixel value of the image (NaN values are ignored)
        """
        return np.nanmax(self.__BAND_DATA) if self.is_valid() else None

    @property
    def median(self) -> Optional[Union[float, int]]:
        """
        Returns:
            The median of the pixel values in the image (NaN values are ignored)
        """
        return np.nanmedian(self.__BAND_DATA) if self.is_valid() else None

    @property
    def std(self) -> Optional[Union[float, int]]:
        """
        Returns:
            The standard deviation of the pixel values in the image (NaN values are ignored)
        """
        return np.nanstd(self.__BAND_DATA, dtype=np.float64) if self.is_valid() else None

    @property
    def variance(self) -> Optional[Union[float, int]]:
        """
        Returns:
            The variance of the pixel values in the image (NaN values are ignored)
        """
        return np.nanvar(self.__BAND_DATA, dtype=np.float64) if self.is_valid() else None

    def is_valid(self) -> bool:
        """
        Returns:
            Whether the image contains pixel values
        """
        return isinstance(self.__BAND_DATA, np.ndarray)

    def init_band_data(self, band_data: np.ndarray):
        """
        Initializes the pixel values of the image.
        If a numpy array is provided, no external data is fetched
        """
        if isinstance(band_data, np.ndarray):
            self.__BAND_DATA = band_data
            self.__band_url = None
        else:
            if self.url:
                with rio.open(self.url) as band:
                    self.__BAND_DATA = band.read(1)
                    self.__band_bounds = band.bounds
                    self.__brand_crs = band.crs
                    self.__band_transform = band.transform

    def set_transform(self, transform: rio.Affine):
        """
        Sets the image's transform

        Args:
        transform: Affine transformation parameters
        """
        self.__band_transform = transform
