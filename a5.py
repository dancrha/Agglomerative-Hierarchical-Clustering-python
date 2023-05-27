'''
CP467 Assignment 5 - Measuring Distances

Created on Nov. 13, 2022

References
https://stackoverflow.com/questions/48887912/find-minimum-distance-between-points-of-two-lists-in-python

'''
import math

#Minimum distance between two points
import numpy as np
from scipy.spatial import distance

s1 = np.array([(1,1), (1,2)])
s2 = np.array([(2,1), (3,1)])
sDistance = distance.cdist(s1,s2)

print("Minimum distance: ")
print(sDistance.min())

#Maximum distance between two points

print("\nMaximum distance: ")
print(sDistance.max())

#Average distance between points

print("\nAverage distance: ")
print(sDistance.mean())

#Mean distance between points
print("\nMean distance: ")
print()
