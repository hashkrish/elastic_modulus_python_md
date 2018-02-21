#this is the main file
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

#importing required libraries
import functionsmd
from numpy import sin, cos, deg2rad, matrix, size, invert, multiply, array
import gridmd

from matplotlib.pyplot import plot
import matplotlib.pyplot as plt
#from sympy import init_printing
from mpl_toolkits.mplot3d import Axes3D
import csv
import pandas as pd


ial = 1.02e-10 #interatomic length


print(gridmd.NN_xyz(100,20,20))

print(functionsmd.printhello())


















"""
for i in x:
    for j in y:
        plt.scatter(i,j,c='b')
plt.show()


fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
for i in x:
    for j in y:
        for k in z:
            ax.scatter(i,j,k,c='b')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

"""