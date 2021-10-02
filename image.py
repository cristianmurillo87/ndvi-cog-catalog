class COGImage(object):

    BAND_INFO_LIST = []

    def __init__(self, geojson={}):
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
    def id(self):
        return self.__id

    @property
    def collection(self):
        return self.__collection

    @property
    def platform(self):
        return self.__platform
    
    @property
    def datetime(self):
        return self.__datetime

    @property
    def pixel_size(self):
        return self.__pixel_size

    @property
    def constellation(self):
        return self.__constellation
    
    @property
    def cloud_cover(self):
        return self.__cloud_cover
    
    @property
    def crs(self):
        return self.__crs
    
    @property
    def data_coverage(self):
        return self.__data_coverage
    
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def created_at(self):
        return self.__created_at
    
    @property
    def last_updated(self):
        return self.__last_updated

    @property
    def num_bands(self):
        return len(self.BAND_INFO_LIST)

    @property
    def bands(self):
        return map(lambda band: band.get('name'), self.BAND_INFO_LIST)

    def update_band_list(self, feature_assets_obj={}):
        self.BAND_INFO_LIST = []
        for asset_key, asset_value in feature_assets_obj.keys():
            if asset_key in ('thumbnail', 'overview', 'info', 'metadata', 'visual'):
                continue
            
            band_info = asset_value.get('eo:bands', [])
            new_band_obj = {
                'title': asset_value.get('title'),
                'type': asset_value.get(''),
                'url': asset_value.get('href'),
                'pixel_size': asset_value.get('gsd'),
                'shape': asset_value.get('proj:shape'),
                'transform': asset_value.get('proj:transform')
            }

            if len(band_info) > 0:
                band_properties = band_info[0]
                new_band_obj['center_wavelength'] = band_properties.get('center_wavelength')
                new_band_obj['full_width_half_max'] = band_properties.get('full_width_half_max')
                new_band_obj['name'] = band_properties.get('name')

            self.BAND_INFO_LIST.append(new_band_obj)

    def get_band_by_name(self, band_name):
        for band in self.BAND_INFO_LIST:
            if band.get('name') == band_name:
                return COGImageBand(**band)
        return None