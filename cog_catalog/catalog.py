"""
A Catalog of standarized STAC metadata
"""
import requests
import json
from typing import Union, List
from pathlib import Path
from cog_catalog.image import COGImage


class COGCatalog(object):
    """
    This class allows to retrieve metadata about Sentinel and Landsat scenes
    from the Element84 API. The class allows to control which scenes will be
    selected from the API by providing several filter possibilities
    e.g (time, maximum number of elements, collection, area of interest, property queries, etc)
    as well as the possibility to sort the results
    """
    __CATALOG_URL = 'https://earth-search.aws.element84.com/v0/search'
    __IMAGE_LIST = []

    def __init__(
            self,
            limit: int = 10,
            collections: List[str] = ['sentinel-s2-l2a-cogs'],
            time_filter: str = None,
            bbox: List[int] = None,
            aoi: Union[Path, str, None] = None,
            query_obj: Union[dict, None] = None,
            sort_list: Union[List[dict], None] = None
    ):
        """
        Initialize the catalog parameters

        Args:
            limit: The maximum number of features that should be retrieved from the API.
            collections: Only features corresponding to the given collections will be returned
            (e.g 'sentinel-s2-l2a-cogs').
            time_filter: A date-time: "2018-02-12T23:20:50Z" or period: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z".
            bbox: A list of coordinates in the format [minx, miny, max, maxy] to limit the search to a specific area.
            Only objects within this coordinates will be returned.
            aoi: Path to a .geojson file to be used to limit the search to the area covered by the geojson feature.
            Only objects within this coordinates will be returned.
            query_obj: A dictionary with search criteria. See for http://sat-utils.github.io/sat-api/#tocssort examples.
            sort_list: A list with sort criteria. See http://sat-utils.github.io/sat-api/#tocsquery for examples.
        """
        self.update_catalog(limit, collections, time_filter, bbox, aoi, query_obj, sort_list)

    def initialize(self):
        """
        Initializes or updates the image catalog
        """
        payload = self.__generate_request_payload()
        try:
            response = requests.post(self.__CATALOG_URL, json=payload)
            if response.ok:
                json_response = response.json()
                if json_response:
                    self.__update_image_list(json_response)
        except requests.HTTPError:
            self.__IMAGE_LIST = []
            return

    def __generate_request_payload(self) -> dict:
        """
        Creates the payload containing the search, filter and sort criteria to be sent to the API

        Returns:
            A dictionary with the payload data
        """
        payload = {
            'limit': self.__limit
        }

        if isinstance(self.__collections, list) and len(self.__collections) > 0:
            payload['collections'] = self.__collections

        if isinstance(self.__bbox, list) and len(self.__bbox) > 0:
            payload['bbox'] = self.__bbox

        if self.__datetime:
            payload['datetime'] = self.__datetime

        if self.__intersects:
            try:
                with open(self.__intersects, 'r') as geojson_file:
                    geojson = json.load(geojson_file)
                    features = geojson.get('features', [])
                    if len(features) > 0:
                        feature = features[0]
                        payload['intersects'] = feature.get('geometry')
            except Exception:
                print('Error loading {}'.format(self.__intersects))

        if isinstance(self.__query, dict):
            payload['query'] = self.__query

        if len(self.__sort) > 0:
            payload['sort'] = self.__sort

        return payload

    def __update_image_list(self, geojson: dict):
        """
        Updates the image list using the features provided in the geojson argument
        """
        self.__IMAGE_LIST = []
        features = geojson.get('features', [])
        for feature in features:
            image = self.__create_image_from_feature(feature)
            self.__IMAGE_LIST.append(image)

    def __create_image_from_feature(self, geojson_feature: dict={}) -> COGImage:
        """
        Creates a COGImage using a geojson feature

        Args:
            geojson_feature: A dictionary in the format of a geojson feature following the structure of the
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
        return COGImage(geojson_feature)

    def update_catalog(
            self,
            limit=10,
            collections=None,
            time_filter=None,
            bbox=None,
            aoi=None,
            query_obj=None,
            sort_list=None
    ):
        """
        Updates the catalog parameters

        Args:
            limit: The maximum number of features that should be retrieved from the API.
            collections: Only features corresponding to the given collections will be returned
            (e.g 'sentinel-s2-l2a-cogs').
            time_filter: A date-time: "2018-02-12T23:20:50Z" or period: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z".
            bbox: A list of coordinates in the format [minx, miny, max, maxy] to limit the search to a specific area.
            Only objects within this coordinates will be returned.
            aoi: Path to a .geojson file to be used to limit the search to the area covered by the geojson feature.
            Only objects within this coordinates will be returned.
            query_obj: A dictionary with search criteria. See for http://sat-utils.github.io/sat-api/#tocssort examples.
            sort_list: A list with sort criteria. See http://sat-utils.github.io/sat-api/#tocsquery for examples.
        """
        self.__limit = limit
        self.__bbox = bbox
        self.__datetime = time_filter
        self.__intersects = aoi
        self.__collections = collections
        self.__query = query_obj
        self.__sort = sort_list or []
        self.initialize()

    def get_image_at(self, index: int) -> Union[COGImage, None]:
        """
        Returns the COGImage located at the specified index.

        Args:
            index: Index of the image

        Returns:
            The COGImage located at the specified index or None if not found.
        """
        if len(self.__IMAGE_LIST) >= index + 1:
            return self.__IMAGE_LIST[index]
        return None

    def get_image_by_id(self, image_id: str) -> Union[COGImage, None]:
        """
        Returns the COGImage that matches the given ID.

        Args:
            image_id: Index of the image

        Returns:
            The COGImage that matches the given ID or None if not found.
        """
        matches = list(filter(lambda img: img.id == image_id, self.__IMAGE_LIST))
        return matches[0] if len(matches) > 0 else None

    def get_image_by_product_id(self, product_id: str) -> Union[COGImage, None]:
        """
        Returns the COGImage that matches the given product ID.

        Args:
            product_id: Index of the image

        Returns:
            The COGImage that matches the given product ID or None if not found.
        """
        matches = list(filter(lambda img: img.product_id == product_id, self.__IMAGE_LIST))
        return matches[0] if len(matches) > 0 else None

    def get_images_by_collection(self, collection_name: str) -> List[COGImage]:
        """
        Returns a list of all the COGImage in the catalog whose "collection" matches the given collection.

        Args:
            collection_name: Name of the collection (e.g sentinel-s2-l2a-cogs)

        Returns:
            A list of matching COGImage.
        """
        return list(filter(lambda img: img.collection == collection_name, self.__IMAGE_LIST))

    def get_images_by_platform(self, platform: str) -> List[COGImage]:
        """
        Returns a list of all the COGImage in the catalog whose "platform" matches the given value.

        Args:
            platform: Name of the platform (e.g. sentinel-2a).

        Returns:
            A list of matching COGImage.
        """
        return list(filter(lambda img: img.platform == platform, self.__IMAGE_LIST))

    def get_images_by_constellation(self, constellation: str) -> List[COGImage]:
        """
        Returns a list of all the COGImage in the catalog whose "constellation" matches the given value.

        Args:
            constellation: Name of the constellation (e.g. sentinel-2).

        Returns:
            A list of matching COGImage.
        """
        return list(filter(lambda img: img.constellation == constellation, self.__IMAGE_LIST))
