import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn import cluster
from matplotlib import rcParams
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
import seaborn as sns


def collision_cluster():
	df = pd.read_csv("NYCGeneralTransport/NYC-vehicle-collisions.csv", low_memory=False)
	df = df[(df['LATITUDE']!=0) &(df['LATITUDE']<42)&(df['LATITUDE']>35)]
	df = df[(df['LONGITUDE']!=0)&(df['LONGITUDE']<-71)&(df['LONGITUDE']>-75)]
	df1 = df[['LATITUDE','LONGITUDE']]
	df1 = pd.DataFrame(df1)
	df1 = df1.dropna(how='any',axis = 0)
	print(df1.isnull().any())
	#print df1
	plt.scatter(df1.LATITUDE, df1.LONGITUDE,s=0.2)
	#plt.scatter(df1.LATITUDE, df1.LONGITUDE,s=0.5)
	#plt.show()

	faith = np.array(df1)
	k = 3
	kmeans = cluster.KMeans(n_clusters=k)
	kmeans.fit(faith)
	labels = kmeans.labels_
	centroids = kmeans.cluster_centers_

	for i in range(k):
	    # select only data observations with cluster label == i
	    ds = faith[np.where(labels==i)]
	    # plot the data observations
	    plt.plot(ds[:,0],ds[:,1],'o', markersize=0.5)
	    # plot the centroids
	    lines = plt.plot(centroids[i,0],centroids[i,1],'kx')
	    # make the centroid x's bigger
	    plt.setp(lines,ms=5.0)
	    plt.setp(lines,mew=2.0)
	plt.show()

def subway_entrance(): 
	data = pd.read_csv("NYCSubwayData/NYC_Transit_Subway_Entrance_And_Exit_Data.csv", low_memory=False)
	data = data[(data['Entrance Latitude']!=0) &(data['Entrance Latitude']<42)&(data['Entrance Latitude']>35)]
	data = data[(data['Entrance Longitude']!=0)&(data['Entrance Longitude']<-71)&(data['Entrance Longitude']>-75)]
	data1 = data[['Entrance Latitude','Entrance Longitude']]
	
	data1 =data1.dropna(how='any',axis = 0)
	print data1
	
	plt.scatter(data1.iloc[:,0], data1.iloc[:,1],s=0.5)
	

def cluster_graph(df1):
	faith = np.array(df1)
	k = 10
	kmeans = cluster.KMeans(n_clusters=k)
	kmeans.fit(faith)
	labels = kmeans.labels_
	centroids = kmeans.cluster_centers_

	for i in range(k):
	    # select only data observations with cluster label == i
	    ds = faith[np.where(labels==i)]
	    # plot the data observations
	    plt.plot(ds[:,0],ds[:,1],'o', markersize=0.5)
	    # plot the centroids
	    lines = plt.plot(centroids[i,0],centroids[i,1],'kx')
	    # make the centroid x's bigger
	    plt.setp(lines,ms=5.0)
	    plt.setp(lines,mew=2.0)
def cluster_dot(df1):
	faith = np.array(df1)
	k = 8
	kmeans = cluster.KMeans(n_clusters=k)
	kmeans.fit(faith)
	labels = kmeans.labels_
	centroids = kmeans.cluster_centers_

	for i in range(k):
	    # select only data observations with cluster label == i
	    ds = faith[np.where(labels==i)]
	    # plot the data observations
	    #plt.plot(ds[:,0],ds[:,1],'o', markersize=0.5)
	    # plot the centroids
	    lines = plt.plot(centroids[i,0],centroids[i,1],'kx')
	    # make the centroid x's bigger
	    plt.setp(lines,ms=6.0)
	    plt.setp(lines,mew=2.0)

def subway_entryhr_temp():
	df = pd.read_excel(open('NYCSubwayData/nyc-subway-turnstile-and-weather.csv.xlsx','rb'))
	m = ols('ENTRIES_hourly ~ temp ',df).fit()
	print (m.summary())
	print('\n')
	print('\n')
	print('\n')
	m = ols('ENTRIES_hourly ~ temp + rain + windspeed+ meanprecip +meanwindspeed',df).fit()
	print (m.summary())
	#sns.jointplot(x="temp", y="ENTRIES_hourly", data=df, kind = 'reg',fit_reg= True, size = 7)
	#plt.show()

def bike_mile_vs_pass():
	df = pd.read_excel(open('NYCSubwayData/nyc-subway-turnstile-and-weather.csv.xlsx','rb'))
	m = ols('ENTRIES_hourly ~ temp ',df).fit()
	print (m.summary())
	print('\n')
	print('\n')
	print('\n')
	m = ols('ENTRIES_hourly ~ temp + rain ',df).fit()
	print (m.summary())



	data = pd.read_csv("NYCSubwayData/NYC_Transit_Subway_Entrance_And_Exit_Data.csv", low_memory=False)
	data = data[(data['Entrance Latitude']!=0) &(data['Entrance Latitude']<42)&(data['Entrance Latitude']>35)]
	data = data[(data['Entrance Longitude']!=0)&(data['Entrance Longitude']<-71)&(data['Entrance Longitude']>-75)]
	data1 = data[['Entrance Latitude','Entrance Longitude']]

	data1 =data1.dropna(how='any',axis = 0)
#cluster_dot(data1)
#collision_cluster()
#plt.show()

#collision_cluster()

#print(df1)

#collision_cluster()
#plt.show()

#df = pd.read_csv("test.csv", low_memory=False)

df = pd.read_excel(open('test.xlsx','rb'))
#print(df)
#df1 =df[['Milestraveledtodaymidnightto1159pm','24HourPassesPurchasedmidnightto1159pm']]
#print(df.head())
#m = ols("miletoday ~ pass", df).fit()                   
sns.jointplot(x="pass", y="miletoday", data=df, kind = 'reg',fit_reg= True, size = 7)
plt.show()
#print (m.summary())
#m = ols(formula="miletoday ~ pass ",data=df).fit()
