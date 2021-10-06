"""
This class provides methods to calculate
and to print statistics of the generated NDVI data
"""
import numpy as np
from cog_catalog.image import COGImage, BandNotFoundException
from cog_catalog.band import COGImageBand

from typing import Optional

np.seterr(invalid='ignore')


class NDVICalculator(object):
    """
    Allows to calculate NDVI. Either by passing a COGImage and the name of the
    Near Infrared and Red bands or by passing the corresponding COGImageBand as parameters
    """

    def __init__(
            self,
            image: COGImage = None,
            red_band: COGImageBand = None,
            nir_band: COGImageBand = None,
            red_band_name: str = 'red',
            nir_band_name: str = 'nir'
    ):
        """
        Class initialization

        Args:
            image: a COGImage from whose red and near infrared will be used to generate the NDVI
            red_band: a COGImageBand corresponding to the red band. Ignored if image is given
            nir_band: a COGImageBand corresponding to the near infrared band. Ignored if image is given
            red_band_name: Name of the red band
            nir_band_name: Name of the near infrared band
        """
        self.image = image
        self.red_band = red_band
        self.nir_band = nir_band
        self.red_band_name = red_band_name
        self.nir_band_name = nir_band_name
        self.__calculate_ndvi()

    def __calculate_ndvi(self):
        """
        Calculates the NDVI from the arguments passed to __init__
        """
        if self.image:
            self.ndvi = NDVICalculator.ndvi_from_image(
                image=self.image,
                red_band_name=self.red_band_name,
                nir_band_name=self.nir_band_name)
        elif self.red_band and self.nir_band:
            self.ndvi = NDVICalculator.ndvi_from_image_bands(self.red_band, self.nir_band)

    @staticmethod
    def ndvi_from_image(
            image: COGImage,
            red_band_name: str ='red',
            nir_band_name: str ='nir'
    ) -> Optional[COGImageBand]:
        """
        Calculates the NDVI from a COGImage
        Args:
            image: a COGImage containing the red and near infrared bands metadata
            red_band_name: Name of the red band
            nir_band_name: Name of the near infrared band

        Returns:
            The NDVI as a COGImageBand
        """
        try:
            red = image.get_band_by_name(red_band_name)
            nir = image.get_band_by_name(nir_band_name)
            return NDVICalculator.ndvi_from_image_bands(red, nir)
        except BandNotFoundException:
            return None

    @staticmethod
    def ndvi_from_image_bands(red_band: COGImageBand, nir_band: COGImageBand) -> COGImageBand:
        """
        Calculates the NDVI from two COGImageBand representing the red and near infrared bands
        Args:
            red_band: Red band
            nir_band: Near infrared band

        Returns:
            The NDVI as a COGImageBand
        """
        band_sub = nir_band.data.astype(int) - red_band.data.astype(int)
        band_sum = nir_band.data.astype(int) + red_band.data.astype(int)
        ndvi_arr = band_sub / band_sum
        ndvi = COGImageBand(
            title='NDVI',
            name='ndvi',
            band_data=ndvi_arr,
            crs=nir_band.crs,
            bounds=nir_band.bounds
        )
        return ndvi

    def summary(self):
        """
            Prints some statistics of the calculated NDVI
        """
        if self.ndvi:
            print(
                'Statistics summary:\nMin: {:.4f}\tMax: {:.4f}\n Mean: {:.4f}\tMedian: {:.4f}\n'
                'Std. Dev: {:.4f}\tVariance:{:.4f}'.format(
                    self.ndvi.min,
                    self.ndvi.max,
                    self.ndvi.mean,
                    self.ndvi.median,
                    self.ndvi.std,
                    self.ndvi.variance
                ))
        else:
            print('Statistics Summary:\nNo NDVI has yet been calculated')
