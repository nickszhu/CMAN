import pandas as pd 
import numpy as np
import folium
from folium import plugins
import datetime
from datetime import datetime
from dateutil.parser import parse
import math
position = []


def parse_float(x):
	try:
		x = float(x)
	except Exception:
		x = 0
	return x

data = pd.read_csv("uber-raw-data-apr14.csv", low_memory=False)
df = pd.DataFrame(data)
df['Date'], df['Time'] = df['Date/Time'].str.split(' ', 1).str
attack_dates = df['Date']
dates = [datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
df['Date']=dates
data15 = df[(df['Date'] == '2014-04-01')]#&(df['Date'] <= '2014-12-31')]
data15 = data15.head(1000)
#print data15
mymap = folium.Map( location=[ data15.Lat.mean(), data15.Lon.mean() ], zoom_start=14)


for index, row in data15.iterrows():
	lon = parse_float(row["Lon"])
	lat = parse_float(row["Lat"])
	if not math.isnan(lon) and not math.isnan(lat):
		position.append([lat, lon])
#for each in position:  
plugins.MarkerCluster(position).add_to(mymap)
  
    #folium.CircleMarker(position, radius=1,color='red').add_to(mymap)

#for coord in position.values:
	
#mymap   # shows map inline in Jupyter but takes up full width
#folium.PolyLine(position, color="red", weight=2.5, opacity=1).add_to(mymap)

mymap.save('fol.html')  # saves to html file for display below