import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn import cluster

#trend


df = pd.read_csv('NYC-vehicle-collisions.csv')
df1 = pd.read_csv('Transportation/NYCSubwayData/NYC_Transit_Subway_Entrance_And_Exit_Data.csv')


df = df[(df['LATITUDE']!=0) &(df['LATITUDE']<42)&(df['LATITUDE']>35)]
df = df[(df['LONGITUDE']!=0)&(df['LONGITUDE']<-71)&(df['LONGITUDE']>-75)]
df1 = df[['LATITUDE','LONGITUDE']]


df1 =pd.DataFrame(df1)
df1 = df1.dropna(how='any',axis = 0)
print(df1.isnull().any())
#print df1
plt.scatter(df1.iloc[:20000].LATITUDE, df1.iloc[:20000].LONGITUDE,s=0.5)
#plt.scatter(df1.LATITUDE, df1.LONGITUDE,s=0.5)
#plt.show()

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
print(centroids[0,0],centroids[0,1])
print(centroids[1,0],centroids[1,1])
print(centroids[2,0],centroids[2,1])
#plt.show()





