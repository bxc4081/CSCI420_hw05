import sys
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
        dataArray.append(data)
    return dataArray
fileName = sys.argv[1]
fileOpened = open(fileName, "r")
fileOpened.readline()
classificationFile = open("HW05_MyClassifications.csv", "w")
indexDict = {"age":0, "height": 1, "tail length":2 , "hair length":3 , "bang length": 4, "reach": 5, "earlobes": 6}
dataArray = readData(fileName)
for line in dataArray:
    if float(line[indexDict['earlobes']]) <= 0:
      if float(line[indexDict['hair length']]) <= 10:
        if float(line[indexDict['bang length']]) <= 6:
          classificationFile.write('-1\n')
        else:
          if float(line[indexDict['hair length']]) <= 7:
            if float(line[indexDict['tail length']]) <= 3:
              classificationFile.write('+1\n')
            else:
              if float(line[indexDict['tail length']]) <= 19:
                if float(line[indexDict['age']]) <= 44:
                  if float(line[indexDict['height']]) <= 140:
                    if float(line[indexDict['tail length']]) <= 13:
                      if float(line[indexDict['age']]) <= 36:
                        classificationFile.write('-1\n')
                      else:
                        classificationFile.write('+1\n')
                    else:
                      classificationFile.write('-1\n')
                  else:
                    classificationFile.write('-1\n')
                else:
                  classificationFile.write('-1\n')
              else:
                classificationFile.write('+1\n')
          else:
            if float(line[indexDict['age']]) <= 42:
              if float(line[indexDict['reach']]) <= 148:
                if float(line[indexDict['tail length']]) <= 22:
                  if float(line[indexDict['reach']]) <= 123:
                    classificationFile.write('-1\n')
                  else:
                    classificationFile.write('+1\n')
                else:
                  classificationFile.write('-1\n')
              else:
                if float(line[indexDict['reach']]) <= 159:
                  if float(line[indexDict['age']]) <= 20:
                    classificationFile.write('+1\n')
                  else:
                    if float(line[indexDict['hair length']]) <= 9:
                      if float(line[indexDict['height']]) <= 145:
                        classificationFile.write('+1\n')
                      else:
                        classificationFile.write('-1\n')
                    else:
                      if float(line[indexDict['reach']]) <= 150:
                        classificationFile.write('-1\n')
                      else:
                        if float(line[indexDict['age']]) <= 34:
                          classificationFile.write('-1\n')
                        else:
                          classificationFile.write('+1\n')
                else:
                  classificationFile.write('-1\n')
            else:
              if float(line[indexDict['reach']]) <= 154:
                if float(line[indexDict['tail length']]) <= 6:
                  if float(line[indexDict['age']]) <= 46:
                    classificationFile.write('-1\n')
                  else:
                    classificationFile.write('+1\n')
                else:
                  if float(line[indexDict['age']]) <= 48:
                    if float(line[indexDict['reach']]) <= 143:
                      classificationFile.write('-1\n')
                    else:
                      if float(line[indexDict['reach']]) <= 148:
                        classificationFile.write('+1\n')
                      else:
                        if float(line[indexDict['age']]) <= 46:
                          classificationFile.write('-1\n')
                        else:
                          classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['bang length']]) <= 7:
                      if float(line[indexDict['tail length']]) <= 11:
                        if float(line[indexDict['age']]) <= 62:
                          if float(line[indexDict['reach']]) <= 141:
                            if float(line[indexDict['hair length']]) <= 8:
                              classificationFile.write('+1\n')
                            else:
                              classificationFile.write('-1\n')
                          else:
                            classificationFile.write('-1\n')
                        else:
                          classificationFile.write('+1\n')
                      else:
                        classificationFile.write('-1\n')
                    else:
                      classificationFile.write('+1\n')
              else:
                if float(line[indexDict['hair length']]) <= 8:
                  if float(line[indexDict['tail length']]) <= 7:
                    classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['reach']]) <= 156:
                      if float(line[indexDict['tail length']]) <= 8:
                        classificationFile.write('+1\n')
                      else:
                        classificationFile.write('-1\n')
                    else:
                      if float(line[indexDict['tail length']]) <= 9:
                        classificationFile.write('-1\n')
                      else:
                        classificationFile.write('+1\n')
                else:
                  if float(line[indexDict['tail length']]) <= 11:
                    classificationFile.write('+1\n')
                  else:
                    if float(line[indexDict['tail length']]) <= 14:
                      classificationFile.write('-1\n')
                    else:
                      classificationFile.write('+1\n')
      else:
        if float(line[indexDict['bang length']]) <= 5:
          if float(line[indexDict['hair length']]) <= 11:
            if float(line[indexDict['tail length']]) <= 5:
              if float(line[indexDict['age']]) <= 40:
                classificationFile.write('+1\n')
              else:
                classificationFile.write('-1\n')
            else:
              if float(line[indexDict['age']]) <= 68:
                if float(line[indexDict['bang length']]) <= 2:
                  classificationFile.write('-1\n')
                else:
                  if float(line[indexDict['tail length']]) <= 16:
                    classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['age']]) <= 60:
                      if float(line[indexDict['age']]) <= 46:
                        if float(line[indexDict['tail length']]) <= 18:
                          if float(line[indexDict['age']]) <= 42:
                            classificationFile.write('-1\n')
                          else:
                            classificationFile.write('+1\n')
                        else:
                          classificationFile.write('-1\n')
                      else:
                        classificationFile.write('-1\n')
                    else:
                      classificationFile.write('+1\n')
              else:
                classificationFile.write('+1\n')
          else:
            if float(line[indexDict['height']]) <= 145:
              if float(line[indexDict['age']]) <= 58:
                if float(line[indexDict['height']]) <= 140:
                  if float(line[indexDict['age']]) <= 24:
                    classificationFile.write('-1\n')
                  else:
                    classificationFile.write('+1\n')
                else:
                  if float(line[indexDict['reach']]) <= 146:
                    classificationFile.write('-1\n')
                  else:
                    classificationFile.write('+1\n')
              else:
                classificationFile.write('-1\n')
            else:
              if float(line[indexDict['height']]) <= 160:
                classificationFile.write('-1\n')
              else:
                classificationFile.write('-1\n')
        else:
          if float(line[indexDict['age']]) <= 48:
            if float(line[indexDict['reach']]) <= 157:
              if float(line[indexDict['height']]) <= 135:
                classificationFile.write('+1\n')
              else:
                if float(line[indexDict['bang length']]) <= 6:
                  if float(line[indexDict['tail length']]) <= 14:
                    classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['height']]) <= 150:
                      classificationFile.write('+1\n')
                    else:
                      classificationFile.write('+1\n')
                else:
                  if float(line[indexDict['bang length']]) <= 7:
                    classificationFile.write('+1\n')
                  else:
                    if float(line[indexDict['tail length']]) <= 9:
                      classificationFile.write('-1\n')
                    else:
                      classificationFile.write('+1\n')
            else:
              if float(line[indexDict['hair length']]) <= 11:
                classificationFile.write('-1\n')
              else:
                if float(line[indexDict['age']]) <= 42:
                  classificationFile.write('-1\n')
                else:
                  classificationFile.write('+1\n')
          else:
            if float(line[indexDict['bang length']]) <= 6:
              if float(line[indexDict['tail length']]) <= 13:
                classificationFile.write('-1\n')
              else:
                if float(line[indexDict['height']]) <= 135:
                  classificationFile.write('-1\n')
                else:
                  classificationFile.write('+1\n')
            else:
              if float(line[indexDict['tail length']]) <= 11:
                classificationFile.write('+1\n')
              else:
                if float(line[indexDict['tail length']]) <= 12:
                  classificationFile.write('-1\n')
                else:
                  if float(line[indexDict['tail length']]) <= 15:
                    classificationFile.write('+1\n')
                  else:
                    classificationFile.write('-1\n')
    else:
      if float(line[indexDict['bang length']]) <= 4:
        if float(line[indexDict['hair length']]) <= 9:
          if float(line[indexDict['tail length']]) <= 9:
            if float(line[indexDict['bang length']]) <= 2:
              classificationFile.write('-1\n')
            else:
              if float(line[indexDict['age']]) <= 34:
                classificationFile.write('+1\n')
              else:
                if float(line[indexDict['age']]) <= 38:
                  if float(line[indexDict['hair length']]) <= 7:
                    classificationFile.write('-1\n')
                  else:
                    classificationFile.write('-1\n')
                else:
                  if float(line[indexDict['height']]) <= 140:
                    if float(line[indexDict['age']]) <= 50:
                      if float(line[indexDict['hair length']]) <= 7:
                        classificationFile.write('-1\n')
                      else:
                        if float(line[indexDict['age']]) <= 44:
                          if float(line[indexDict['age']]) <= 42:
                            classificationFile.write('+1\n')
                          else:
                            classificationFile.write('-1\n')
                        else:
                          classificationFile.write('+1\n')
                    else:
                      classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['age']]) <= 54:
                      classificationFile.write('+1\n')
                    else:
                      if float(line[indexDict['age']]) <= 56:
                        classificationFile.write('-1\n')
                      else:
                        classificationFile.write('+1\n')
          else:
            if float(line[indexDict['reach']]) <= 139:
              classificationFile.write('-1\n')
            else:
              if float(line[indexDict['hair length']]) <= 7:
                if float(line[indexDict['hair length']]) <= 5:
                  classificationFile.write('+1\n')
                else:
                  if float(line[indexDict['height']]) <= 140:
                    if float(line[indexDict['age']]) <= 32:
                      classificationFile.write('+1\n')
                    else:
                      if float(line[indexDict['tail length']]) <= 14:
                        classificationFile.write('+1\n')
                      else:
                        classificationFile.write('-1\n')
                  else:
                    classificationFile.write('-1\n')
              else:
                if float(line[indexDict['tail length']]) <= 20:
                  if float(line[indexDict['age']]) <= 60:
                    if float(line[indexDict['height']]) <= 160:
                      if float(line[indexDict['age']]) <= 38:
                        classificationFile.write('+1\n')
                      else:
                        if float(line[indexDict['tail length']]) <= 11:
                          if float(line[indexDict['age']]) <= 52:
                            classificationFile.write('+1\n')
                          else:
                            classificationFile.write('-1\n')
                        else:
                          if float(line[indexDict['bang length']]) <= 3:
                            classificationFile.write('-1\n')
                          else:
                            if float(line[indexDict['height']]) <= 145:
                              if float(line[indexDict['age']]) <= 44:
                                classificationFile.write('+1\n')
                              else:
                                classificationFile.write('-1\n')
                            else:
                              if float(line[indexDict['age']]) <= 44:
                                if float(line[indexDict['height']]) <= 150:
                                  classificationFile.write('-1\n')
                                else:
                                  classificationFile.write('-1\n')
                              else:
                                if float(line[indexDict['age']]) <= 52:
                                  classificationFile.write('+1\n')
                                else:
                                  classificationFile.write('+1\n')
                    else:
                      classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['age']]) <= 62:
                      classificationFile.write('-1\n')
                    else:
                      classificationFile.write('-1\n')
                else:
                  if float(line[indexDict['height']]) <= 155:
                    classificationFile.write('-1\n')
                  else:
                    classificationFile.write('-1\n')
        else:
          if float(line[indexDict['bang length']]) <= 3:
            if float(line[indexDict['reach']]) <= 163:
              if float(line[indexDict['height']]) <= 125:
                classificationFile.write('+1\n')
              else:
                if float(line[indexDict['hair length']]) <= 10:
                  classificationFile.write('-1\n')
                else:
                  classificationFile.write('-1\n')
            else:
              classificationFile.write('+1\n')
          else:
            if float(line[indexDict['age']]) <= 62:
              if float(line[indexDict['tail length']]) <= 17:
                classificationFile.write('+1\n')
              else:
                if float(line[indexDict['height']]) <= 155:
                  if float(line[indexDict['reach']]) <= 152:
                    classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['age']]) <= 22:
                      classificationFile.write('-1\n')
                    else:
                      classificationFile.write('+1\n')
                else:
                  classificationFile.write('-1\n')
            else:
              if float(line[indexDict['height']]) <= 140:
                classificationFile.write('-1\n')
              else:
                classificationFile.write('+1\n')
      else:
        if float(line[indexDict['hair length']]) <= 8:
          if float(line[indexDict['tail length']]) <= 9:
            classificationFile.write('+1\n')
          else:
            if float(line[indexDict['reach']]) <= 138:
              if float(line[indexDict['age']]) <= 26:
                classificationFile.write('+1\n')
              else:
                if float(line[indexDict['tail length']]) <= 17:
                  if float(line[indexDict['age']]) <= 42:
                    if float(line[indexDict['tail length']]) <= 11:
                      if float(line[indexDict['age']]) <= 38:
                        if float(line[indexDict['hair length']]) <= 7:
                          classificationFile.write('-1\n')
                        else:
                          classificationFile.write('-1\n')
                      else:
                        classificationFile.write('+1\n')
                    else:
                      classificationFile.write('-1\n')
                  else:
                    classificationFile.write('-1\n')
                else:
                  classificationFile.write('+1\n')
            else:
              if float(line[indexDict['tail length']]) <= 15:
                if float(line[indexDict['reach']]) <= 141:
                  if float(line[indexDict['age']]) <= 46:
                    if float(line[indexDict['hair length']]) <= 6:
                      if float(line[indexDict['tail length']]) <= 11:
                        classificationFile.write('+1\n')
                      else:
                        classificationFile.write('-1\n')
                    else:
                      classificationFile.write('+1\n')
                  else:
                    if float(line[indexDict['bang length']]) <= 6:
                      classificationFile.write('-1\n')
                    else:
                      classificationFile.write('-1\n')
                else:
                  if float(line[indexDict['height']]) <= 165:
                    classificationFile.write('+1\n')
                  else:
                    classificationFile.write('-1\n')
              else:
                if float(line[indexDict['bang length']]) <= 5:
                  if float(line[indexDict['tail length']]) <= 18:
                    if float(line[indexDict['age']]) <= 44:
                      classificationFile.write('-1\n')
                    else:
                      if float(line[indexDict['height']]) <= 135:
                        classificationFile.write('+1\n')
                      else:
                        if float(line[indexDict['height']]) <= 145:
                          classificationFile.write('-1\n')
                        else:
                          if float(line[indexDict['reach']]) <= 162:
                            if float(line[indexDict['reach']]) <= 157:
                              if float(line[indexDict['tail length']]) <= 16:
                                classificationFile.write('-1\n')
                              else:
                                classificationFile.write('+1\n')
                            else:
                              classificationFile.write('+1\n')
                          else:
                            classificationFile.write('-1\n')
                  else:
                    if float(line[indexDict['age']]) <= 40:
                      if float(line[indexDict['height']]) <= 145:
                        classificationFile.write('+1\n')
                      else:
                        classificationFile.write('-1\n')
                    else:
                      if float(line[indexDict['height']]) <= 165:
                        if float(line[indexDict['height']]) <= 140:
                          classificationFile.write('-1\n')
                        else:
                          classificationFile.write('-1\n')
                      else:
                        classificationFile.write('+1\n')
                else:
                  if float(line[indexDict['age']]) <= 60:
                    if float(line[indexDict['height']]) <= 160:
                      if float(line[indexDict['hair length']]) <= 4:
                        classificationFile.write('-1\n')
                      else:
                        if float(line[indexDict['age']]) <= 48:
                          classificationFile.write('+1\n')
                        else:
                          if float(line[indexDict['hair length']]) <= 6:
                            classificationFile.write('-1\n')
                          else:
                            if float(line[indexDict['tail length']]) <= 18:
                              if float(line[indexDict['reach']]) <= 149:
                                if float(line[indexDict['age']]) <= 56:
                                  if float(line[indexDict['height']]) <= 140:
                                    classificationFile.write('-1\n')
                                  else:
                                    classificationFile.write('+1\n')
                                else:
                                  classificationFile.write('+1\n')
                              else:
                                classificationFile.write('+1\n')
                            else:
                              classificationFile.write('+1\n')
                    else:
                      classificationFile.write('-1\n')
                  else:
                    classificationFile.write('-1\n')
        else:
          classificationFile.write('+1\n')
