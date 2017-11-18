import pandas as pd 
import numpy as np
import folium
from folium import plugins
import datetime
from datetime import datetime
from dateutil.parser import parse


def parse_float(x):
	try:
		x = float(x)
	except Exception:
		x = 0
	return x


data = pd.read_csv("Transportation/NYCGeneralTransport/NYC-vehicle-collisions.csv", low_memory=False)
df = pd.DataFrame(data)



region = data['BOROUGH'].unique()

df['LATITUDE'] = df['LATITUDE'].apply(parse_float)
df['LONGITUDE'] = df['LONGITUDE'].apply(parse_float)

attack_dates = df['DATE']
dates = [datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
df['DATE']=dates

data15 = df[(df['DATE'] >= '2015-01-01')&(df['DATE'] <= '2015-12-31')]
data16 = data[(data['DATE'] >= '2016-01-01')&(data['DATE'] <= '2016-12-31')]
data17 = data[(data['DATE'] >= '2017-01-01')&(data['DATE'] <= '2017-12-31')]
print("{0}".format(region))
print(data['BOROUGH'].value_counts())
print(df.groupby(['DATE', 'BOROUGH']).size())
print("Accidents in 2015\n{0}".format(data15['BOROUGH'].value_counts()))
print("Accidents in 2016\n{0}".format(data16['BOROUGH'].value_counts()))
print("Accidents in 2017\n{0}".format(data17['BOROUGH'].value_counts()))



#morning_rush = last_year[(last_year["date"].dt.weekday < 5) & 
#			   (last_year["date"].dt.hour > 5) & (last_year["date"].dt.hour < 10)]
#print(morning_rush.shape)
#last_year.shape
import math

position = []
NY_map = folium.Map(location=[40.657, -73.947], zoom_start=11, tiles='https://api.mapbox.com/styles/v1/nickszhu/cja4ybeod31lc2roeya5ijuxb/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoibmlja3N6aHUiLCJhIjoiY2phNHdhd3hvMWNxNjMybGZjdTZvd2g1MCJ9.Oqaq80B5Gnr5amdoZOGYSg', attr='nick')
#marker_cluster = plugins.MarkerCluster().add_to(NY_map)
for index, row in data15.iterrows():
	lon = parse_float(row["LONGITUDE"])
	lat = parse_float(row["LATITUDE"])
	if not math.isnan(lon) and not math.isnan(lat):
		#folium.Marker([lon, lat], popup='NYC Map').add_to(marker_cluster)
		position.append([lat, lon])

plugins.MarkerCluster(position).add_to(NY_map)
NY_map.save('map.html')
NY_map






















