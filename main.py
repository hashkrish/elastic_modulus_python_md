#this is the main file


#importing required libraries
from datetime import datetime
startTime = datetime.now()
print("-----------start-----------")

from classes import gridmd, functionsmd
from numpy import sin, cos, deg2rad, matrix, size, invert, multiply, array, empty, zeros, ones

#from matplotlib.pyplot import plot
#import matplotlib.pyplot as plt
#from sympy import init_printing
#from mpl_toolkits.mplot3d import Axes3D
#import csv
#import pandas as pd


ial = 1.02e-10 #interatomic length

N = gridmd.N_xyz(100,6,6)
coor_0 = gridmd.initialPos(N,ial)
xyz_grid = gridmd.xyz_grid(coor_0[0], coor_0[1], coor_0[2])




















print(datetime.now() - startTime)
print("------------end------------")