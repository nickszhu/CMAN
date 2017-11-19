import pandas as pd 
import numpy as np
import folium
from folium import plugins
import datetime
from datetime import datetime
from dateutil.parser import parse
from folium.plugins import HeatMap
import matplotlib
import matplotlib.pyplot as plt




data = pd.read_csv("20141-3.csv", low_memory=False)
d2 = pd.read_csv("201404-06 Daily Ridership and Membership.csv",low_memory=False)
d3 = pd.read_csv("201407-09 Daily Ridership and Membership.csv",low_memory=False)
d4 = pd.read_csv("201410-12 Daily Ridership and Membership.csv",low_memory=False)

df = pd.DataFrame(data)
df2 = pd.DataFrame(d2)
df3 = pd.DataFrame(d3)
df4 = pd.DataFrame(d4)

attack_dates = df['Date']
dates = [datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
df['Date']=dates

attack_dates = df2['Date']
dates = [datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
df2['Date']=dates

attack_dates = df3['Date']
dates = [datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
df3['Date']=dates

attack_dates = df4['Date']
dates = [datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
df4['Date']=dates


dMin = df[df['Annual Member Sign-Ups (midnight to 11:59 pm)']<=10]

dMax= df[df['Annual Member Sign-Ups (midnight to 11:59 pm)']>=100]

data1 = df[(df['Date'] >= '2014-01-01')& (df['Date'] <= '2014-01-31')]
data2 = df[(df['Date'] >= '2014-02-01')&(df['Date'] <= '2014-02-28')]
data3 = df[(df['Date'] >= '2014-03-01')&(df['Date'] <= '2014-03-31')]
data4 = df2[(df2['Date'] >= '2014-04-01')&(df2['Date'] <= '2014-04-30')]
data5 = df2[(df2['Date'] >= '2014-05-01')&(df2['Date'] <= '2014-05-31')]
data6 = df2[(df2['Date'] >= '2014-06-01')&(df2['Date'] <= '2014-06-30')]
data7 = df3[(df3['Date'] >= '2014-07-01')&(df3['Date'] <= '2014-07-31')]

data8 = df3[(df3['Date'] >= '2014-08-01')&(df3['Date'] <= '2014-08-31')]
data9 = df3[(df3['Date'] >= '2014-09-01')&(df3['Date'] <= '2014-09-30')]

data10 = df4[(df4['Date'] >= '2014-10-01')&(df4['Date'] <= '2014-10-31')]
data11= df4[(df4['Date'] >= '2014-11-01')&(df4['Date'] <= '2014-11-30')]

data12= df4[(df4['Date'] >= '2014-12-01')&(df4['Date'] <= '2014-12-31')]


 
sum1 = data1['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum2 = data2['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum3 = data3['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum4 = data4['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum5 = data5['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum6 = data6['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum7 = data7['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum8 = data8['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum9 = data9['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum10 = data10['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum11 = data11['Trips over the past 24-hours (midnight to 11:59pm)'].sum()
sum12 = data12['Trips over the past 24-hours (midnight to 11:59pm)'].sum()


print "1-3: "
print sum1, sum2 , sum3

print "4-6: "
print sum4,sum5,sum6
print "7-9: "
print sum7,sum8,sum9
print "10-12: "
print sum10, sum11, sum12

fig = plt.figure(figsize=(12, 6))
sqft = fig.add_subplot(121)
cost = fig.add_subplot(122)

sqft.hist(df.Trips_over_the_past_24-hours_(midnight_to_11_:_59pm), bins=80)
sqft.set_xlabel('Ft^2')
sqft.set_title("Histogram of seasonal 24h trips length ")

cost.hist(df.Date, bins=80)
cost.set_xlabel('trips length')
cost.set_title("dates")

plt.show()

