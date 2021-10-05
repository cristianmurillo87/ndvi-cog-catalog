from cog_catalog.catalog import COGCatalog
from cog_catalog.calculator import NDVICalculator
sentinel_cog_catalog = COGCatalog(
    limit=1,
    collections=['sentinel-s2-l2a-cogs'],
    aoi='assets/doberitzer_heide.geojson',
    time_filter='2018-02-12T00:00:00Z/2018-03-18T12:31:12Z'
)
image = sentinel_cog_catalog.get_image_at(0)
red_band_name = 'B04'
nir_band_name = 'B08'
if image:
    red_band = image.get_band_by_name(red_band_name)
    nir_band = image.get_band_by_name(nir_band_name)
    print('Name: {} Min:{:.4f}\tMax:{:.4f}'.format(red_band.name, red_band.min, red_band.max))
    print('Name:{} Min:{:.4f}\tMax:{:.4f}'.format(nir_band.name, nir_band.min, nir_band.max))

    ndvi = NDVICalculator.ndvi_from_image_bands(red_band, nir_band)
    print('Name: NDVI Min:{:.4f}\tMax:{:.4f}\tMean: {:.4f}'.format(ndvi.min, ndvi.max, ndvi.mean))