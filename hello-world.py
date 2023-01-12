# print("Hello, World")

# print("Python has three numeric types: int, float, and complex")

# myValue = 1

# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))

# myValue = 3.14
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))

# myValue = 5j
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))

# myValue=True
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))

# myString = "This is a string."
# print(myString)
# print(type(myString))
# print(myString + " is of the data type " + str(type(myString)))

# firstString = "water"
# secondString = "fall"
# thirdString = firstString + secondString
# print(thirdString)

# name = input("What is your name? ")
# print(name)

# color = input("What is your favorite color?  ")
# animal = input("What is your favorite animal?  ")
# print("{}, you like a {} {}!".format(name,color,animal))

# myFruitList = ["apple", "banana", "cherry"]
# print(myFruitList)
# print(type(myFruitList))

# print(myFruitList[0])
# print(myFruitList[1])
# print(myFruitList[2])

# myFruitList[2] = "orange"
# print(myFruitList)

# myFinalAnswerTuple = ("apple", "banana", "pineapple")
# print(myFinalAnswerTuple)
# print(type(myFinalAnswerTuple))
# print(myFinalAnswerTuple[0])

# myFavoriteFruitDictionary = {
#   "Akua" : "apple",
#   "Saanvi" : "banana",
#   "Paulo" : "pineapple"
# }
# print(myFavoriteFruitDictionary)
# print(type(myFavoriteFruitDictionary))

# print(myFavoriteFruitDictionary["Akua"])
# import random
# myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# random_num = random.choice(myMixedTypeList)

# for random_num in myMixedTypeList:
#     print("{} is of the data type {}".format(random_num,type(random_num)))

import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
    
myInventoryList = []


with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")


