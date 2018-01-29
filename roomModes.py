#This program takes the distance between two paralell walls
#as an argument, and returns a graph showing the room modes
#within the given area.

#Importing nessicary materials
import matplotlib.pyplot as plt
import numpy as np
import math


#Taking user input to determine the area being evaluated,
#and the units that should be used for evaluation.
wallDist=input("Enter the distance between two paralell walls in the room: ")
wallDist=float(wallDist) #Distance between paralell walls
units=input("Is the measurement in feet or meters? (Enter f for feet, and m for meters): ")


#Setting up units of measurement based off of user input
if units == "f":
    v=1125.33 #Setting value for speed of sound
elif units == "m":
    v=343 #Setting value for speed of sound
else:    #If f or m is not entered, user is prompted to resubmit either m or f
    print("Please enter either m or f to indicate units.")
    units=input("Is the measurement in feet or meters? (Enter f for feet, and m for meters): ")


#This section calculates the axial room modes (between paralell walls)
axialW = range(1,21) #Sets the number of harmonics to be calculated (x axis)
axialF = [] #List of frequencies where room modes reside
axialWave = []
v = v/2

for i in range(1,21):
    axialF.append(v*math.sqrt(wallDist**2/i**2)) #Calculating and appending room modes to list axialF

#Generating graph of room mode frequency vs harmonic number
plt.scatter(axialW, axialF)
plt.ylabel('Frequency (Hz)')
plt.xlabel('Harmonic Number)
plt.show()

#for f in axialF:
 #   axialWave.append(abs(math.sin(2*math.pi*f)))

#print(axialF)
