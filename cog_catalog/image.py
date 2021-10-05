"""
A representation of a single feature element from the FeatureCollection returned
when searching images from the Element84 API.
"""
from cog_catalog.band import COGImageBand
from typing import List


class BandNotFoundException(Exception):
    """
    Exception that can be raised if a band cannot be found within a COGImage object
    """
    def __init__(self, band_name=None, message=None):
        if message:
            self.message = message
        if band_name:
            self.message = 'No band name {} was found'.format(band_name)


class COGImage(object):
    """
    This class holds the metadata of a scene returned by the Element84 API.
    The metadata of the bands of the scene is also stored here. Note that this
    class only holds the metadata associated to the scene and its bands and
    no data is downloaded here.
    """
    BAND_INFO_LIST = []

    def __init__(self, geojson: dict={}):
        """
        Initializes the instance

        Args:
            geojson: A dictionary in the format of a geojson feature following the structure of the
            Element84 API.
            Example:
                {
                  "type": "Feature",
                  "stac_version": "1.0.0-beta.2",
                  "stac_extensions": [],
                  "id": "",
                  "bbox": [],
                  "geometry": {},
                  "properties": {},
                  "collection": "sentinel-s2-l2a-cogs",
                  "assets": {
                      "B01": {},
                      "B02": {},
                      "B03": {}
                  }
                }
        """
        properties = geojson.get('properties', {})
        self.__id = geojson.get('id')
        self.__collection = geojson.get('collection')
        self.__datetime = properties.get('datetime')
        self.__platform = properties.get('platform')
        self.__constellation = properties.get('constellation')
        self.__pixel_size = properties.get('gsd')
        self.__cloud_cover = properties.get('eo:cloud_cover')
        self.__crs = properties.get('proj:epsg')
        self.__data_coverage = properties.get('data_coverage')
        self.__product_id = properties.get('sentinel:product_id')
        self.__created_at = properties.get('created')
        self.__last_updated = properties.get('updated')
        self.update_band_list(geojson.get('assets'))

    @property
    def id(self) -> str:
        """
        Returns the ID of the image

        Returns:
            The ID of the image
        """
        return self.__id

    @property
    def collection(self) -> str:
        """
        Returns the collection of the image

        Returns:
            The collection of the image
        """
        return self.__collection

    @property
    def platform(self) -> str:
        """
        Returns the platform of the image

        Returns:
            The platform of the image
        """
        return self.__platform

    @property
    def datetime(self) -> str:
        """
        Returns the datetime of the image

        Returns:
            The datetime of the image
        """
        return self.__datetime

    @property
    def pixel_size(self) -> int:
        """
        Returns the pixel size of the image. Note that each COGImageBand may have a different pixel size

        Returns:
            The pixel size of the image
        """
        return self.__pixel_size

    @property
    def constellation(self) -> str:
        """
        Returns the constellation of the image

        Returns:
            The constellation of the image
        """
        return self.__constellation

    @property
    def cloud_cover(self) -> float:
        """
        Returns the percentage of cloud cover of the image

        Returns:
            The percentage of cloud cover of the image
        """
        return self.__cloud_cover

    @property
    def crs(self) -> str:
        """
        Returns the code of the Coordinate Reference System associated to the image

        Returns:
            The code of the Coordinate Reference System associated to the image
        """
        return self.__crs

    @property
    def data_coverage(self) -> float:
        """
        Returns the percentage of data coverage of the image

        Returns:
            The percentage of data coverage of the image
        """
        return self.__data_coverage

    @property
    def product_id(self) -> str:
        """
        Returns the product ID of the image.

        Returns:
            The product ID of the image
        """
        return self.__product_id

    @property
    def created_at(self) -> str:
        """
        Returns the datetime when the image was made available in the Element84 API.

        Returns:
            The datetime when the image was made available in the Element84 API.
        """
        return self.__created_at

    @property
    def last_updated(self) -> str:
        """
        Returns the datetime when the image was updated in the Element84 API.

        Returns:
            The datetime when the image was updated in the Element84 API.
        """
        return self.__last_updated

    @property
    def num_bands(self) -> int:
        """
        Returns the number of bands available in the image

        Returns:
            The number of bans of the image.
        """
        return len(self.BAND_INFO_LIST)

    @property
    def bands(self) -> List[dict]:
        """
        Returns a list of dictionaries containing the name and title of each of the
        bands available in the image.

        Returns:
            A list with information about the bands in the image.
        """
        return list(map(lambda band: dict(name=band.get('name'), title=band.get('title')), self.BAND_INFO_LIST))

    def update_band_list(self, feature_assets_obj: dict={}):
        """
        Updated the list of bands of the image

        Args:
            feature_assets_obj: a dictionary corresponding to the "assets" key
            of a feature returned by the Element84 API
        """
        self.BAND_INFO_LIST = []
        for asset_key, asset_value in feature_assets_obj.items():

            # only add to self.BAND_INFO_LIST the metadata associated to the actual image bands
            if asset_key in ('thumbnail', 'overview', 'info', 'metadata', 'visual'):
                continue

            band_info = asset_value.get('eo:bands', [])
            new_band_obj = {
                'title': asset_value.get('title'),
                'url': asset_value.get('href'),
                'pixel_size': asset_value.get('gsd'),
                'crs': 'EPSG:{}'.format(self.__crs) if self.__crs else None
            }

            if len(band_info) > 0:
                band_properties = band_info[0]
                new_band_obj['center_wavelength'] = band_properties.get('center_wavelength')
                new_band_obj['full_width_half_max'] = band_properties.get('full_width_half_max')
                new_band_obj['name'] = band_properties.get('name')
                new_band_obj['common_name'] = band_properties.get('common_name')

            if new_band_obj.get('name'):
                self.BAND_INFO_LIST.append(new_band_obj)

    def get_band_by_name(self, band_name: str) -> COGImageBand:
        """
        Returns the COGImageBand whose name or common_name (if exists) matches the given value.

        Returns:
            The COGImageBand whose name or common name matches the given value.

        Raises:
            A BandNotFoundException if no COGImageBand with the specified name is found
        """
        for band in self.BAND_INFO_LIST:
            if band.get('name') == band_name or band.get('common_name') == band_name:
                return COGImageBand(**band)
        raise BandNotFoundException(band_name=band_name)