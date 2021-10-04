# Brandon Chen & Jack Xu
# CSCI 420


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



def main():
    trainingDataFile = 'Abominable_Data_HW_LABELED_TRAINING_DATA__v740.csv'
    dataArray = readData(trainingDataFile)
    

if __name__ == '__main__':
    main()