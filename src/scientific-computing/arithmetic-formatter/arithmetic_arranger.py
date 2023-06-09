def arithmetic_arranger(problems, isAnswered=False):
  typeError = 0 #If non digits are provided
  valueError = 0 #If digits exceed 4
  operandError = 0 #If an operand other than + or - appears
  lengthError = 0 #If problems is more then 5
  arranged_problems = 'An uknown error has occured'
  if len(problems) > 5:
    lengthError = 1
  else:
    arrangedValuesX = []
    arrangedValuesY = []
    arrangedValuesF = []
    arrangedDash = []
    x = -1
    
    for operation in problems:
      x += 1
      arrangedDash.insert(x, "")
      arrangedValuesY.insert(x, "")
      arrangedValuesX.insert(x, "")
      arrangedValuesF.insert(x, "")
      
      #Seperating, X, Y, and operands to perform operations
      if '+' in operation:
        values = operation.replace(" ","").split('+')
        parseX = values[0]
        parseY = values[1]
        if not values[0].isnumeric() or not values[1].isnumeric():
          typeError = 1
        elif int(parseX) > 9999 or int(parseY) > 9999:
          valueError = 1
        else:
          parseX = int(parseX)
          parseY = int(parseY)
          xLength = len(values[0])
          yLength = len(values[1])
          #Checking lengths to determine spaces needed between operand and dashes for solution
          if xLength > yLength:
            for i in range(xLength + 2):
              arrangedDash[x] += '-'
            arrangedValuesY[x] = '+'
            for i in range(xLength - yLength):
              arrangedValuesX[x] += ' '
              arrangedValuesY[x] += ' '
            arrangedValuesX[x] =  "  " + str(parseX)
            arrangedValuesY[x] += ' ' + str(parseY)
            for i in range(xLength - len(str(parseX + parseY)) + 2):
              arrangedValuesF[x] += " "
          else:
            for i in range(yLength + 2):
              arrangedDash[x] += '-'
            arrangedValuesY[x] = '+'
            for i in range(yLength - xLength):
              arrangedValuesX[x] += ' '
            arrangedValuesX[x] +=  "  " + str(parseX)
            arrangedValuesY[x] += ' ' + str(parseY)
            for i in range(yLength - len(str(parseX + parseY)) + 2):
              arrangedValuesF[x] += " "
          #Storing the solved value, for if the second function parameter is True
          arrangedValuesF[x] += str(parseX + parseY)
          
            
      #Complete replication of above code. + is substituted for -
      elif '-' in operation:
        values = operation.replace(" ","").split('-')
        parseX = values[0]
        parseY = values[1]
        if not values[0].isnumeric() or not values[1].isnumeric():
          typeError = 1
        elif int(parseX) > 9999 or int(parseY) > 9999:
          valueError = 1
        else:
          parseX = int(parseX)
          parseY = int(parseY)
          xLength = len(values[0])
          yLength = len(values[1])
          if xLength > yLength:
            for i in range(xLength + 2):
              arrangedDash[x] += '-'
            arrangedValuesY[x] = '-'
            for i in range(xLength - yLength):
              arrangedValuesY[x] += ' '
            arrangedValuesX[x] +=  "  " + str(parseX)
            arrangedValuesY[x] += ' ' + str(parseY)
            for i in range(xLength - len(str(parseX + parseY))):
              arrangedValuesF[x] += ' '
            for i in range(len(str(parseX + parseY)) - xLength + 1):
              arrangedValuesF[x] += " "
          else:
            for i in range(yLength + 2):
              arrangedDash[x] += '-'
            arrangedValuesY[x] = '-'
            for i in range(yLength - xLength):
              arrangedValuesX[x] += ' '
            for i in range(yLength - len(str(parseX + parseY))):
              arrangedValuesF[x] += ' '
            arrangedValuesX[x] +=  "  " + str(parseX)
            arrangedValuesY[x] += ' ' + str(parseY)
            for i in range(len(str(parseX + parseY)) - yLength + 1):
              arrangedValuesF[x] += " "
          arrangedValuesF[x] += str(parseX - parseY)

      #If neither of the above are called, there is an incorrect operand being used
      else:
        operandError = 1
        
  #Each loop iteration contains an operand check in the list
  if operandError == 1:
    arranged_problems = "Error: Operator must be '+' or '-'."
  elif typeError == 1:
    arranged_problems = "Error: Numbers must only contain digits."
  elif valueError == 1:
    arranged_problems = "Error: Numbers cannot be more than four digits."
  elif lengthError == 1:
    arranged_problems = "Error: Too many problems."
  else:
    #Organize our parsed data into strings
    arranged_problems = ""
    arranged_problems += arrangedValuesX[0]
    for i in range(1, len(arrangedValuesX)):
      arranged_problems += "    " + arrangedValuesX[i]
    arranged_problems += "\n"
    arranged_problems += arrangedValuesY[0]
    for i in range(1, len(arrangedValuesY)):
     arranged_problems += "    " + arrangedValuesY[i]
    arranged_problems += "\n"
    arranged_problems += arrangedDash[0]
    for i in range(1, len(arrangedDash)):
     arranged_problems += "    " + arrangedDash[i]
    #We check to see if the user wants to output results
    if isAnswered == 1:
      arranged_problems += "\n"
      arranged_problems += arrangedValuesF[0]
      for i in range(1, len(arrangedValuesF)):
        arranged_problems += "    " + arrangedValuesF[i]

  print(arranged_problems)
  return arranged_problems