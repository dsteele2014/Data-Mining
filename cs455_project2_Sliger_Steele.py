#Nolan Sliget and Darcy Steele 3/1/2018
#CS455 Assignment 2

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

class csvParser():
	def __init__(self):
		self.data = [[0 for x in range(200)]for y in range(2)]
	
	def csvReader(self):
		with open('cs455_project2_Sliger_Steele.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			i=0
			for row in reader:
			    self.data[0][i] = (float(row['longitude']))
			    self.data[1][i] = (float(row['latitude']))
			    i=i+1

class normalizeData():
		def __init__(self):
			self.normData = [[0 for x in range(200)]for y in range(2)]
			
		def normalize(self, data):
			highLong = max(data[0])
			lowLong = min(data[0])
			highLat = max(data[1])
			lowLat = min(data[1])
			highNorm = 100
			lowNorm = 0
			
			for i in range (0,1):
				for j in range(0,200):
					self.normData[i][j] = (round(lowNorm + (data[i][j]-lowLong)*(highNorm - lowNorm) / (highLong-lowLong)))
			for i in range (1,2):
				for j in range(0,200):
					self.normData[i][j] = (round(lowNorm + (data[i][j]-lowLat)*(highNorm - lowNorm) / (highLat-lowLat)))




class kMeans():
	def __init__(self):
		self.centroids = [[0 for x in range(2)]for y in range(2)]
		self.data = []
		self.cluster1 = []
		self.cluster2 = []
		self.meanLong = 0
		self.meanLat = 0
	
	def euclideanDistance(self, longData1, latData1, longData2, latData2):
		distance = ((longData2 - longData1)**2+(latData2 - latData1)**2)**(.5)
		return distance

	def initialPartition(self):
		distance = 0
		for i in range(0, len(self.data[0])):
			for j in range(0,len(self.data[1])):
				d = self.euclideanDistance(self.data[0][i],self.data[1][i],self.data[0][j],self.data[1][j])
				if(d>distance):
					self.centroids[0][0] = self.data[0][i]
					self.centroids[1][0] = self.data[1][i]
					self.centroids[0][1] = self.data[0][j]
					self.centroids[1][1] = self.data[1][j]
					distance = d


	def clustering(self):
		distance1 = 0
		distance2 = 0
		change = 1
		with open('cs455_project2_Sliger_Steele_Results.csv','w') as csvfile:
			fieldnames = ['Cluster','Centroid Long','Centroid Lat']
			writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
			writer.writeheader()
			i=0
			while(change!=0):
				change = 0
				for i in range(0,len(self.data[0])):
					distance1 = self.euclideanDistance(self.centroids[0][0],self.centroids[0][1],self.data[0][i],self.data[1][i])
					distance2 = self.euclideanDistance(self.centroids[1][0],self.centroids[1][1],self.data[0][i],self.data[1][i])
					if(abs(distance1)<abs(distance2)):
						if i in self.cluster1:
							pass
						else:
							change = change+1
							self.cluster1.append(i)
							self.mean(self.cluster1)
							self.centroids[0][0]= self.meanLong
							self.centroids[1][0]= self.meanLat
							
					else:
						if i in self.cluster2:
							pass
						else:
							change = change+1
							self.cluster2.append(i)
							self.mean(self.cluster2)
							self.centroids[0][1]= self.meanLong
							self.centroids[1][1]= self.meanLat
				
				writer.writerow({'Cluster' : 'Cluster 1', 'Centroid Long': self.centroids[0][0], 'Centroid Lat':self.centroids[0][1]})
				writer.writerow({'Cluster' : 'Cluster 2', 'Centroid Long': self.centroids[1][0],'Centroid Lat':self.centroids[1][1]})
				self.drawPlot(self.cluster1,'red')
				self.drawPlot(self.cluster2,'blue')
				self.SSE(self.cluster1,0)
				self.SSE(self.cluster2,1)
				plt.show()


	def mean(self, cluster):
		totalLat=0
		totalLong=0
		for i in range(0,len(cluster)):
			totalLong = totalLong+self.data[0][i]
			totalLat = totalLat + self.data[1][i]
		self.meanLong = totalLong/len(cluster)
		self.meanLat = totalLat/len(cluster)
		

	def SSE(self, cluster,centroid):
		clusterMatrix = [[0 for x in range(len(cluster))]for y in range(2)]
		total = 0
		sse=0
		for i in range(len(cluster)):
			y=int(cluster[i])
			clusterMatrix[0][i] = self.data[0][y]
			clusterMatrix[1][i] = self.data[1][y]
			total = total+self.euclideanDistance(self.centroids[centroid][0],self.centroids[centroid][1],self.data[0][i],self.data[1][i])
		average = total/len(cluster)
		distances= []
		for i in range(len(cluster)):
			distances.append((self.euclideanDistance(self.centroids[centroid][0],self.centroids[centroid][1],self.data[0][i],self.data[1][i])-average)**2)
		sse=sum(distances)        
		print(sse)


	def drawPlot(self, cluster,rgb):
		clusterMatrix = [[0 for x in range(len(cluster))]for y in range(2)]
		for i in range(len(cluster)):
			y = int(cluster[i])
			clusterMatrix[0][i] = self.data[0][y]
			clusterMatrix[1][i] = self.data[1][y]
		plt.scatter(clusterMatrix[0],clusterMatrix[1],color=rgb)

                                	
class main():
	parser = csvParser()
	parser.csvReader()
	normalize = normalizeData()
	normalize.normalize(parser.data)
	kmeans = kMeans()
	kmeans.data = normalize.normData
	kmeans.initialPartition()
	kmeans.clustering()
