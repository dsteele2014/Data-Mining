#Nolan Sliger and Darcy Steele 2/1/2018
#CS455 Assignment 1
import csv
import math

class csvParser():

	def __init__(self):
		self.siteList = []
		self.statusList = []
		self.healthList = []
		self.root_stoneList = []
		self.latitudeList = []
		self.longitudeList = []
	
	def csvReader(self):
		with open('cs455_project1_part1_Sliger_Steele.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.siteList.append(row['site'])
				self.statusList.append(row['status'])
				self.healthList.append(row['health'])
				self.root_stoneList.append(row['root_stone'])
				self.latitudeList.append(row['latitude'])
				self.longitudeList.append(row['longitude'])

	
class attributeComputations():

	
	def computeMax(self, dataList):
		maxNum = None
		for i in dataList:
			if maxNum is None:
				maxNum = i
			else:
				if i > maxNum:
					maxNum = i
		return maxNum

	def computeMin(self, dataList):
		minNum = None
		for i in dataList:
			if minNum is None:
				minNum = i
			else:
				if i < minNum:
					minNum = i
		return minNum
	
	def computeMedian(self, dataList):
		listSize = len(dataList)
		if listSize%2==0:
			median = dataList[listSize/2]
		else:
			ceiling = math.ceil(listSize/2)
			floor = math.floor(listSize/2)
			median = (float(dataList[floor])+float(dataList[ceiling]))/2
			
		return median
	
	def computeMode(self,dataList):
		
		for i in range(0,len(dataList)):
			       dataList[i]=round(float(dataList[i]),2)
		mode = max(set(dataList), key=dataList.count)
		return mode
	
	def computeMean(self, dataList):
		total = 0
		for i in range(0,len(dataList)):
			total = total + float(dataList[i])
		mean = total/len(dataList)

		return mean
	
	def computeStandardDeviation(self, dataList, mean):
		total = 0
		for i in range(0, len(dataList)):
			total = total + math.sqrt(math.fabs(float(dataList[i])- mean))
		total = total/len(dataList)
		standardDeviation = math.sqrt(math.fabs(total))
		return standardDeviation

	def computeBooleanFrequency(self, datalist):
			#yes and no are the boolean attributes
			counter_true = 0;
			counter_false = 0;
			for i in datalist:
					if i == "Yes":
						counter_true +=1
			counter_false = (1000 - counter_true)
			return (counter_true, counter_false)
		
	def computeCategoricalFrequency_status(self, datalist):
		#categorical are status (alive, stump, dead) 
			counter_alive = 0;
			counter_stump = 0;
			counter_dead = 0;
			for i in datalist:
					if i == "Alive":
						counter_alive +=1
					elif i == "Stump":
						counter_stump +=1
						counter_dead = (1000 - (counter_stump + counter_alive))
			return (counter_alive, counter_stump, counter_dead)
		
	def computeCategoricalFrequency_site(self, datalist):
			#categorical site(front, adjacent, side, median, assigned, across, rear)
			counter_front = 0;
			counter_adjacent = 0;
			counter_side = 0;
			counter_median = 0;
			counter_assigned = 0;
			counter_across = 0;
			counter_rear = 0;
			
			for i in datalist:
					if i == "Front":
						counter_front +=1
					elif i == "Adjacent":
						counter_adjacent +=1
					elif i == "Side":
						counter_side +=1
					elif i == "Median":
						counter_median +=1
					elif i == "Assigned":
						counter_assigned +=1
					elif i == "Across":
						counter_across +=1
					elif i == "Rear":
						counter_rear +=1
			return (counter_front, counter_adjacent, counter_side, counter_median, counter_assigned, counter_across, counter_rear)	
			
	
	def computeOrdinalFrequency(self, datalist):
			#good, fair, poor, dead are the ordinal attributes
			counter_good = 0;
			counter_fair = 0;
			counter_poor = 0;
			#counter_dead
			for i in datalist:
					if i == "Good":
						counter_good += 1
					elif i == "Fair":
						counter_fair += 1
					elif i == "Poor":
						counter_poor += 1
			counter_dead = (1000 - (counter_good + counter_fair + counter_poor))
			return (counter_good, counter_fair, counter_poor, counter_dead)
	    
class main():
	parser = csvParser()
	parser.csvReader()
	computations = attributeComputations()
	maxlat = computations.computeMax(parser.latitudeList)
	minlat = computations.computeMin(parser.latitudeList)
	medlat = computations.computeMedian(parser.latitudeList)
	meanlat = computations.computeMean(parser.latitudeList)
	sdlat = computations.computeStandardDeviation(parser.latitudeList, meanlat)
	modelat = computations.computeMode(parser.latitudeList)
	print(modelat)
	maxlong = computations.computeMax(parser.longitudeList)
	minlong = computations.computeMin(parser.longitudeList)
	medlong = computations.computeMedian(parser.longitudeList)
	meanlong = computations.computeMean(parser.longitudeList)
	sdlong = computations.computeStandardDeviation(parser.longitudeList, meanlong)
	modelong = computations.computeMode(parser.longitudeList)
	print(modelong)
	bool_freq = computations.computeBooleanFrequency(parser.root_stoneList)
	categorical_freq_site = computations.computeCategoricalFrequency_site(parser.siteList)
	categorical_freq_status = computations.computeCategoricalFrequency_status(parser.statusList)
	ordinal_freq_status = computations.computeOrdinalFrequency(parser.healthList)
	print(bool_freq)
	print(categorical_freq_site)
	print(categorical_freq_status)
	print(ordinal_freq_status)
	
