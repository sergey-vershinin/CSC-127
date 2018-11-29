#Sergey Vershinin
#09.21.2018
#This program takes elevation data of NYC
#and displays uding the default color map

#import first the libraries for arrays and displaying images:

import numpy as np
import matplotlib.pyplot as plt

#read the data to an array, called elevations:

elevations = np.loadtxt('elevationsNYC.txt')


#take the shape (dimentions) of the elevstions
#and add 3rd dimention to hold the color channels

mapShape = elevations.shape + (3, )

#creat the blank image that's all zeros:

floodMap = np.zeros(mapShape)
for row in range(mapShape[0]):
     for col in range(mapShape[1]):
         if elevations[row,col] <=0:    #below sea level
             floodMap[row,col,2] = 1.0  #set the blue channel to 100%
         elif elevations[row,col] <=6: #below the storm surge of Hurricane Sandy(flooding likely)
         elif elevations[row,col]<=20: #in range of (6,20) ft
             floodMap[row,col,0] = 0.5 #set red to 50%
             floodMap[row,col,1] = 0.5 #set the green to 50%
             floodMap[row,col,2] = 0.5 #set the blue channel to 50%
             floodMap[row,col,0] = 1.0 #set the red channel to 100%
         else:                          #above the 6 foot storm surge
             floodMap[row,col,1] = 1.0 #set the green channel to 100%

#load the flood map image into matplotlib.pyplot:

plt.imshow(floodMap)

#Display the plot
plt.show()

#Save the image:
plt.imsave('floodMap.png' , floodMap)
