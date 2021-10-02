import requests
from image import COGImage

class COGCatalog(object):

    CATALOG_URL = 'https://earth-search.aws.element84.com/v0/search'
    IMAGE_LIST = []

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
        
        self.__limit = limit
        self.__bbox = bbox
        self.__datetime = time_filter
        self.__intersects = aoi
        self.__collections = collections or ['sentinel-s2-l2a-cogs']
        self.__query = query_obj
        self.__sort = sort_list or []

    def initialize(self):
        payload = self.__generate_request_payload()
        try:
            response = requests.post(self.CATALOG_URL, data=payload)
            json_response = response.json()
            if json_response:
                self.update_image_list(json_response)
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

    def update_image_list(self, geojson):
        self.IMAGE_LIST = []
        features = geojson.get('features', [])
        for feature in features:
            image = self.create_image_from_feature(feature)
            self.IMAGE_LIST.append(image)

    def create_image_from_feature(self, geojson_feature={}):
        return COGImage(geojson_feature)

