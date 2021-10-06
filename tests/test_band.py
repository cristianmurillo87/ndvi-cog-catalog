import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import rasterio
from cog_catalog.band import COGImageBand
from mocks import mock_read, MockRead


class TestCOGImageBand(unittest.TestCase):

    def setUp(self):
        self.image_band = COGImageBand(
            title='Test Band',
            name='test_band',
            band_data=np.array([[2, 3, 4], [2, 3, 4], [2, 3, 4]]),
            pixel_size=10,
            crs='EPSG:4326',
            bounds=[10, 10, 30, 30]
        )

        self.nan_image_band = COGImageBand(
            title='Test Band Nan',
            name='test_band_nan',
            band_data=np.array([[2, 3, np.nan], [2, 3, 4], [2, np.nan, 4]]),
            pixel_size=10,
            crs='EPSG:4326',
            bounds=[10, 10, 30, 30]
        )

    def test_band_name(self):
        """Test that the name of the band is passed correctly"""
        self.assertEqual(self.image_band.name, 'test_band')

    def test_pixel_size(self):
        """Test that the pixel size of the band is passed correctly"""
        self.assertEqual(self.image_band.pixel_size, 10)

    def test_image_data(self):
        """Test that the image data is a numpy array"""
        self.assertIsInstance(self.image_band.data, np.ndarray)

    def test_statistics(self):
        """Test that the statistics of the image data"""
        self.assertEqual(self.image_band.mean, 3.0)
        self.assertEqual(self.image_band.min, 2)
        self.assertEqual(self.image_band.max, 4)
        self.assertAlmostEqual(self.image_band.std, 0.816, 3)
        self.assertAlmostEqual(self.image_band.variance, 0.667, 3)
        self.assertEqual(self.image_band.median, 3.0)

    def test_nan_statistics(self):
        """Test that the statistics of the image data if NaN values are present"""
        self.assertAlmostEqual(self.nan_image_band.mean, 2.857, 3)
        self.assertEqual(self.nan_image_band.min, 2.0)
        self.assertEqual(self.nan_image_band.max, 4.0)
        self.assertAlmostEqual(self.nan_image_band.std, 0.833, 3)
        self.assertAlmostEqual(self.nan_image_band.variance, 0.694, 3)
        self.assertEqual(self.nan_image_band.median, 3.0)

    def test_array_shape(self):
        """Test that the shape of the image data"""
        self.assertEqual(self.image_band.size, 9)
        self.assertEqual(self.image_band.width, 3)
        self.assertEqual(self.image_band.height, 3)
        self.assertEqual(self.image_band.shape, (3, 3))

    def test_remote_url_band(self):
        """Test that remote data is fetched correctly"""
        with patch('rasterio.open') as mocked_open:
            mocked_open.return_value = MockRead()
            remote_image_band = COGImageBand(
                title='Test Band Remote',
                name='test_band_remote',
                url='https://mock_url/image.tif',
                pixel_size=10
            )
        self.assertIsInstance(remote_image_band.data, np.ndarray)
        self.assertEqual(remote_image_band.size, 9)
        self.assertEqual(remote_image_band.width, 3)
        self.assertEqual(remote_image_band.height, 3)
        self.assertEqual(remote_image_band.shape, (3, 3))
        self.assertEqual(remote_image_band.crs, 'EPSG:4326')
        self.assertEqual(remote_image_band.name, 'test_band_remote')
        mocked_open.assert_called_with('https://mock_url/image.tif')


if __name__ == '__main__':
    unittest.main(verbosity=2)
