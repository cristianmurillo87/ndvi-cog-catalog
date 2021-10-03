import matplotlib.pyplot as plt
from image import COGImage, BandNotFoundException

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
        self.ndvi = None

    def calculate_ndv(self):
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
        ndvi_arr = (nir_band.data - red_band.data) / (nir_band.data + red_band.data)
        ndvi = COGImageBand(
            title='NDVI',
            name='ndvi',
            band_data=ndvi_arr,
            crs=nir_band.crs,
            bounds=nir.bounds
        )
        return ndvi

    def plot_ndvi(self):
        if self.ndvi:
            plt.imshow(self.ndvi.data)
            plt.colorbar()
            plt.title('NDVI (mean {})'.format(self.ndvi.mean))
            plt.xlabel('Row')
            plt.ylabel('Column')

    def summary(self):
        if self.ndvi:
            print("""
                Statistics summary:
                Mean: {}\tMedian: {}
                Std. Dev: {}\tVariance:{}
            """.format(
                self.ndvi.mean,
                self.ndvi.median,
                self.ndvi.std,
                self.ndiv.variance
                )
                )
        else:
            print('Statistics Summary:\nNo ndvi has yet been calculated')