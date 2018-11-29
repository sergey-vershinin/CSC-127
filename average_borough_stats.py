#Sergey Veshinin
#10/05/18
#this program computes the average and maximum population




#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd


#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#ask user for a borough name
boroughName=input("Enter borough name: ")

#Print the average populatin for asked borough:
print("Average population:", pop[boroughName].mean())

#Print the maximum populatin:
print("Maximum population:", pop[boroughName].max())


