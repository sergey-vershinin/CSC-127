#Name: Sergey Vershinin
#Date: 10/17/2018
#This program loads a program, displays it and then creates and displays
#a new imagethat is only lower left corner.

import matplotlib.pyplot as plt
import numpy as np

Name = input("Enter image file name: ")
OutputName = input("Enter output file: ")

img = plt.imread(Name) #read an img from .png file
plt.imshow(img)  #load img into pyplot
plt.show()

#specify the height and width of the new image

height= img.shape[0] #get height
width= img.shape[1]  #get width

img2 = img[int(height/2):, :int(width/2)]    #copy img and create img2

plt.imshow(img2)
plt.show()
plt.imsave(OutputName, img2)
