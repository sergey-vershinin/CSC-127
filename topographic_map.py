#Sergey Vershinin
#09.21.2018
#This program takes elevation data of NYC
#and displays uding the default color map
#Modified 10/05/18

#import first the libraries for arrays and displaying images:

import numpy as np
import matplotlib.pyplot as plt

#read the data to an array, called elevations:

elevations = np.loadtxt('elevationsNYC.webarchive.txt')


#take the shape (dimentions) of the elevstions
#and add 3rd dimention to hold the color channels

mapShape = elevations.shape + (3, )

#creat the blank image that's all zeros:

topo = np.zeros(mapShape)
for row in range(mapShape[0]):
     for col in range(mapShape[1]):
         if  elevations[row,col] <=0:       #below sea level
             topo[row,col,2] = 0.25    #set the blue channel to 100%
         elif elevations[row,col] %10==0:  #below the storm surge of Hurricane Sandy(flooding likely)
              topo[row,col,0] = 0       #set the red channel to 100%
              topo[row,col,1] = 0
              topo[row,col,2] = 0
         else:                            
             topo[row,col,0] = 0.5       
             topo[row,col,1] = 0.5
             topo[row,col,2] = 0.5

plt.imshow(topo)

#Display the plot
plt.show()

#Save the image:
plt.imsave('topo.png' , topo)
