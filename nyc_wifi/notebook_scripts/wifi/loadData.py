import sys
import os
import django

sys.path.append('/home/yohoos/Desktop/git/RiceMilk')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RiceMilk.settings')
django.setup()

import json
import pandas as pd

from cartopy import crs as ccrs
from nyc_wifi.models import WifiSpot


def convert_to_model(row):
    record = WifiSpot()
    record.borough = row.Borough
    record.type = row.Type
    record.provider = row.Provider
    record.name = row.Name
    record.location = row.Location
    record.latitude = row.Latitude
    record.longitude = row.Longitude
    record.location_type = row.Location_Type
    record.remarks = row.Remarks
    record.city = row.City
    record.ssid = row.SSID
    record.lat = row.lat
    record.lon = row.lon

    return record


if __name__ == '__main__':
    f = open('nyc_wifi/notebook_scripts/datasets/nyc-wifi.json')
    nyc = json.load(f)
    f.close()

    columns_type = list(
        map(lambda x: (x['name'], x['dataTypeName']), nyc['meta']['view']['columns']))

    def convert_type(orig_type):
        if orig_type == 'number':
            return 'float'
        else:
            return 'object'

    columns = list(map(lambda x: x[0], columns_type))
    df = pd.DataFrame(nyc['data'])
    df.columns = columns

    select_columns = ['Borough', 'Type', 'Provider', 'Name', 'Location', 'Latitude', 'Longitude',
                      'Location_T', 'Remarks', 'City', 'SSID']
    df = df.loc[:, select_columns]
    df.rename(columns={'Location_T': 'Location_Type'}, inplace=True)

    numeric_cols = ['Latitude', 'Longitude']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

    lat = df['Latitude'].as_matrix()
    lon = df['Longitude'].as_matrix()
    coords = ccrs.GOOGLE_MERCATOR.transform_points(
        ccrs.PlateCarree(), lon, lat)
    df['lon'] = coords[:, 0]
    df['lat'] = coords[:, 1]

    df.fillna('', inplace=True)

    models = map(convert_to_model, df.itertuples(False))
    models = list(models)

    WifiSpot.objects.all().delete()
    WifiSpot.objects.bulk_create(models, 10000)
