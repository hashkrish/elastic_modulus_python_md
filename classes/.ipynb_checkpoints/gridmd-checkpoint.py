
# coding: utf-8
from .constantsmd import *
from .gridmd import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import time
#import sympy as sy
#sy.init_printing()
print("called gridmd")

def __init__():
    #initializaztion
    pass

def xyzGrid(x,y,z):
    x_y_z = np.empty([x.size,y.size,z.size,3])

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                x_y_z[i][j][k][0]=x[i]
                x_y_z[i][j][k][1]=y[j]
                x_y_z[i][j][k][2]=z[k]
    return x_y_z

def xyz(x,y,z):
    x_y_z = np.empty([x.size,y.size,z.size])

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                x_y_z[i][j][k]=x[i]
                x_y_z[i][j][k]=y[j]
                x_y_z[i][j][k]=z[k]
    return x_y_z

def xy(x,y):
    x_y = np.empty([x.size,2])

    for i in range(x.size):
        x_y_z[i][j]=x[i]
    for j in range(y.size):
        x_y_z[i][j]=y[j]
    return x_y

def N_xyz(Nx,Ny,Nz): 
    #defining number of atoms along x, y and z axis
    return np.array([Nx,Ny,Nz])

def initialPos(N,ial):

    X=(N[0]-1) * ial
    Y=(N[1]-1) * ial
    Z=(N[2]-1) * ial

    x_coor_0 = np.empty(N[0])
    for i in range(N[0]):
        x_coor_0[i] = (-X/2)+(i*ial)
    y_coor_0 = np.empty(N[1])
    for i in range(N[1]):
        y_coor_0[i] = (-Y/2)+(i*ial)
    z_coor_0 = np.empty(N[2])
    for i in range(N[2]):
        z_coor_0[i] = (-Z/2)+(i*ial)

    return np.array([x_coor_0,y_coor_0,z_coor_0])