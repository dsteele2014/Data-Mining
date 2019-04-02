import csv
import math

class csvParser():

    def __init__(self):
        self.curb_locList = []
        self.statusList = []
        self.healthList = []
        self.root_stoneList = []
        self.latitudeList = []
        self.longitudeList = []
    
    def csvReader(self):
        with open('cs455_project1_part1_Sliger_Steele.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.curb_locList.append(row['curb_loc'])
                self.statusList.append(row['status'])
                self.healthList.append(row['health'])
                self.root_stoneList.append(row['root_stone'])
                self.latitudeList.append(row['latitude'])
                self.longitudeList.append(row['longitude'])

    
class numericAttributeComputations():

    
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
    
    def mode():
        pass
    
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

class main():
    parser = csvParser()
    parser.csvReader()
    numericComputations = numericAttributeComputations()
    maxlat = numericComputations.computeMax(parser.latitudeList)
    minlat = numericComputations.computeMin(parser.latitudeList)
    medlat = numericComputations.computeMedian(parser.latitudeList)
    meanlat = numericComputations.computeMean(parser.latitudeList)
    sdlat = numericComputations.computeStandardDeviation(parser.latitudeList, meanlat)
    print(medlat)
    print(sdlat)
    maxlong = numericComputations.computeMax(parser.longitudeList)
    minlong = numericComputations.computeMin(parser.longitudeList)
    medlong = numericComputations.computeMedian(parser.longitudeList)
    meanlong = numericComputations.computeMean(parser.longitudeList)
    sdlong = numericComputations.computeStandardDeviation(parser.longitudeList, meanlong)
    print(medlong)
    print(sdlong)
    
