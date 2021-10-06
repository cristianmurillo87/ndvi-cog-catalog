import unittest
from unittest.mock import patch
import requests
from cog_catalog.catalog import COGCatalog
from cog_catalog.image import COGImage
from data import catalog_data


def mock_post_json():
    return catalog_data


class TestCOGCatalog(unittest.TestCase):

    def setUp(self):
        with patch('requests.post') as mock_post:
            mock_post.return_value.ok = True
            mock_post.return_value.json = mock_post_json
            self.catalog = COGCatalog()

    def test_catalog_images(self):
        """Test that images can be retrieved correctly"""
        image_at = self.catalog.get_image_at(0)
        image_by_id = self.catalog.get_image_by_id('S2A_18STJ_20211002_0_L2A')
        images_by_platform = self.catalog.get_images_by_platform('sentinel-2a')
        images_by_collection = self.catalog.get_images_by_collection('sentinel-s2-l2a-cogs')
        self.assertIsNotNone(image_at)
        self.assertIsNotNone(image_by_id)
        self.assertIsInstance(image_at, COGImage)
        self.assertIsInstance(image_by_id, COGImage)
        self.assertGreater(len(images_by_platform), 0)
        self.assertGreater(len(images_by_collection), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
