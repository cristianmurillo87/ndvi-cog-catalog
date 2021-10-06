### NDVI Calculator for COG

This project aims to provide to an interface that allows calculating the NDVI for satellite image scenes
obtained through the Element84 API. It can be used either as a Python script or as a command line interface (CLI). Both options 
to filter which scenes from the API; the only difference being that when used as a CLI, the result
is restricted to a single image whereas using the script variant, the user has more control over which 
results are retrieved.

### Setup
This script was developed using Python > = 3.6 and the following packages must be available in the Python installation
or virtual environment used to run the script/command-line:

- requests
- numpy
- scipy
- boto3
- rasterio
- click

These packages can be installed using the `requirements.txt` file available in this repository:

```bash
pip install requirements.txt
```

### Running the Script

#### As a Command Line Interface
Using the script as CLI calculates the NDVI for a single satellite image.
After calculating the NDVI, it prints the mean NDVI of the image values if no other value is given
using the `--operation - o` option.

Additional options can be given in order to define for which the NDVI is calculated.
Such options can be listed using the following command:

Assuming the current location in the terminal is the same as that of the `ndvi.py` file

```bash
python ndvi.py --help
```

It would print

```bash
Usage: ndvi.py [OPTIONS]

Usage: ndvi.py [OPTIONS]

Options:
  -t, --time_range TEXT  A date-time: "2018-02-12T23:20:50Z" or period:
                         "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"

  -g, --geojson TEXT     Path to a geojson file used to retrieve only images
                         that intersect with its geometry

  -r, --red_band TEXT    Name or common name of the red band
  -n, --nir_band TEXT    Name or common name of the near infrared band
  -o, --operation TEXT   Determines what value should be printed after
                         calculating the NDVI. The possible values are: mean,
                         median, std, var, min, max, summary

  --help                 Show this message and exit.

```


##### Example:

```bash
python ndvi.py -g assets/doberitzer_heide.json -r B04 -n B08 -o summary
```

Using the command above would print:

```
============================================================
Image Information
ID: S2B_32UQD_20211005_0_L2A
Platform: sentinel-2b
Collection: sentinel-s2-l2a-cogs
Date: 2021-10-05T10:16:14Z

============================================================
Statistics summary:
Min: -0.0488    Max: 0.0949
Mean: 0.0146   Median: 0.0147
Std. Dev: 0.0054        Variance:0.0000

``` 
 
 Which would correspond to a statistical summary for the NDVI calculated for the
 latest Sentinel 2 image available in the area described by the `assets/doberitzer_heide.json` file.
 

#### As a script

This allows more flexibility than the CLI options since additional parameters for the search can be given.

Example:

````python

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
````

#### Statistics
The purpose was originally to print only the mean NDVI. But since the mean is so sensitive to blunders or atipical values;
using it alone might lead to erroneous assumptions regarding the meaning of the obtained result. Therefore it was decided
to provide additional statistical measurements like the median (which is not as affected by such atypical values as the mean),
standard deviation, variance, minimum and maximum  so that a better understanding of the NDVI values distribution can be obtained.
