#this is the main file


#importing required libraries
from classes import gridmd, functionsmd
from numpy import sin, cos, deg2rad, matrix, size, invert, multiply, array, empty, zeros

#from matplotlib.pyplot import plot
#import matplotlib.pyplot as plt
#from sympy import init_printing
#from mpl_toolkits.mplot3d import Axes3D
#import csv
#import pandas as pd
print("-----------start-----------")

ial = 1.02e-10 #interatomic length

N = gridmd.N_xyz(100,6,6)
coor_0 = gridmd.initialPos(N,ial)




















print("------------end------------")