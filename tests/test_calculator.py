import unittest
from unittest.mock import patch
import rasterio
import numpy as np
from cog_catalog.calculator import NDVICalculator
from cog_catalog.image import COGImage
from cog_catalog.band import COGImageBand
from mocks import MockRead
from data import feature_data

class TestNDVICalculator(unittest.TestCase):

    def setUp(self):
        self.image = COGImage(geojson=feature_data)
        with patch('rasterio.open') as mock_open:
            mock_open.return_value = MockRead()
            self.band_from_image_1 = self.image.get_band_by_name('B04')
            self.band_from_image_2 = self.image.get_band_by_name('B08')

    def test_ndvi_from_image(self):
        """Test that the NDVI can be generated"""
        with patch('rasterio.open') as mock_open:
            mock_open.return_value = MockRead()
            ndvi = NDVICalculator.ndvi_from_image(self.image, 'B04', 'B08')
        self.assertIsNotNone(ndvi)
        self.assertIsInstance(ndvi, COGImageBand)

    def test_ndvi_from_bands(self):
        """Test that a NDVI from image bands can be generated"""
        ndvi = NDVICalculator.ndvi_from_image_bands(self.band_from_image_1, self.band_from_image_2)
        self.assertIsNotNone(ndvi)
        self.assertIsInstance(ndvi, COGImageBand)


if __name__ == '__main__':
    unittest.main(verbosity=2)