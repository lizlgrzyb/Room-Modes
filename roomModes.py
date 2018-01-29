#This program takes the dimensions of the room as
#and argument, and returns the axial, tangential,
#and oblique room modes within that given area via
#graph.

#Importing nessicary materials
import matplotlib.pyplot as plt
import numpy as np
import math


#Taking user input to determine the area being evaluated,
#and the units that should be used for evaluation.
length=input("Enter the length of the room: ")
width=input("Enter the width of the room: ")
height=input("Enter the height of the room: ")
length=float(length) #Value for length as float
width=float(width) #Value for width as float
height=float(height) #Value for height as float
units=input("Is the measurement in feet or meters? (Enter f for feet, and m for meters): ")


#Setting up units for speed of sound based off of user input
if units == "f":
    v=1125.33 #Feet per second
elif units == "m":
    v=343 #Meters per second
else:    #If f or m is not entered, user is prompted to resubmit either m or f
    print("Please enter either m or f to indicate units.")
    units=input("Is the measurement in feet or meters? (Enter f for feet, and m for meters): ")


#This section calculates the axial room modes (between paralell walls)
axialN = range(1,21) #Sets the number of harmonics to be calculated (x axis)
axialL = [] #List of room modes created as a result of room length
axialW = [] #List of room modes created as a result of room width
axialH = [] #List of room modes created as a result of room height
v = v/2

for i in range(1,21):
    axialL.append(v*math.sqrt(length**2/i**2)) #Calculating and appending room modes to list axialF
    axialW.append(v*math.sqrt(width**2/i**2))
    axialH.append(v*math.sqrt(height**2/i**2))


#Generating graph of room mode frequency vs harmonic number
plt.scatter(axialN, axialL, label="Length") #Plotting length modes
plt.scatter(axialN, axialW, label="Width") #Plotting width modes
plt.scatter(axialN, axialH, label="Height") #Plotting height modes
plt.title('Axial Modes')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Harmonic Number')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

#for f in axialF:
 #   axialWave.append(abs(math.sin(2*math.pi*f)))

#print(axialF)
