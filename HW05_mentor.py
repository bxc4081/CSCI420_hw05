# Brandon Chen & Jack Xu
# CSCI 420
# Bhutan = +1
# Assam = -1


# global variables
header = ["age", "height", "tail length", "hair length", "bang length", "reach", "earlobes"]
header_dict = {"age":0, "height": 1, "tail length":2 , "hair length":3 , "bang length": 4, "reach": 5, "earlobes": 6}

# read and quantize the data
def readData(fileName):
    file = open(fileName)
    dataArray = []
    file.readline()
    for line in file:
        data = line.split(',')
        # quantize age
        data[0] = round(float(data[0])/2) * 2
        # quantize height
        data[1] = round(float(data[1])/5) * 5
        # quantize everything else
        data[2] = round(float(data[2]))
        data[3] = round(float(data[3]))
        data[4] = round(float(data[4]))
        data[5] = round(float(data[5]))
        data[6] = int(data[6])
        data[8] = data[8].strip()
        dataArray.append(data)
    return dataArray

# decision tree criteria:
# - binary splits
# - leaf node should have at least 3 records
# - maximum depth of 26
# - weighted gini index for best split
# - stop recursing if there are less than 3 data points
# - stop recursing if the node is greater than or equal to 95% one class or the other
# - stop recursing if the tree depth has greater than or equal to 26 levels

def decisionTree(data, depth):
    AssamPercent = getPercentageOfClass(data)
    BhuttanPercent = 1 - AssamPercent
    # print(data)
    # print(AssamPercent, BhuttanPercent)
    if depth >= 26 or len(data) <= 3 or AssamPercent > .95 or BhuttanPercent > .95:
        # This is a leaf node
        # print(header[attribute] + ' node')
        # print(AssamPercent)
        # print(BhuttanPercent)
        print(data)
        print('Assam: ' + str(AssamPercent))
        print('Bhuttan: ' + str(BhuttanPercent))
        return
    else:
        # Stopping criteria not met
        currBestAttributeThreshold, currBestAttributeGini = float("inf"), float("inf")
        currBestAttribute = ""
        currBestLessThanSplit = []
        currBestGreaterThanSplit = []
        # for each attribute, find the best split based on the weighted gini index
        for attribute in header_dict:
            bestAttributeSplit = findBestSplit(data, attribute)
            #Check the Weighted gini index
            if (bestAttributeSplit[1] < currBestAttributeGini):
                #bestAttributeSplit = [threshold, Gini, lessThanSplit, greaterThanSplit]
                currBestAttribute = attribute
                currBestAttributeThreshold = bestAttributeSplit[0]
                currBestAttributeGini = bestAttributeSplit[1]
                currBestLessThanSplit = bestAttributeSplit[2]
                currBestGreaterThanSplit = bestAttributeSplit[3]
        #Now we have found the best attribute with the lowest minimum weighted gini index
        #Find the split again
        print("At depth = {}, our best attribute is {} and threshold val is {}".format(depth, currBestAttribute, currBestAttributeThreshold))
        depth += 1
        decisionTree(currBestLessThanSplit, depth)
        decisionTree(currBestGreaterThanSplit, depth)



# we are splitting the data based on the weighted gini index
def findBestSplit(aggregateData, attribute):
    attributeIndex = header_dict[attribute]
    min, max = getRangeOfData(aggregateData, attributeIndex)
    currMinGiniIndex = float("inf")
    currThreshold = -1
    currBestLessThanSplit = []
    currBestGreaterThanSplit = []
    # print(data)
    for thresholdVal in range(min, max+1):
        #split the data
        #Greater than = right split
        #Less than equal to = left split
        greater_than = []
        less_than_equal_to = []
        for currData in aggregateData:
            currAttributeVal = currData[attributeIndex]
            if (currAttributeVal > thresholdVal):
                greater_than.append(currData)
            else:
                less_than_equal_to.append(currData)
        # print(attribute)
        # print(thresholdVal)
        # print(greater_than)
        # print(less_than_equal_to)
        #Finished with current threshold split
        #Calculate the weighted gini index
        weightedGiniIndex = findWeightedGiniIndex(less_than_equal_to, greater_than)
        if (weightedGiniIndex < currMinGiniIndex):
            currMinGiniIndex = weightedGiniIndex
            currThreshold = thresholdVal
            currBestLessThanSplit = less_than_equal_to
            currBestGreaterThanSplit = greater_than
    return currThreshold, currMinGiniIndex, currBestLessThanSplit, currBestGreaterThanSplit

def findWeightedGiniIndex(lessThanEqualTo, greaterThan):
    # print(lessThanEqualTo, greaterThan)
    #Find the weighted Gini Index
    lessThanSplitGiniVal = findGiniIndex(lessThanEqualTo)
    greaterThanSplitGiniVal = findGiniIndex(greaterThan)

    totalLen = len(lessThanEqualTo) + len(greaterThan)
    lessThanEqualToWeighted = len(lessThanEqualTo) / totalLen * lessThanSplitGiniVal
    greaterThanWeighted = len(greaterThan) / totalLen * greaterThanSplitGiniVal

    return lessThanEqualToWeighted + greaterThanWeighted

def findGiniIndex(splitArray):
    if (len(splitArray) == 0):
        return 0
    #Find C0 aka Bhutan aka +1
    #Find C1 aka Assam aka -1
    bhutanCount = 0
    assamCount = 0
    for currElement in splitArray:
        if (currElement[-1] == "+1"):
            bhutanCount += 1
        else:
            assamCount += 1
    bhutanCountPerc = bhutanCount / len(splitArray)
    assamCountPerc = assamCount / len(splitArray)
    bhutanCountSquared = bhutanCountPerc * bhutanCountPerc
    assamCountSquared = assamCountPerc * assamCountPerc
    giniVal = 1 - bhutanCountSquared - assamCountSquared
    return giniVal
        

def getRangeOfData(data, attributeNumber):
    min = float('inf')
    max = float('-inf')
    for row in data:
        if row[attributeNumber] < min:
            min = row[attributeNumber]
        if row[attributeNumber] > max:
            max = row[attributeNumber]
    return min, max

def getPercentageOfClass(data):
    if (len(data) == 0):
        return 0
    total = 0
    Assam = 0
    Bhuttan = 0
    for row in data:
        if row[-1] == "+1":
            Bhuttan += 1
        else:
            Assam += 1
        total += 1
    return Assam/total

def main():
    trainingDataFile = 'Test_suite_C_tail.csv'
    dataArray = readData(trainingDataFile)
    decisionTree(dataArray, 0)
    # findBestSplit(dataArray, )
    # print(dataArray)
    

if __name__ == '__main__':
    main()