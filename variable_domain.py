#getting values of a variable from a netCDF4 file for a special domain with definit latitudes and longitudes and showing them in csv format

import netCDF4
import numpy as np
import pandas as pd
from netCDF4 import Dataset
import xarray as xr

ds = xr.open_dataset('/home/lida/Desktop/pm.nc4')
print(ds)   # an explanation about dataset and dimensions of existed variables

f = Dataset ('/home/lida/Desktop/pm.nc4')

#DUSMASS is the name of a variable in pm.nc4
dusmass = f.variables['DUSMASS']

def domain_bounderies(lat1, lat2, lon1, lon2):
    latitudes = f.variables ['lat']
    lat_b = latitudes[:]>=lat1
    lat_s = latitudes[:]<=lat2
    lat = [a and b for a, b in zip(lat_b, lat_s)]

    longitudes = f.variables ['lon']
    lon_b = longitudes[:]>=lon1
    lon_s = longitudes[:]<=lon2
    lon = [a and b for a, b in zip(lon_b, lon_s)]

    latitudes_grid, longitudes_grid = [x.flatten() for x in np.meshgrid(latitudes[lat], longitudes[lon], indexing='ij')]
#in this example (pm.nc4), there is just a time. So, there is no need to write time in np.meshgrid
    df = pd.DataFrame({'latitude': latitudes_grid,'longitude': longitudes_grid,'dusmass': dusmass[:,lat,lon].flatten()})

    df.to_csv('/home/lida/Desktop/table.csv', index=False)  
    print('Done')
    return df.to_csv
latlon_value = domain_bounderies(27.8,34,50,53.65)
