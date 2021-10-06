import numpy as np
import rasterio


def mock_read(index):
    return np.array([[2, 3, 4], [2, 3, 4], [2, 3, 4]])


class MockRead(object):
    def __init__(self):
        self.crs = 'EPSG:4326'
        self.transform = rasterio.Affine(1.1, 1.2, 1.3, 1.4, 1.5, 1.6)
        self.bounds = [10, 10, 30, 30]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def read(self, index):
        return np.array([[2, 3, 4], [2, 3, 4], [2, 3, 4]])
