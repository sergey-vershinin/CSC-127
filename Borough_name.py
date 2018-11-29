#Sergey Veshinin
#10/05/18

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd


#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#ask user for a borough name
boroughName=input("Enter borough name: ")
outputName = input("Enter output file name: ")

                   

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[boroughName]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y='Fraction')
#plt.show()
#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(outputName)
