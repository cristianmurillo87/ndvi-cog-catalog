import requests
from image import COGImage

class COGCatalog(object):

    __CATALOG_URL = 'https://earth-search.aws.element84.com/v0/search'
    __IMAGE_LIST = []

    def __init__(
        self,
        limit=10,
        collections=None,
        time_filter=None,
        bbox=None,
        aoi=None,
        query_obj=None,
        sort_list=None
        ):
        """Initialize the catalog parameters"""
        self.update_catalog(limit, collections, time_filter, bbox, aoi, query_obj, sort_list)
        

    def initialize(self):
        payload = self.__generate_request_payload()
        try:
            response = requests.post(self.__CATALOG_URL, data=payload)
            json_response = response.json()
            if json_response:
                self.__update_image_list(json_response)
        except requests.HTTPError:
            return

    def __generate_request_payload(self):
        payload = {
            'limit': self.__limit
        }

        if len(self.__collections) > 0:
            payload['collections'] = self.__collections
        
        if len(self.__intersects) > 0:
            payload['bbox'] = self.__bbox
        
        if self.__datetime:
            payload['datetime'] = self.__datetime
        
        if self.__intersects:
            payload['intersects'] = self.__intersects
        
        if isinstance(self.__query, dict):
            payload['query'] = self.__query

        if len(self.__sort) > 0:
            payload['sort'] = self.__sort

    def __update_image_list(self, geojson):
        self.__IMAGE_LIST = []
        features = geojson.get('features', [])
        for feature in features:
            image = self.__create_image_from_feature(feature)
            self.__IMAGE_LIST.append(image)

    def __create_image_from_feature(self, geojson_feature={}):
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
        self.__limit = limit
        self.__bbox = bbox
        self.__datetime = time_filter
        self.__intersects = aoi
        self.__collections = collections or ['sentinel-s2-l2a-cogs']
        self.__query = query_obj
        self.__sort = sort_list or []
        self.initialize()

    def get_image_at(self, index):
        if len(self.__IMAGE_LIST) >= index + 1:
            return self.__IMAGE_LIST[index]
        return None
        
    def get_image_by_id(self, image_id):
        matches = filter(lambda img: img.id == image_id, self.__IMAGE_LIST)
        return matches[0] if len(matches) > 0 else None

    def get_image_by_product_id(self, product_id):
        matches = filter(lambda img: img.product_id == product_id, self.__IMAGE_LIST)
        return matches[0] if len(matches) > 0 else None

    def get_images_by_collection(self, collection_name):
        return filter(lambda img: img.collection == collection_name, self.__IMAGE_LIST)

    def get_images_by_platform(self, platform):
        return filter(lambda img: img.platform == platform, self.__IMAGE_LIST)
    
    def get_images_by_platform(self, constellation):
        return filter(lambda img: img.constellation == constellation, self.__IMAGE_LIST)