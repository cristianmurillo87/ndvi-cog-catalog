from cog_catalog.catalog import COGCatalog
from cog_catalog.calculator import NDVICalculator

# Create a catalog to store the image metadata
# the catalog will have a maximum of 3 Sentinel 2 COG taken within
# the time period given and located in the area described by the .geojson file
sentinel_cog_catalog = COGCatalog(
    limit=3,
    collections=['sentinel-s2-l2a-cogs'],
    aoi='assets/doberitzer_heide.geojson',
    time_filter='2018-02-12T00:00:00Z/2018-03-18T12:31:12Z'
)
# retrieve an image from the catalog using an index
image = sentinel_cog_catalog.get_image_at(0)
red_band_name = 'B04'
nir_band_name = 'B08'
if image:
    # access the bands of the images by name
    red_band = image.get_band_by_name(red_band_name)
    nir_band = image.get_band_by_name(nir_band_name)

    # print properties of the bands
    print('Name: {} Min:{:.4f}\tMax:{:.4f}'.format(red_band.name, red_band.min, red_band.max))
    print('Name:{} Min:{:.4f}\tMax:{:.4f}'.format(nir_band.name, nir_band.min, nir_band.max))

    # Calculate the NDVI and print some statistics
    ndvi = NDVICalculator.ndvi_from_image_bands(red_band, nir_band)
    print('Name: NDVI Min:{:.4f}\tMax:{:.4f}\tMean: {:.4f}'.format(ndvi.min, ndvi.max, ndvi.mean))