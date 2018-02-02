#This program takes the dimensions of the room as
#an argument, and returns the axial, room modes
#within that given area via graph.

#Importing nessicary materials
import matplotlib.pyplot as plt
import numpy as np
import math


#Taking user input to determine the area being evaluated,
# the units that should be used for evaluation, and the
#number of room modes to be calculated.
length=input("Enter the length of the room: ")
width=input("Enter the width of the room: ")
height=input("Enter the height of the room: ")
harmonic=input("Number of harmonics to calculate: ")
harmonic=int(harmonic)#Value for number of harmonics
length=float(length) #Value for length as float
width=float(width) #Value for width as float
height=float(height) #Value for height as float
units=input("Is the measurement in feet or meters? (Enter f for feet, and m for meters): ")

#Setting up units for speed of sound based off of user input
if units == "f":
    c=1125.33 #Feet per second (speed of sound)
elif units == "m":
    c=343 #Meters per second (speed of sound)
else:    #If f or m is not entered, user is prompted to resubmit either m or f
    print("Please enter either m or f to indicate units.")
    units=input("Is the measurement in feet or meters? (Enter f for feet, and m for meters): ")



#This section calculates the axial room modes (between paralell walls)
axialN = range(1,harmonic+1) #Sets the number of harmonics to be calculated (x axis)
axialL = [] #List of room modes created as a result of room length
axialW = [] #List of room modes created as a result of room width
axialH = [] #List of room modes created as a result of room height
axialAll = [] #List of all axial modes (for histogram)
v = c/2 #Adjusting speed of sound for equation

for i in range(1,harmonic+1):
    axialL.append(v*math.sqrt(i**2/length**2)) #Calculating and appending room modes to list axialL
    axialW.append(v*math.sqrt(i**2/width**2)) #Calculating and appending room modes to list axialW
    axialH.append(v*math.sqrt(i**2/height**2)) #Calculating and appending room modes to list axialH

#Appending to a list to store all axial modes
for f in axialL:
    axialAll.append(f)
for f in axialW:
    axialAll.append(f)
for f in axialH:
    axialAll.append(f)


#Generating scatterplot of axial room modes with frequency vs harmonic number
plt.scatter(axialN, axialL, label="Length ") #Plotting length modes
plt.scatter(axialN, axialW, label="Width") #Plotting width modes
plt.scatter(axialN, axialH, label="Height") #Plotting height modes
plt.title('Axial Modes')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Harmonic Number')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

#Generating histogram of axial room modes grouped to frequency bands
bins = np.linspace(math.ceil(min(axialAll)),
                   math.floor(max(axialAll)),
                   20) # fixed number of bins
plt.xlim([0, max(axialAll)+5])
plt.hist(axialAll, bins=bins, alpha=0.5)
plt.title('Axial Modes Per Frequency Range (fixed number of groups)')
plt.xlabel('Frequency Range (20 Groups)')
plt.ylabel('Number of Modes')

plt.show()
