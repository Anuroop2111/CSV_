import csv
import re
import numpy as np
import urllib.parse



rows = []

dictionary = {
  "USD":76,
  "GBP":100,
  "YEN":0.65
}


with open('test_1.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    parent = []
    for row in lines:
      newArray = []
      newArray.append(eval(row[0]))
      [arr1,operand,arr2] = (re.split(r"(-|\+)",row[1]))
      npArr1 = np.array(eval(arr1))
      npArr2 = np.array(eval(arr2))
      if(operand == "+"):
        result = npArr1 + npArr2
      if(operand == "-"):
        result = npArr1 - npArr2
      newArray.append(result)
      parsed_url = urllib.parse.urlparse(row[2])
      newArray.append(parsed_url.netloc)
      [currency1,operator,currency2] = (re.split(r"(-|\+)",row[3]))
      currencyType1 = currency1.replace(" ","")[-3:]
      currencyType2 = currency2.replace(" ","")[-3:]
      if(currencyType1 == "USD"):
        currencyPrice1 = 76
      elif(currencyType1 == "GBP"):
        currencyPrice1 = 100
      elif(currencyType1 == "YEN"):
        currencyPrice1 = 0.65

      if(currencyType2 == "USD"):
        currencyPrice2 = 76
      elif(currencyType2 == "GBP"):
        currencyPrice2 = 100
      elif(currencyType2 == "YEN"):
        currencyPrice2 = 0.65
      
  
      currencyValue1 = currency1[:-5]
      currencyValue2 = currency2[:-5]
      
      currency1Rupee = float(currencyValue1)*(currencyPrice1)
      currency2Rupee =float(currencyValue2)*(currencyPrice2)

      if(operator == "+"):
        result2 = currency1Rupee + currency2Rupee
      if(operator == "-"):
        result2 = currency1Rupee - currency2Rupee
      newArray.append(result2)
      parent.append(newArray)
print(parent)

        
        
        

