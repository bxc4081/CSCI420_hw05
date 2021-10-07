# Brandon Chen & Jack Xu
# CSCI 420


# global variables
header = ["age", "height", "bang length", "tail length", "hair length", "reach", "earlobes"]

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

def decisionTree(data, depth, attribute):
    AssamPercent = getPercentageOfClass(data)[0]
    BhuttanPercent = getPercentageOfClass(data)[1]
    if depth >= 26 or len(data) <= 3 or AssamPercent > .95 or BhuttanPercent > .95:
        # This is a leaf node
        print(header[attribute] + ' node')
        print('Assam: ' + str(AssamPercent))
        print('Bhuttan: ' + str(BhuttanPercent))
    else:
        # Stopping criteria not met
        firstAttribute = 0
        firstThreshold = -1
        goodness = float('inf')
        # for each attribute, find the best split based on the weighted gini index
        for attributeNumber in range(0, 7):
            findBestSplit(data, attributeNumber)

# we are splitting the data based on the weighted gini index
def findBestSplit(data, attributeNumber):
    min, max = getRangeOfData(data)
    for val in range(min, max+1):
        

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
    total = 0
    Assam = 0
    Bhuttan = 0
    for row in data:
        if row[-1] == 1:
            Bhuttan += 1
        else:
            Assam += 1
        total += 1
    return Assam/total, Bhuttan/total

def main():
    trainingDataFile = 'Abominable_Data_HW_LABELED_TRAINING_DATA__v740.csv'
    dataArray = readData(trainingDataFile)
    

if __name__ == '__main__':
    main()