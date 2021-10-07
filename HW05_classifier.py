import sys
fileName = sys.argv[1]
fileOpened = open(fileName, "r")
fileOpened.readline()
arr = []
indexDict = {"age":0, "height": 1, "tail length":2 , "hair length":3 , "bang length": 4, "reach": 5, "earlobes": 6}
for line in fileOpened:
    line = line.strip().split(',')
    if float(line[indexDict['earlobes']]) <= 0:
      if float(line[indexDict['hair length']]) <= 10:
        if float(line[indexDict['bang length']]) <= 6:
          arr.append('-1')
        else:
          if float(line[indexDict['hair length']]) <= 7:
            if float(line[indexDict['tail length']]) <= 3:
              print('+1')
            else:
              if float(line[indexDict['tail length']]) <= 19:
                if float(line[indexDict['age']]) <= 44:
                  if float(line[indexDict['height']]) <= 140:
                    if float(line[indexDict['tail length']]) <= 13:
                      if float(line[indexDict['age']]) <= 36:
                        arr.append('-1')
                      else:
                        print('+1')
                    else:
                      arr.append('-1')
                  else:
                    arr.append('-1')
                else:
                  arr.append('-1')
              else:
                print('+1')
          else:
            if float(line[indexDict['age']]) <= 42:
              if float(line[indexDict['reach']]) <= 148:
                if float(line[indexDict['tail length']]) <= 22:
                  if float(line[indexDict['reach']]) <= 123:
                    arr.append('-1')
                  else:
                    print('+1')
                else:
                  arr.append('-1')
              else:
                if float(line[indexDict['reach']]) <= 159:
                  if float(line[indexDict['age']]) <= 20:
                    print('+1')
                  else:
                    if float(line[indexDict['hair length']]) <= 9:
                      if float(line[indexDict['height']]) <= 145:
                        print('+1')
                      else:
                        arr.append('-1')
                    else:
                      if float(line[indexDict['reach']]) <= 150:
                        arr.append('-1')
                      else:
                        if float(line[indexDict['age']]) <= 34:
                          arr.append('-1')
                        else:
                          print('+1')
                else:
                  arr.append('-1')
            else:
              if float(line[indexDict['reach']]) <= 154:
                if float(line[indexDict['tail length']]) <= 6:
                  if float(line[indexDict['age']]) <= 46:
                    arr.append('-1')
                  else:
                    print('+1')
                else:
                  if float(line[indexDict['age']]) <= 48:
                    if float(line[indexDict['reach']]) <= 143:
                      arr.append('-1')
                    else:
                      if float(line[indexDict['reach']]) <= 148:
                        print('+1')
                      else:
                        if float(line[indexDict['age']]) <= 46:
                          arr.append('-1')
                        else:
                          arr.append('-1')
                  else:
                    if float(line[indexDict['bang length']]) <= 7:
                      if float(line[indexDict['tail length']]) <= 11:
                        if float(line[indexDict['age']]) <= 62:
                          if float(line[indexDict['reach']]) <= 141:
                            if float(line[indexDict['hair length']]) <= 8:
                              print('+1')
                            else:
                              arr.append('-1')
                          else:
                            arr.append('-1')
                        else:
                          print('+1')
                      else:
                        arr.append('-1')
                    else:
                      print('+1')
              else:
                if float(line[indexDict['hair length']]) <= 8:
                  if float(line[indexDict['tail length']]) <= 7:
                    arr.append('-1')
                  else:
                    if float(line[indexDict['reach']]) <= 156:
                      if float(line[indexDict['tail length']]) <= 8:
                        print('+1')
                      else:
                        arr.append('-1')
                    else:
                      if float(line[indexDict['tail length']]) <= 9:
                        arr.append('-1')
                      else:
                        print('+1')
                else:
                  if float(line[indexDict['tail length']]) <= 11:
                    print('+1')
                  else:
                    if float(line[indexDict['tail length']]) <= 14:
                      arr.append('-1')
                    else:
                      print('+1')
      else:
        if float(line[indexDict['bang length']]) <= 5:
          if float(line[indexDict['hair length']]) <= 11:
            if float(line[indexDict['tail length']]) <= 5:
              if float(line[indexDict['age']]) <= 40:
                print('+1')
              else:
                arr.append('-1')
            else:
              if float(line[indexDict['age']]) <= 68:
                if float(line[indexDict['bang length']]) <= 2:
                  arr.append('-1')
                else:
                  if float(line[indexDict['tail length']]) <= 16:
                    arr.append('-1')
                  else:
                    if float(line[indexDict['age']]) <= 60:
                      if float(line[indexDict['age']]) <= 46:
                        if float(line[indexDict['tail length']]) <= 18:
                          if float(line[indexDict['age']]) <= 42:
                            arr.append('-1')
                          else:
                            print('+1')
                        else:
                          arr.append('-1')
                      else:
                        arr.append('-1')
                    else:
                      print('+1')
              else:
                print('+1')
          else:
            if float(line[indexDict['height']]) <= 145:
              if float(line[indexDict['age']]) <= 58:
                if float(line[indexDict['height']]) <= 140:
                  if float(line[indexDict['age']]) <= 24:
                    arr.append('-1')
                  else:
                    print('+1')
                else:
                  if float(line[indexDict['reach']]) <= 146:
                    arr.append('-1')
                  else:
                    print('+1')
              else:
                arr.append('-1')
            else:
              if float(line[indexDict['height']]) <= 160:
                arr.append('-1')
              else:
                arr.append('-1')
        else:
          if float(line[indexDict['age']]) <= 48:
            if float(line[indexDict['reach']]) <= 157:
              if float(line[indexDict['height']]) <= 135:
                print('+1')
              else:
                if float(line[indexDict['bang length']]) <= 6:
                  if float(line[indexDict['tail length']]) <= 14:
                    arr.append('-1')
                  else:
                    if float(line[indexDict['height']]) <= 150:
                      print('+1')
                    else:
                      print('+1')
                else:
                  if float(line[indexDict['bang length']]) <= 7:
                    print('+1')
                  else:
                    if float(line[indexDict['tail length']]) <= 9:
                      arr.append('-1')
                    else:
                      print('+1')
            else:
              if float(line[indexDict['hair length']]) <= 11:
                arr.append('-1')
              else:
                if float(line[indexDict['age']]) <= 42:
                  arr.append('-1')
                else:
                  print('+1')
          else:
            if float(line[indexDict['bang length']]) <= 6:
              if float(line[indexDict['tail length']]) <= 13:
                arr.append('-1')
              else:
                if float(line[indexDict['height']]) <= 135:
                  arr.append('-1')
                else:
                  print('+1')
            else:
              if float(line[indexDict['tail length']]) <= 11:
                print('+1')
              else:
                if float(line[indexDict['tail length']]) <= 12:
                  arr.append('-1')
                else:
                  if float(line[indexDict['tail length']]) <= 15:
                    print('+1')
                  else:
                    arr.append('-1')
    else:
      if float(line[indexDict['bang length']]) <= 4:
        if float(line[indexDict['hair length']]) <= 9:
          if float(line[indexDict['tail length']]) <= 9:
            if float(line[indexDict['bang length']]) <= 2:
              arr.append('-1')
            else:
              if float(line[indexDict['age']]) <= 34:
                print('+1')
              else:
                if float(line[indexDict['age']]) <= 38:
                  if float(line[indexDict['hair length']]) <= 7:
                    arr.append('-1')
                  else:
                    arr.append('-1')
                else:
                  if float(line[indexDict['height']]) <= 140:
                    if float(line[indexDict['age']]) <= 50:
                      if float(line[indexDict['hair length']]) <= 7:
                        arr.append('-1')
                      else:
                        if float(line[indexDict['age']]) <= 44:
                          if float(line[indexDict['age']]) <= 42:
                            print('+1')
                          else:
                            arr.append('-1')
                        else:
                          print('+1')
                    else:
                      arr.append('-1')
                  else:
                    if float(line[indexDict['age']]) <= 54:
                      print('+1')
                    else:
                      if float(line[indexDict['age']]) <= 56:
                        arr.append('-1')
                      else:
                        print('+1')
          else:
            if float(line[indexDict['reach']]) <= 139:
              arr.append('-1')
            else:
              if float(line[indexDict['hair length']]) <= 7:
                if float(line[indexDict['hair length']]) <= 5:
                  print('+1')
                else:
                  if float(line[indexDict['height']]) <= 140:
                    if float(line[indexDict['age']]) <= 32:
                      print('+1')
                    else:
                      if float(line[indexDict['tail length']]) <= 14:
                        print('+1')
                      else:
                        arr.append('-1')
                  else:
                    arr.append('-1')
              else:
                if float(line[indexDict['tail length']]) <= 20:
                  if float(line[indexDict['age']]) <= 60:
                    if float(line[indexDict['height']]) <= 160:
                      if float(line[indexDict['age']]) <= 38:
                        print('+1')
                      else:
                        if float(line[indexDict['tail length']]) <= 11:
                          if float(line[indexDict['age']]) <= 52:
                            print('+1')
                          else:
                            arr.append('-1')
                        else:
                          if float(line[indexDict['bang length']]) <= 3:
                            arr.append('-1')
                          else:
                            if float(line[indexDict['height']]) <= 145:
                              if float(line[indexDict['age']]) <= 44:
                                print('+1')
                              else:
                                arr.append('-1')
                            else:
                              if float(line[indexDict['age']]) <= 44:
                                if float(line[indexDict['height']]) <= 150:
                                  arr.append('-1')
                                else:
                                  arr.append('-1')
                              else:
                                if float(line[indexDict['age']]) <= 52:
                                  print('+1')
                                else:
                                  print('+1')
                    else:
                      arr.append('-1')
                  else:
                    if float(line[indexDict['age']]) <= 62:
                      arr.append('-1')
                    else:
                      arr.append('-1')
                else:
                  if float(line[indexDict['height']]) <= 155:
                    arr.append('-1')
                  else:
                    arr.append('-1')
        else:
          if float(line[indexDict['bang length']]) <= 3:
            if float(line[indexDict['reach']]) <= 163:
              if float(line[indexDict['height']]) <= 125:
                print('+1')
              else:
                if float(line[indexDict['hair length']]) <= 10:
                  arr.append('-1')
                else:
                  arr.append('-1')
            else:
              print('+1')
          else:
            if float(line[indexDict['age']]) <= 62:
              if float(line[indexDict['tail length']]) <= 17:
                print('+1')
              else:
                if float(line[indexDict['height']]) <= 155:
                  if float(line[indexDict['reach']]) <= 152:
                    arr.append('-1')
                  else:
                    if float(line[indexDict['age']]) <= 22:
                      arr.append('-1')
                    else:
                      print('+1')
                else:
                  arr.append('-1')
            else:
              if float(line[indexDict['height']]) <= 140:
                arr.append('-1')
              else:
                print('+1')
      else:
        if float(line[indexDict['hair length']]) <= 8:
          if float(line[indexDict['tail length']]) <= 9:
            print('+1')
          else:
            if float(line[indexDict['reach']]) <= 138:
              if float(line[indexDict['age']]) <= 26:
                print('+1')
              else:
                if float(line[indexDict['tail length']]) <= 17:
                  if float(line[indexDict['age']]) <= 42:
                    if float(line[indexDict['tail length']]) <= 11:
                      if float(line[indexDict['age']]) <= 38:
                        if float(line[indexDict['hair length']]) <= 7:
                          arr.append('-1')
                        else:
                          arr.append('-1')
                      else:
                        print('+1')
                    else:
                      arr.append('-1')
                  else:
                    arr.append('-1')
                else:
                  print('+1')
            else:
              if float(line[indexDict['tail length']]) <= 15:
                if float(line[indexDict['reach']]) <= 141:
                  if float(line[indexDict['age']]) <= 46:
                    if float(line[indexDict['hair length']]) <= 6:
                      if float(line[indexDict['tail length']]) <= 11:
                        print('+1')
                      else:
                        arr.append('-1')
                    else:
                      print('+1')
                  else:
                    if float(line[indexDict['bang length']]) <= 6:
                      arr.append('-1')
                    else:
                      arr.append('-1')
                else:
                  if float(line[indexDict['height']]) <= 165:
                    print('+1')
                  else:
                    arr.append('-1')
              else:
                if float(line[indexDict['bang length']]) <= 5:
                  if float(line[indexDict['tail length']]) <= 18:
                    if float(line[indexDict['age']]) <= 44:
                      arr.append('-1')
                    else:
                      if float(line[indexDict['height']]) <= 135:
                        print('+1')
                      else:
                        if float(line[indexDict['height']]) <= 145:
                          arr.append('-1')
                        else:
                          if float(line[indexDict['reach']]) <= 162:
                            if float(line[indexDict['reach']]) <= 157:
                              if float(line[indexDict['tail length']]) <= 16:
                                arr.append('-1')
                              else:
                                print('+1')
                            else:
                              print('+1')
                          else:
                            arr.append('-1')
                  else:
                    if float(line[indexDict['age']]) <= 40:
                      if float(line[indexDict['height']]) <= 145:
                        print('+1')
                      else:
                        arr.append('-1')
                    else:
                      if float(line[indexDict['height']]) <= 165:
                        if float(line[indexDict['height']]) <= 140:
                          arr.append('-1')
                        else:
                          arr.append('-1')
                      else:
                        print('+1')
                else:
                  if float(line[indexDict['age']]) <= 60:
                    if float(line[indexDict['height']]) <= 160:
                      if float(line[indexDict['hair length']]) <= 4:
                        arr.append('-1')
                      else:
                        if float(line[indexDict['age']]) <= 48:
                          print('+1')
                        else:
                          if float(line[indexDict['hair length']]) <= 6:
                            arr.append('-1')
                          else:
                            if float(line[indexDict['tail length']]) <= 18:
                              if float(line[indexDict['reach']]) <= 149:
                                if float(line[indexDict['age']]) <= 56:
                                  if float(line[indexDict['height']]) <= 140:
                                    arr.append('-1')
                                  else:
                                    print('+1')
                                else:
                                  print('+1')
                              else:
                                print('+1')
                            else:
                              print('+1')
                    else:
                      arr.append('-1')
                  else:
                    arr.append('-1')
        else:
          print('+1')
