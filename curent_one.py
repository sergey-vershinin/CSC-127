#Name: Sergey Vershinin
#Date: 10/25/2018
#This program name top three Contributing factors for the primary vehichle of a collision:


import pandas as pd
import folium 

inFile = input("Enter CSV file name: ") #NYPD_Motor_Vehicle_Collisions.csv

collisions = pd.read_csv(inFile) #convert csv in pandas

#print(collisions["TIME"])

outfile= input("Enter output file: ")

mapNYC = folium.Map(location=[40.768731, -73.964915])

for index, row in collisions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name=row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(outfile) 
