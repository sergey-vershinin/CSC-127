#Name: Sergey Vershinin
#Date: 10/25/2018
#This program name top three Contributing factors for the primary vehichle of a collision:


import pandas as pd

inFile = input ("Enter CSV file name: ") #NYPD_Motor_Vehicle_Collisions.csv

collisions = pd.read_csv(inFile) #convert csv in pandas

print("Top three contributing factors for collisions: ")

#print 3 main factors
print(collisions["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
