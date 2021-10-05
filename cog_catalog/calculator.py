import matplotlib.pyplot as plt
import numpy as np
from cog_catalog.image import COGImage, BandNotFoundException
from cog_catalog.band import COGImageBand

np.seterr(invalid='ignore')

class NDVICalculator(object):

    def __init__(
        self,
        image=None,
        red_band=None,
        nir_band=None,
        red_band_name='red',
        nir_band_name='nir'
        ):
        self.image = image
        self.red_band = red_band
        self.nir_band = nir_band
        self.red_band_name = red_band_name
        self.nir_band_name = nir_band_name
        self.__calculate_ndvi()

    def __calculate_ndvi(self):
        if self.image:
            self.ndvi = NDVICalculator.ndvi_from_image(
                image=self.image,
                red_band_name=self.red_band_name,
                nir_band_name=self.nir_band_name)
        elif self.red_band and self.nir_band:
            self.ndvi = NDVICalculator.ndvi_from_image_bands(self.red_band, self.nir_band)

    @staticmethod
    def ndvi_from_image(
        image,
        red_band_name='red',
        nir_band_name='nir'
        ):
        try:
            red = image.get_band_by_name(red_band_name)
            nir = image.get_band_by_name(nir_band_name)
            return NDVICalculator.ndvi_from_image_bands(red,nir)
        except BandNotFoundException:
            return None

    @staticmethod
    def ndvi_from_image_bands(red_band, nir_band):
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

    def plot_ndvi(self):
        if self.ndvi:
            plt.imshow(self.ndvi.data)
            plt.colorbar()
            plt.title('NDVI (mean {})'.format(self.ndvi.mean))
            plt.xlabel('Row')
            plt.ylabel('Column')
        else:
            print('Statistics Summary:\nNo NDVI has yet been calculated')

    def summary(self):
        if self.ndvi:
            print('Statistics summary:\nMin: {:.4f}\tMax: {:.4f}\n Mean: {:.4f}\tMedian: {:.4f}\nStd. Dev: {:.4f}\tVariance:{:.4f}'.format(
                self.ndvi.min,
                self.ndvi.max,
                self.ndvi.mean,
                self.ndvi.median,
                self.ndvi.std,
                self.ndvi.variance
                ))
        else:
            print('Statistics Summary:\nNo NDVI has yet been calculated')