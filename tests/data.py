catalog_data = {
    'type': 'FeatureCollection',
    'stac_version': '1.0.0-beta.2',
    'stac_extensions': [],
    'context': {
        'page': 1,
        'limit': 3,
        'matched': 472,
        'returned': 3
    },
    'numberMatched': 472,
    'numberReturned': 3,
    'features': [
        {
            'type': 'Feature',
            'stac_version': '1.0.0-beta.2',
            'stac_extensions': [
                'eo',
                'view',
                'proj'
            ],
            'id': 'S2A_18STJ_20211002_0_L2A',
            'bbox': [
                -77.95337796105937,
                38.72355003898747,
                -77.1886636996379,
                39.575037252516026
            ],
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [
                            -77.95337796105937,
                            38.72355003898747
                        ],
                        [
                            -77.7020628230002,
                            39.575037252516026
                        ],
                        [
                            -77.3795834273484,
                            39.528820064497175
                        ],
                        [
                            -77.21244463164855,
                            39.504374168834815
                        ],
                        [
                            -77.1886636996379,
                            38.74037874635374
                        ],
                        [
                            -77.95337796105937,
                            38.72355003898747
                        ]
                    ]
                ]
            },
            'properties': {
                'datetime': '2021-10-02T16:02:33Z',
                'platform': 'sentinel-2a',
                'constellation': 'sentinel-2',
                'instruments': [
                    'msi'
                ],
                'gsd': 10,
                'view:off_nadir': 0,
                'proj:epsg': 32618,
                'sentinel:utm_zone': 18,
                'sentinel:latitude_band': 'S',
                'sentinel:grid_square': 'TJ',
                'sentinel:sequence': '0',
                'sentinel:product_id': 'S2A_MSIL2A_20211002T155101_N0301_R054_T18STJ_20211002T201235',
                'sentinel:data_coverage': 40.6,
                'eo:cloud_cover': 3.89,
                'sentinel:valid_cloud_cover': True,
                'created': '2021-10-02T22:07:56.585Z',
                'updated': '2021-10-02T22:07:56.585Z'
            },
            'collection': 'sentinel-s2-l2a-cogs',
            'assets': {
                'thumbnail': {
                    'title': 'Thumbnail',
                    'type': 'image/png',
                    'roles': [
                        'thumbnail'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/18/S/TJ/2021/10/2/0/preview.jpg'
                },
                'overview': {
                    'title': 'True color image',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'overview'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        },
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        },
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/L2A_PVI.tif',
                    'proj:shape': [
                        343,
                        343
                    ],
                    'proj:transform': [
                        320,
                        0,
                        199980,
                        0,
                        -320,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'info': {
                    'title': 'Original JSON metadata',
                    'type': 'application/json',
                    'roles': [
                        'metadata'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TJ/2021/10/2/0/tileInfo.json'
                },
                'metadata': {
                    'title': 'Original XML metadata',
                    'type': 'application/xml',
                    'roles': [
                        'metadata'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TJ/2021/10/2/0/metadata.xml'
                },
                'visual': {
                    'title': 'True color image',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'overview'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        },
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        },
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/TCI.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B01': {
                    'title': 'Band 1 (coastal)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 60,
                    'eo:bands': [
                        {
                            'name': 'B01',
                            'common_name': 'coastal',
                            'center_wavelength': 0.4439,
                            'full_width_half_max': 0.027
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B01.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        199980,
                        0,
                        -60,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B02': {
                    'title': 'Band 2 (blue)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B02.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B03': {
                    'title': 'Band 3 (green)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B03.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B04': {
                    'title': 'Band 4 (red)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B04.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B05': {
                    'title': 'Band 5',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B05',
                            'center_wavelength': 0.7039,
                            'full_width_half_max': 0.019
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B05.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B06': {
                    'title': 'Band 6',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B06',
                            'center_wavelength': 0.7402,
                            'full_width_half_max': 0.018
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B06.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B07': {
                    'title': 'Band 7',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B07',
                            'center_wavelength': 0.7825,
                            'full_width_half_max': 0.028
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B07.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B08': {
                    'title': 'Band 8 (nir)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B08',
                            'common_name': 'nir',
                            'center_wavelength': 0.8351,
                            'full_width_half_max': 0.145
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B08.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B8A': {
                    'title': 'Band 8A',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B8A',
                            'center_wavelength': 0.8648,
                            'full_width_half_max': 0.033
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B8A.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B09': {
                    'title': 'Band 9',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 60,
                    'eo:bands': [
                        {
                            'name': 'B09',
                            'center_wavelength': 0.945,
                            'full_width_half_max': 0.026
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B09.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        199980,
                        0,
                        -60,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B11': {
                    'title': 'Band 11 (swir16)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B11',
                            'common_name': 'swir16',
                            'center_wavelength': 1.6137,
                            'full_width_half_max': 0.143
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B11.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'B12': {
                    'title': 'Band 12 (swir22)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B12',
                            'common_name': 'swir22',
                            'center_wavelength': 2.22024,
                            'full_width_half_max': 0.242
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B12.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'AOT': {
                    'title': 'Aerosol Optical Thickness (AOT)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/AOT.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        199980,
                        0,
                        -60,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'WVP': {
                    'title': 'Water Vapour (WVP)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/WVP.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4400040,
                        0,
                        0,
                        1
                    ]
                },
                'SCL': {
                    'title': 'Scene Classification Map (SCL)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/SCL.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4400040,
                        0,
                        0,
                        1
                    ]
                }
            },
            'links': [
                {
                    'rel': 'self',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_18STJ_20211002_0_L2A'
                },
                {
                    'rel': 'canonical',
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/S2A_18STJ_20211002_0_L2A.json',
                    'type': 'application/json'
                },
                {
                    'title': 'sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TJ-2021-10-2-0',
                    'rel': 'via-cirrus',
                    'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TJ-2021-10-2-0'
                },
                {
                    'title': 'Source STAC Item',
                    'rel': 'derived_from',
                    'href': 'https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/S2A_18STJ_20211002_0_L2A.json',
                    'type': 'application/json'
                },
                {
                    'title': 'sentinel-s2-l2a/workflow-cog-archive/S2A_18STJ_20211002_0_L2A',
                    'rel': 'via-cirrus',
                    'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_18STJ_20211002_0_L2A'
                },
                {
                    'rel': 'parent',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
                },
                {
                    'rel': 'collection',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
                },
                {
                    'rel': 'root',
                    'href': 'https://earth-search.aws.element84.com/v0/'
                }
            ]
        },
        {
            'type': 'Feature',
            'stac_version': '1.0.0-beta.2',
            'stac_extensions': [
                'eo',
                'view',
                'proj'
            ],
            'id': 'S2A_18STH_20210912_0_L2A',
            'bbox': [
                -78.20755995927591,
                37.815749078158476,
                -77.161763815112,
                38.82843053932372
            ],
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [
                            -78.20755995927591,
                            37.815749078158476
                        ],
                        [
                            -77.91721702219844,
                            38.81255036936634
                        ],
                        [
                            -77.19135849244294,
                            38.82843053932372
                        ],
                        [
                            -77.161763815112,
                            37.83960429207432
                        ],
                        [
                            -78.20755995927591,
                            37.815749078158476
                        ]
                    ]
                ]
            },
            'properties': {
                'datetime': '2021-09-12T16:02:42Z',
                'platform': 'sentinel-2a',
                'constellation': 'sentinel-2',
                'instruments': [
                    'msi'
                ],
                'gsd': 10,
                'view:off_nadir': 0,
                'proj:epsg': 32618,
                'sentinel:utm_zone': 18,
                'sentinel:latitude_band': 'S',
                'sentinel:grid_square': 'TH',
                'sentinel:sequence': '0',
                'sentinel:product_id': 'S2A_MSIL2A_20210912T154911_N0301_R054_T18STH_20210912T201501',
                'sentinel:data_coverage': 70.68,
                'eo:cloud_cover': 0,
                'sentinel:valid_cloud_cover': True,
                'created': '2021-09-12T22:29:41.569Z',
                'updated': '2021-09-12T22:29:41.569Z'
            },
            'collection': 'sentinel-s2-l2a-cogs',
            'assets': {
                'thumbnail': {
                    'title': 'Thumbnail',
                    'type': 'image/png',
                    'roles': [
                        'thumbnail'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/18/S/TH/2021/9/12/0/preview.jpg'
                },
                'overview': {
                    'title': 'True color image',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'overview'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        },
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        },
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/L2A_PVI.tif',
                    'proj:shape': [
                        343,
                        343
                    ],
                    'proj:transform': [
                        320,
                        0,
                        199980,
                        0,
                        -320,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'info': {
                    'title': 'Original JSON metadata',
                    'type': 'application/json',
                    'roles': [
                        'metadata'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TH/2021/9/12/0/tileInfo.json'
                },
                'metadata': {
                    'title': 'Original XML metadata',
                    'type': 'application/xml',
                    'roles': [
                        'metadata'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TH/2021/9/12/0/metadata.xml'
                },
                'visual': {
                    'title': 'True color image',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'overview'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        },
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        },
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/TCI.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B01': {
                    'title': 'Band 1 (coastal)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 60,
                    'eo:bands': [
                        {
                            'name': 'B01',
                            'common_name': 'coastal',
                            'center_wavelength': 0.4439,
                            'full_width_half_max': 0.027
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B01.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        199980,
                        0,
                        -60,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B02': {
                    'title': 'Band 2 (blue)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B02.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B03': {
                    'title': 'Band 3 (green)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B03.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B04': {
                    'title': 'Band 4 (red)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B04.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B05': {
                    'title': 'Band 5',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B05',
                            'center_wavelength': 0.7039,
                            'full_width_half_max': 0.019
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B05.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B06': {
                    'title': 'Band 6',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B06',
                            'center_wavelength': 0.7402,
                            'full_width_half_max': 0.018
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B06.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B07': {
                    'title': 'Band 7',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B07',
                            'center_wavelength': 0.7825,
                            'full_width_half_max': 0.028
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B07.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B08': {
                    'title': 'Band 8 (nir)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B08',
                            'common_name': 'nir',
                            'center_wavelength': 0.8351,
                            'full_width_half_max': 0.145
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B08.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B8A': {
                    'title': 'Band 8A',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B8A',
                            'center_wavelength': 0.8648,
                            'full_width_half_max': 0.033
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B8A.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B09': {
                    'title': 'Band 9',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 60,
                    'eo:bands': [
                        {
                            'name': 'B09',
                            'center_wavelength': 0.945,
                            'full_width_half_max': 0.026
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B09.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        199980,
                        0,
                        -60,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B11': {
                    'title': 'Band 11 (swir16)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B11',
                            'common_name': 'swir16',
                            'center_wavelength': 1.6137,
                            'full_width_half_max': 0.143
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B11.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B12': {
                    'title': 'Band 12 (swir22)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B12',
                            'common_name': 'swir22',
                            'center_wavelength': 2.22024,
                            'full_width_half_max': 0.242
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/B12.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'AOT': {
                    'title': 'Aerosol Optical Thickness (AOT)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/AOT.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        199980,
                        0,
                        -60,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'WVP': {
                    'title': 'Water Vapour (WVP)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/WVP.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        199980,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'SCL': {
                    'title': 'Scene Classification Map (SCL)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/SCL.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        199980,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                }
            },
            'links': [
                {
                    'rel': 'self',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_18STH_20210912_0_L2A'
                },
                {
                    'rel': 'canonical',
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/S2A_18STH_20210912_0_L2A.json',
                    'type': 'application/json'
                },
                {
                    'title': 'sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TH-2021-9-12-0',
                    'rel': 'via-cirrus',
                    'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TH-2021-9-12-0'
                },
                {
                    'title': 'Source STAC Item',
                    'rel': 'derived_from',
                    'href': 'https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/18/S/TH/2021/9/S2A_18STH_20210912_0_L2A/S2A_18STH_20210912_0_L2A.json',
                    'type': 'application/json'
                },
                {
                    'title': 'sentinel-s2-l2a/workflow-cog-archive/S2A_18STH_20210912_0_L2A',
                    'rel': 'via-cirrus',
                    'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_18STH_20210912_0_L2A'
                },
                {
                    'rel': 'parent',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
                },
                {
                    'rel': 'collection',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
                },
                {
                    'rel': 'root',
                    'href': 'https://earth-search.aws.element84.com/v0/'
                }
            ]
        },
        {
            'type': 'Feature',
            'stac_version': '1.0.0-beta.2',
            'stac_extensions': [
                'eo',
                'view',
                'proj'
            ],
            'id': 'S2A_18SUH_20210912_0_L2A',
            'bbox': [
                -77.30391904144093,
                37.83751264090908,
                -76.02534804963985,
                38.84436482287841
            ],
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [
                            -77.27280734820702,
                            37.83751264090908
                        ],
                        [
                            -77.30391904144093,
                            38.826263846784215
                        ],
                        [
                            -76.03939567037992,
                            38.84436482287841
                        ],
                        [
                            -76.02534804963985,
                            37.85498657505244
                        ],
                        [
                            -77.27280734820702,
                            37.83751264090908
                        ]
                    ]
                ]
            },
            'properties': {
                'datetime': '2021-09-12T16:02:39Z',
                'platform': 'sentinel-2a',
                'constellation': 'sentinel-2',
                'instruments': [
                    'msi'
                ],
                'gsd': 10,
                'view:off_nadir': 0,
                'proj:epsg': 32618,
                'sentinel:utm_zone': 18,
                'sentinel:latitude_band': 'S',
                'sentinel:grid_square': 'UH',
                'sentinel:sequence': '0',
                'sentinel:product_id': 'S2A_MSIL2A_20210912T154911_N0301_R054_T18SUH_20210912T201501',
                'sentinel:data_coverage': 100,
                'eo:cloud_cover': 0,
                'sentinel:valid_cloud_cover': True,
                'created': '2021-09-12T22:29:49.610Z',
                'updated': '2021-09-12T22:29:49.610Z'
            },
            'collection': 'sentinel-s2-l2a-cogs',
            'assets': {
                'thumbnail': {
                    'title': 'Thumbnail',
                    'type': 'image/png',
                    'roles': [
                        'thumbnail'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/18/S/UH/2021/9/12/0/preview.jpg'
                },
                'overview': {
                    'title': 'True color image',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'overview'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        },
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        },
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/L2A_PVI.tif',
                    'proj:shape': [
                        343,
                        343
                    ],
                    'proj:transform': [
                        320,
                        0,
                        300000,
                        0,
                        -320,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'info': {
                    'title': 'Original JSON metadata',
                    'type': 'application/json',
                    'roles': [
                        'metadata'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/UH/2021/9/12/0/tileInfo.json'
                },
                'metadata': {
                    'title': 'Original XML metadata',
                    'type': 'application/xml',
                    'roles': [
                        'metadata'
                    ],
                    'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/UH/2021/9/12/0/metadata.xml'
                },
                'visual': {
                    'title': 'True color image',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'overview'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        },
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        },
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/TCI.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        300000,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B01': {
                    'title': 'Band 1 (coastal)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 60,
                    'eo:bands': [
                        {
                            'name': 'B01',
                            'common_name': 'coastal',
                            'center_wavelength': 0.4439,
                            'full_width_half_max': 0.027
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B01.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        300000,
                        0,
                        -60,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B02': {
                    'title': 'Band 2 (blue)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B02',
                            'common_name': 'blue',
                            'center_wavelength': 0.4966,
                            'full_width_half_max': 0.098
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B02.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        300000,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B03': {
                    'title': 'Band 3 (green)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B03',
                            'common_name': 'green',
                            'center_wavelength': 0.56,
                            'full_width_half_max': 0.045
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B03.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        300000,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B04': {
                    'title': 'Band 4 (red)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B04',
                            'common_name': 'red',
                            'center_wavelength': 0.6645,
                            'full_width_half_max': 0.038
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B04.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        300000,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B05': {
                    'title': 'Band 5',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B05',
                            'center_wavelength': 0.7039,
                            'full_width_half_max': 0.019
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B05.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B06': {
                    'title': 'Band 6',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B06',
                            'center_wavelength': 0.7402,
                            'full_width_half_max': 0.018
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B06.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B07': {
                    'title': 'Band 7',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B07',
                            'center_wavelength': 0.7825,
                            'full_width_half_max': 0.028
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B07.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B08': {
                    'title': 'Band 8 (nir)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 10,
                    'eo:bands': [
                        {
                            'name': 'B08',
                            'common_name': 'nir',
                            'center_wavelength': 0.8351,
                            'full_width_half_max': 0.145
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B08.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        300000,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B8A': {
                    'title': 'Band 8A',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B8A',
                            'center_wavelength': 0.8648,
                            'full_width_half_max': 0.033
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B8A.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B09': {
                    'title': 'Band 9',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 60,
                    'eo:bands': [
                        {
                            'name': 'B09',
                            'center_wavelength': 0.945,
                            'full_width_half_max': 0.026
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B09.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        300000,
                        0,
                        -60,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B11': {
                    'title': 'Band 11 (swir16)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B11',
                            'common_name': 'swir16',
                            'center_wavelength': 1.6137,
                            'full_width_half_max': 0.143
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B11.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'B12': {
                    'title': 'Band 12 (swir22)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'gsd': 20,
                    'eo:bands': [
                        {
                            'name': 'B12',
                            'common_name': 'swir22',
                            'center_wavelength': 2.22024,
                            'full_width_half_max': 0.242
                        }
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/B12.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'AOT': {
                    'title': 'Aerosol Optical Thickness (AOT)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/AOT.tif',
                    'proj:shape': [
                        1830,
                        1830
                    ],
                    'proj:transform': [
                        60,
                        0,
                        300000,
                        0,
                        -60,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'WVP': {
                    'title': 'Water Vapour (WVP)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/WVP.tif',
                    'proj:shape': [
                        10980,
                        10980
                    ],
                    'proj:transform': [
                        10,
                        0,
                        300000,
                        0,
                        -10,
                        4300020,
                        0,
                        0,
                        1
                    ]
                },
                'SCL': {
                    'title': 'Scene Classification Map (SCL)',
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                    'roles': [
                        'data'
                    ],
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/SCL.tif',
                    'proj:shape': [
                        5490,
                        5490
                    ],
                    'proj:transform': [
                        20,
                        0,
                        300000,
                        0,
                        -20,
                        4300020,
                        0,
                        0,
                        1
                    ]
                }
            },
            'links': [
                {
                    'rel': 'self',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_18SUH_20210912_0_L2A'
                },
                {
                    'rel': 'canonical',
                    'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/S2A_18SUH_20210912_0_L2A.json',
                    'type': 'application/json'
                },
                {
                    'title': 'sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-UH-2021-9-12-0',
                    'rel': 'via-cirrus',
                    'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-UH-2021-9-12-0'
                },
                {
                    'title': 'Source STAC Item',
                    'rel': 'derived_from',
                    'href': 'https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/18/S/UH/2021/9/S2A_18SUH_20210912_0_L2A/S2A_18SUH_20210912_0_L2A.json',
                    'type': 'application/json'
                },
                {
                    'title': 'sentinel-s2-l2a/workflow-cog-archive/S2A_18SUH_20210912_0_L2A',
                    'rel': 'via-cirrus',
                    'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_18SUH_20210912_0_L2A'
                },
                {
                    'rel': 'parent',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
                },
                {
                    'rel': 'collection',
                    'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
                },
                {
                    'rel': 'root',
                    'href': 'https://earth-search.aws.element84.com/v0/'
                }
            ]
        }
    ],
    'links': [
        {
            'rel': 'next',
            'title': 'Next page of results',
            'method': 'POST',
            'href': 'https://earth-search.aws.element84.com/v0/search',
            'merge': False,
            'body': {
                'intersects': {
                    'type': 'Polygon',
                    'coordinates': [
                        [
                            [
                                -77.13902381708914,
                                38.26355335375666
                            ],
                            [
                                -77.28718772718392,
                                38.30058309174283
                            ],
                            [
                                -77.30391904144093,
                                38.826263846784215
                            ],
                            [
                                -76.94352518307373,
                                38.83281841414546
                            ],
                            [
                                -77.13902381708914,
                                38.26355335375666
                            ]
                        ]
                    ]
                },
                'query': {
                    'eo:cloud_cover': {
                        'lt': 20
                    },
                    'platform': {
                        'eq': 'sentinel-2a'
                    }
                },
                'collections': [
                    'sentinel-s2-l2a-cogs'
                ],
                'page': 2,
                'limit': 3
            }
        }
    ]
}

feature_data = {
    'type': 'Feature',
    'stac_version': '1.0.0-beta.2',
    'stac_extensions': [
        'eo',
        'view',
        'proj'
    ],
    'id': 'S2A_18STJ_20211002_0_L2A',
    'bbox': [
        -77.95337796105937,
        38.72355003898747,
        -77.1886636996379,
        39.575037252516026
    ],
    'geometry': {
        'type': 'Polygon',
        'coordinates': [
            [
                [
                    -77.95337796105937,
                    38.72355003898747
                ],
                [
                    -77.7020628230002,
                    39.575037252516026
                ],
                [
                    -77.3795834273484,
                    39.528820064497175
                ],
                [
                    -77.21244463164855,
                    39.504374168834815
                ],
                [
                    -77.1886636996379,
                    38.74037874635374
                ],
                [
                    -77.95337796105937,
                    38.72355003898747
                ]
            ]
        ]
    },
    'properties': {
        'datetime': '2021-10-02T16:02:33Z',
        'platform': 'sentinel-2a',
        'constellation': 'sentinel-2',
        'instruments': [
            'msi'
        ],
        'gsd': 10,
        'view:off_nadir': 0,
        'proj:epsg': 32618,
        'sentinel:utm_zone': 18,
        'sentinel:latitude_band': 'S',
        'sentinel:grid_square': 'TJ',
        'sentinel:sequence': '0',
        'sentinel:product_id': 'S2A_MSIL2A_20211002T155101_N0301_R054_T18STJ_20211002T201235',
        'sentinel:data_coverage': 40.6,
        'eo:cloud_cover': 3.89,
        'sentinel:valid_cloud_cover': True,
        'created': '2021-10-02T22:07:56.585Z',
        'updated': '2021-10-02T22:07:56.585Z'
    },
    'collection': 'sentinel-s2-l2a-cogs',
    'assets': {
        'thumbnail': {
            'title': 'Thumbnail',
            'type': 'image/png',
            'roles': [
                'thumbnail'
            ],
            'href': 'https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/18/S/TJ/2021/10/2/0/preview.jpg'
        },
        'overview': {
            'title': 'True color image',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'overview'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B04',
                    'common_name': 'red',
                    'center_wavelength': 0.6645,
                    'full_width_half_max': 0.038
                },
                {
                    'name': 'B03',
                    'common_name': 'green',
                    'center_wavelength': 0.56,
                    'full_width_half_max': 0.045
                },
                {
                    'name': 'B02',
                    'common_name': 'blue',
                    'center_wavelength': 0.4966,
                    'full_width_half_max': 0.098
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/L2A_PVI.tif',
            'proj:shape': [
                343,
                343
            ],
            'proj:transform': [
                320,
                0,
                199980,
                0,
                -320,
                4400040,
                0,
                0,
                1
            ]
        },
        'info': {
            'title': 'Original JSON metadata',
            'type': 'application/json',
            'roles': [
                'metadata'
            ],
            'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TJ/2021/10/2/0/tileInfo.json'
        },
        'metadata': {
            'title': 'Original XML metadata',
            'type': 'application/xml',
            'roles': [
                'metadata'
            ],
            'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TJ/2021/10/2/0/metadata.xml'
        },
        'visual': {
            'title': 'True color image',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'overview'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B04',
                    'common_name': 'red',
                    'center_wavelength': 0.6645,
                    'full_width_half_max': 0.038
                },
                {
                    'name': 'B03',
                    'common_name': 'green',
                    'center_wavelength': 0.56,
                    'full_width_half_max': 0.045
                },
                {
                    'name': 'B02',
                    'common_name': 'blue',
                    'center_wavelength': 0.4966,
                    'full_width_half_max': 0.098
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/TCI.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B01': {
            'title': 'Band 1 (coastal)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 60,
            'eo:bands': [
                {
                    'name': 'B01',
                    'common_name': 'coastal',
                    'center_wavelength': 0.4439,
                    'full_width_half_max': 0.027
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B01.tif',
            'proj:shape': [
                1830,
                1830
            ],
            'proj:transform': [
                60,
                0,
                199980,
                0,
                -60,
                4400040,
                0,
                0,
                1
            ]
        },
        'B02': {
            'title': 'Band 2 (blue)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B02',
                    'common_name': 'blue',
                    'center_wavelength': 0.4966,
                    'full_width_half_max': 0.098
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B02.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B03': {
            'title': 'Band 3 (green)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B03',
                    'common_name': 'green',
                    'center_wavelength': 0.56,
                    'full_width_half_max': 0.045
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B03.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B04': {
            'title': 'Band 4 (red)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B04',
                    'common_name': 'red',
                    'center_wavelength': 0.6645,
                    'full_width_half_max': 0.038
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B04.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B05': {
            'title': 'Band 5',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B05',
                    'center_wavelength': 0.7039,
                    'full_width_half_max': 0.019
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B05.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B06': {
            'title': 'Band 6',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B06',
                    'center_wavelength': 0.7402,
                    'full_width_half_max': 0.018
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B06.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B07': {
            'title': 'Band 7',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B07',
                    'center_wavelength': 0.7825,
                    'full_width_half_max': 0.028
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B07.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B08': {
            'title': 'Band 8 (nir)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B08',
                    'common_name': 'nir',
                    'center_wavelength': 0.8351,
                    'full_width_half_max': 0.145
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B08.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B8A': {
            'title': 'Band 8A',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B8A',
                    'center_wavelength': 0.8648,
                    'full_width_half_max': 0.033
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B8A.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B09': {
            'title': 'Band 9',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 60,
            'eo:bands': [
                {
                    'name': 'B09',
                    'center_wavelength': 0.945,
                    'full_width_half_max': 0.026
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B09.tif',
            'proj:shape': [
                1830,
                1830
            ],
            'proj:transform': [
                60,
                0,
                199980,
                0,
                -60,
                4400040,
                0,
                0,
                1
            ]
        },
        'B11': {
            'title': 'Band 11 (swir16)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B11',
                    'common_name': 'swir16',
                    'center_wavelength': 1.6137,
                    'full_width_half_max': 0.143
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B11.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B12': {
            'title': 'Band 12 (swir22)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B12',
                    'common_name': 'swir22',
                    'center_wavelength': 2.22024,
                    'full_width_half_max': 0.242
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B12.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'AOT': {
            'title': 'Aerosol Optical Thickness (AOT)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/AOT.tif',
            'proj:shape': [
                1830,
                1830
            ],
            'proj:transform': [
                60,
                0,
                199980,
                0,
                -60,
                4400040,
                0,
                0,
                1
            ]
        },
        'WVP': {
            'title': 'Water Vapour (WVP)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/WVP.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'SCL': {
            'title': 'Scene Classification Map (SCL)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/SCL.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        }
    },
    'links': [
        {
            'rel': 'self',
            'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_18STJ_20211002_0_L2A'
        },
        {
            'rel': 'canonical',
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/S2A_18STJ_20211002_0_L2A.json',
            'type': 'application/json'
        },
        {
            'title': 'sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TJ-2021-10-2-0',
            'rel': 'via-cirrus',
            'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TJ-2021-10-2-0'
        },
        {
            'title': 'Source STAC Item',
            'rel': 'derived_from',
            'href': 'https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/S2A_18STJ_20211002_0_L2A.json',
            'type': 'application/json'
        },
        {
            'title': 'sentinel-s2-l2a/workflow-cog-archive/S2A_18STJ_20211002_0_L2A',
            'rel': 'via-cirrus',
            'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_18STJ_20211002_0_L2A'
        },
        {
            'rel': 'parent',
            'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
        },
        {
            'rel': 'collection',
            'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
        },
        {
            'rel': 'root',
            'href': 'https://earth-search.aws.element84.com/v0/'
        }
    ]
}

update_feature_data = {
    'type': 'Feature',
    'stac_version': '1.0.0-beta.2',
    'stac_extensions': [
        'eo',
        'view',
        'proj'
    ],
    'id': 'S2A_18STJ_20211002_0_L2A',
    'bbox': [
        -77.95337796105937,
        38.72355003898747,
        -77.1886636996379,
        39.575037252516026
    ],
    'geometry': {
        'type': 'Polygon',
        'coordinates': [
            [
                [
                    -77.95337796105937,
                    38.72355003898747
                ],
                [
                    -77.7020628230002,
                    39.575037252516026
                ],
                [
                    -77.3795834273484,
                    39.528820064497175
                ],
                [
                    -77.21244463164855,
                    39.504374168834815
                ],
                [
                    -77.1886636996379,
                    38.74037874635374
                ],
                [
                    -77.95337796105937,
                    38.72355003898747
                ]
            ]
        ]
    },
    'properties': {
        'datetime': '2021-10-02T16:02:33Z',
        'platform': 'sentinel-2a',
        'constellation': 'sentinel-2',
        'instruments': [
            'msi'
        ],
        'gsd': 10,
        'view:off_nadir': 0,
        'proj:epsg': 32618,
        'sentinel:utm_zone': 18,
        'sentinel:latitude_band': 'S',
        'sentinel:grid_square': 'TJ',
        'sentinel:sequence': '0',
        'sentinel:product_id': 'S2A_MSIL2A_20211002T155101_N0301_R054_T18STJ_20211002T201235',
        'sentinel:data_coverage': 40.6,
        'eo:cloud_cover': 3.89,
        'sentinel:valid_cloud_cover': True,
        'created': '2021-10-02T22:07:56.585Z',
        'updated': '2021-10-02T22:07:56.585Z'
    },
    'collection': 'sentinel-s2-l2a-cogs',
    'assets': {
        'thumbnail': {
            'title': 'Thumbnail',
            'type': 'image/png',
            'roles': [
                'thumbnail'
            ],
            'href': 'https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/18/S/TJ/2021/10/2/0/preview.jpg'
        },
        'overview': {
            'title': 'True color image',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'overview'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B04',
                    'common_name': 'red',
                    'center_wavelength': 0.6645,
                    'full_width_half_max': 0.038
                },
                {
                    'name': 'B03',
                    'common_name': 'green',
                    'center_wavelength': 0.56,
                    'full_width_half_max': 0.045
                },
                {
                    'name': 'B02',
                    'common_name': 'blue',
                    'center_wavelength': 0.4966,
                    'full_width_half_max': 0.098
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/L2A_PVI.tif',
            'proj:shape': [
                343,
                343
            ],
            'proj:transform': [
                320,
                0,
                199980,
                0,
                -320,
                4400040,
                0,
                0,
                1
            ]
        },
        'info': {
            'title': 'Original JSON metadata',
            'type': 'application/json',
            'roles': [
                'metadata'
            ],
            'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TJ/2021/10/2/0/tileInfo.json'
        },
        'metadata': {
            'title': 'Original XML metadata',
            'type': 'application/xml',
            'roles': [
                'metadata'
            ],
            'href': 'https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/18/S/TJ/2021/10/2/0/metadata.xml'
        },
        'visual': {
            'title': 'True color image',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'overview'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B04',
                    'common_name': 'red',
                    'center_wavelength': 0.6645,
                    'full_width_half_max': 0.038
                },
                {
                    'name': 'B03',
                    'common_name': 'green',
                    'center_wavelength': 0.56,
                    'full_width_half_max': 0.045
                },
                {
                    'name': 'B02',
                    'common_name': 'blue',
                    'center_wavelength': 0.4966,
                    'full_width_half_max': 0.098
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/TCI.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B01': {
            'title': 'Band 1 (coastal)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 60,
            'eo:bands': [
                {
                    'name': 'B01',
                    'common_name': 'coastal',
                    'center_wavelength': 0.4439,
                    'full_width_half_max': 0.027
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B01.tif',
            'proj:shape': [
                1830,
                1830
            ],
            'proj:transform': [
                60,
                0,
                199980,
                0,
                -60,
                4400040,
                0,
                0,
                1
            ]
        },
        'B02': {
            'title': 'Band 2 (blue)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B02',
                    'common_name': 'blue',
                    'center_wavelength': 0.4966,
                    'full_width_half_max': 0.098
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B02.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B03': {
            'title': 'Band 3 (green)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B03',
                    'common_name': 'green',
                    'center_wavelength': 0.56,
                    'full_width_half_max': 0.045
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B03.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B04': {
            'title': 'Band 4 (red)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 10,
            'eo:bands': [
                {
                    'name': 'B04',
                    'common_name': 'red',
                    'center_wavelength': 0.6645,
                    'full_width_half_max': 0.038
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B04.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'B05': {
            'title': 'Band 5',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B05',
                    'center_wavelength': 0.7039,
                    'full_width_half_max': 0.019
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B05.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B06': {
            'title': 'Band 6',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B06',
                    'center_wavelength': 0.7402,
                    'full_width_half_max': 0.018
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B06.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'B07': {
            'title': 'Band 7',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'gsd': 20,
            'eo:bands': [
                {
                    'name': 'B07',
                    'center_wavelength': 0.7825,
                    'full_width_half_max': 0.028
                }
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/B07.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        },
        'AOT': {
            'title': 'Aerosol Optical Thickness (AOT)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/AOT.tif',
            'proj:shape': [
                1830,
                1830
            ],
            'proj:transform': [
                60,
                0,
                199980,
                0,
                -60,
                4400040,
                0,
                0,
                1
            ]
        },
        'WVP': {
            'title': 'Water Vapour (WVP)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/WVP.tif',
            'proj:shape': [
                10980,
                10980
            ],
            'proj:transform': [
                10,
                0,
                199980,
                0,
                -10,
                4400040,
                0,
                0,
                1
            ]
        },
        'SCL': {
            'title': 'Scene Classification Map (SCL)',
            'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
            'roles': [
                'data'
            ],
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/SCL.tif',
            'proj:shape': [
                5490,
                5490
            ],
            'proj:transform': [
                20,
                0,
                199980,
                0,
                -20,
                4400040,
                0,
                0,
                1
            ]
        }
    },
    'links': [
        {
            'rel': 'self',
            'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_18STJ_20211002_0_L2A'
        },
        {
            'rel': 'canonical',
            'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/S2A_18STJ_20211002_0_L2A.json',
            'type': 'application/json'
        },
        {
            'title': 'sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TJ-2021-10-2-0',
            'rel': 'via-cirrus',
            'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-18-S-TJ-2021-10-2-0'
        },
        {
            'title': 'Source STAC Item',
            'rel': 'derived_from',
            'href': 'https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/18/S/TJ/2021/10/S2A_18STJ_20211002_0_L2A/S2A_18STJ_20211002_0_L2A.json',
            'type': 'application/json'
        },
        {
            'title': 'sentinel-s2-l2a/workflow-cog-archive/S2A_18STJ_20211002_0_L2A',
            'rel': 'via-cirrus',
            'href': 'https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_18STJ_20211002_0_L2A'
        },
        {
            'rel': 'parent',
            'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
        },
        {
            'rel': 'collection',
            'href': 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
        },
        {
            'rel': 'root',
            'href': 'https://earth-search.aws.element84.com/v0/'
        }
    ]
}
