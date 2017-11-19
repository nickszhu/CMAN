import pandas as pd 
import numpy as np
import folium
from folium import plugins
import datetime
from datetime import datetime
from dateutil.parser import parse
from folium.plugins import HeatMap
import math


def parse_float(x):
	try:
		x = float(x)
	except Exception:
		x = 0
	return x


data = pd.read_csv("201410-citibike-tripdata.csv", low_memory=False)
df = pd.DataFrame(data)
data2 = pd.read_csv("2014-04 - Citi Bike trip data.csv",low_memory = False)
df2 = pd.DataFrame(data2)

position = []
NY_map = folium.Map(location=[40.657, -73.947], zoom_start=11)
marker_cluster = plugins.MarkerCluster().add_to(NY_map)
df = df.head(1000)
df2 = df2.head(1000)
for index, row in df.iterrows():
	lon = parse_float(row["start station latitude"])
	lat = parse_float(row["start station longitude"])
	if not math.isnan(lon) and not math.isnan(lat):
		folium.Marker([lon, lat], popup='NYC Map',icon=folium.Icon(color='red')).add_to(marker_cluster)
		position.append([lat, lon])
plugins.MarkerCluster(position).add_to(NY_map)

for index,row in df2.iterrows():
	lon = parse_float(row["start station latitude"])
	lat = parse_float(row["start station longitude"])
	if not math.isnan(lon) and not math.isnan(lat):
		folium.Marker([lon, lat], popup='NYC Map',icon=folium.Icon(color='black')).add_to(marker_cluster)
		position.append([lat, lon])
plugins.MarkerCluster(position).add_to(NY_map)	


NY_map.save('start.html')

position2 = []

mymap = folium.Map(location=[40.657, -73.947], zoom_start=11)
marker_cluster2 = plugins.MarkerCluster().add_to(mymap)
for index, row in df.iterrows():
	lon = parse_float(row["end station latitude"])
	lat = parse_float(row["end station longitude"])
	if not math.isnan(lon) and not math.isnan(lat):
		folium.Marker([lon, lat], popup='NYC Map').add_to(marker_cluster2)
		position2.append([lat, lon])
plugins.MarkerCluster(position2).add_to(mymap)

for index,row in df2.iterrows():
	lon = parse_float(row["end station latitude"])
	lat = parse_float(row["end station longitude"])
	if not math.isnan(lon) and not math.isnan(lat):
		folium.Marker([lon, lat], popup='NYC Map',icon=folium.Icon(color='black')).add_to(marker_cluster)
		position.append([lat, lon])
plugins.MarkerCluster(position).add_to(mymap)	






mymap.save('end.html')