import click
from cog_catalog.catalog import COGCatalog
from cog_catalog.calculator import NDVICalculator


@click.command()
@click.option('--time_range', '-t',
              default='latest',
              nargs=1, type=str,
              help='A date-time: "2018-02-12T23:20:50Z" or period: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"')
@click.option('--geojson', '-g',
              default='assets/doberitzer_heide.geojson',
              type=str,
              nargs=1,
              help='Path to a geojson file used to retrieve only images that intersect with its geometry')
@click.option('--red_band', '-r', default='B04', type=str, nargs=1, help='Name or common name of the red band')
@click.option('--nir_band', '-n',
              default='B08',
              type=str,
              nargs=1,
              help='Name or common name of the near infrared band')
@click.option('--operation', '-o',
              default='mean',
              type=str,
              nargs=1,
              help='Determines what value should be printed after calculating the NDVI')
def calculate_ndvi(time_range, geojson, red_band, nir_band, operation):
    try:
        time_filter = time_range if time_range != 'latest' else None
        sort_list = [dict(field='datetime', direction='desc'), dict(field='date', direction='desc')] if time_filter \
            else None
        sentinel_cog_catalog = COGCatalog(
                                    limit=1,
                                    collections=['sentinel-s2-l2a-cogs'],
                                    aoi=geojson,
                                    time_filter=time_filter,
                                    sort_list=sort_list
        )
        image = sentinel_cog_catalog.get_image_at(0)

        if image:
            print('=' * 60)
            template = 'Image Information\nID: {}\nPlatform: {}\nCollection: {}\nDate: {}\nCloud Cover: {}%'
            print(template.format(image.id, image.platform, image.collection, image.datetime, image.cloud_cover))
            print('='*60)
            ndvi_calculator = NDVICalculator(image=image, red_band_name=red_band, nir_band_name=nir_band)
            ndvi = ndvi_calculator.ndvi
            if operation == 'mean':
                print('Mean NDVI: {:.4f}'.format(ndvi.mean))
            elif operation == 'median':
                print('Median NDVI: {:.4f}'.format(ndvi.median))
            elif operation == 'min':
                print('Minimum NDVI value: {:.4f}'.format(ndvi.min))
            elif operation == 'max':
                print('Maximum NDVI value: {:.4f}'.format(ndvi.max))
            elif operation == 'std':
                print('Standard Deviation of the calculated NDVI: {:.4f}'.format(ndvi.std))
            elif operation == 'var':
                print('Variance of the calculated NDVI: {:.4f}'.format(ndvi.variance))
            else:
                ndvi_calculator.summary()
    except Exception:
        print('Error occured while trying to calculate the NDVI. Please check the arguments given in the command line')


if __name__ == '__main__':
    calculate_ndvi()
