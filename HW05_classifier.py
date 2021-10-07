import sys
fileName = sys.argv[1]
fileOpened = open(fileName, "r")
for line in fileOpened:
  line = line.strip()
