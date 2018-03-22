
# coding: utf-8
from .constantsmd import *
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

def xyzGridFCC(x,y,z,xf,yf,zf):
    x_y_z = np.empty([x.size*2,y.size*2,z.size*2,3])

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                x_y_z[i][j][k][0]=x[i]
                x_y_z[i][j][k][1]=y[j]
                x_y_z[i][j][k][2]=z[k]
                x_y_z[i+x.size-1][j][k][3]=xf[i]
                x_y_z[i][j+y.size-1][k][4]=yf[j]
                x_y_z[i][j][k+z.size-1][5]=zf[k]
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

def N_xyz(Nx,Ny,Nz): 
    #defining number of atoms along x, y and z axis
    return np.array([Nx,Ny,Nz])

def initialPosSC(N,ial):

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

def initialPosFCC(N,ial):

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

    x_coor_0f = np.empty(N[0])
    for i in range(N[0]):
        x_coor_0f[i] = (-X/2)+(i*ial)+ial/2
    y_coor_0f = np.empty(N[1])
    for i in range(N[1]):
        y_coor_0f[i] = (-Y/2)+(i*ial)+ial/2
    z_coor_0f = np.empty(N[2])
    for i in range(N[2]):
        z_coor_0f[i] = (-Z/2)+(i*ial)+ial/2

    return np.array([x_coor_0 ,y_coor_0 ,z_coor_0, x_coor_0f, y_coor_0f, z_coor_0f])

def plotStructureUnitCell(brick):
    length = 1
    fig0 = plt.figure()
    ax = fig0.add_subplot(111, projection='3d')
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(brick[i, j, k] == 1):
                    ax.scatter(length * i, length * j, length * k, c='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def plotStructure(mat):
    length = 1
    fig0 = plt.figure()
    ax = fig0.add_subplot(111, projection='3d')
    for i in range(mat[:,0,0].size):
        for j in range(mat[0,:,0].size):
            for k in range(mat[0, 0, :].size):
                if(mat[i, j, k] == 1):
                    ax.scatter(length * i, length * j, length * k, c='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def plotPosGrid(mat):
    fig0 = plt.figure()
    ax = fig0.add_subplot(111, projection='3d')
    for i in range(mat[:, 0, 0, 0].size):
        for j in range(mat[0, :, 0, 0].size):
            for k in range(mat[0, 0, :, 0].size):
                ax.scatter(mat[i, j ,k, 0], mat[i, j ,k, 1], mat[i, j ,k, 2], c='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def makeLattice(brick, na1, na2, na3):
    xnet = brick
    for i in range(na1-1):
        xnet = np.concatenate((xnet, brick[1:, :, :]), axis=0)
    xynet = xnet
    for j in range(na2-1):
        xynet = np.concatenate((xynet, xnet[:, 1:,:]), axis=1)
    xyznet = xynet
    for k in range(na3-1):
        xyznet = np.concatenate((xyznet, xynet[:, :, 1:]), axis=2)
    return xyznet

def makeLatticePos(brick, na1, na2, na3, ial, ialX=0, ialY=0, ialZ=0):
    if ialX==0:
        ialX=ial
    if ialY==0:
        ialY=ial
    if ialZ==0:
        ialZ==ial

    xnet = brick
    for i in range(na1-1):
        xnet = np.concatenate((xnet, brick[1:, :, :]), axis=0)
    xynet = xnet
    for j in range(na2-1):
        xynet = np.concatenate((xynet, xnet[:, 1:,:]), axis=1)
    xyznet = xynet
    for k in range(na3-1):
        xyznet = np.concatenate((xyznet, xynet[:, :, 1:]), axis=2)
    xyzPosGrid = np.zeros([xyznet[:,0,0].size, xyznet[0,:,0].size, xyznet[0, 0, :].size, 3])
    try:
        for i in range(xyznet[:,0,0].size):
            for j in range(xyznet[0,:,0].size):
                for k in range(xyznet[0, 0, :].size):
                    if(xyznet[i, j, k] == 1):
                        xyzPosGrid[i, j, k] = np.array([ialX*i, ialY*j, ialZ*k])
    except:
        print("error at:",i,j,k)
        print(xyznet.shape)
    return xyzPosGrid

    