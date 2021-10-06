import unittest
from cog_catalog.image import COGImage, BandNotFoundException
from cog_catalog.band import COGImageBand
from data import feature_data, update_feature_data


class TestCOGImage(unittest.TestCase):

    def setUp(self):
        self.test_image = COGImage(geojson=feature_data)

    def test_image_properties(self):
        """Test the image properties are set correctly """
        properties = feature_data.get('properties', {})
        self.assertEqual(self.test_image.id, feature_data.get('id'))
        self.assertEqual(self.test_image.collection, feature_data.get('collection'))
        self.assertEqual(self.test_image.datetime, properties.get('datetime'))
        self.assertEqual(self.test_image.cloud_cover, properties.get('eo:cloud_cover'))
        self.assertEqual(self.test_image.platform, properties.get('platform'))
        self.assertEqual(self.test_image.constellation, properties.get('constellation'))
        self.assertEqual(self.test_image.pixel_size, properties.get('gsd'))
        self.assertEqual(self.test_image.product_id, properties.get('sentinel:product_id'))
        self.assertEqual(self.test_image.crs, properties.get('proj:epsg'))

    def test_image_bands(self):
        """Test that bands in the image can be accessed"""
        band = self.test_image.get_band_by_name('B01')
        band_name = 'False band'
        self.assertEqual(self.test_image.num_bands, 12)
        self.assertEqual(len(self.test_image.bands), 12)
        self.assertIn(dict(name='B01', title='Band 1 (coastal)'), self.test_image.bands)
        self.assertIsInstance(band, COGImageBand)

        with self.assertRaises(BandNotFoundException) as excep:
            self.test_image.get_band_by_name(band_name)

        self.assertIsInstance(excep.exception, BandNotFoundException)
        self.assertEqual(excep.exception.message, 'No band name {} was found'.format(band_name))

    def test_update_bands(self):
        """Test that the band list is updated"""
        self.test_image.update_band_list(feature_assets_obj=update_feature_data.get('assets', {}))
        self.assertEqual(self.test_image.num_bands, 7)
        self.assertEqual(len(self.test_image.bands), 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
