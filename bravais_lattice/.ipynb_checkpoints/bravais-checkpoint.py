import sys;sys.path.append('/home/krish/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np

from classes.constantsmd import *
from classes.functionsmd import bravais, forceLJ3, verlet_pos
from classes.gridmd import N_xyz
# a = 1
# nx, ny, nz = 10, 10, 10
# a1 = np.array([0.0, 0.5, 0.5])*a
# a2 = np.array([0.5, 0.0, 0.5])*a
# a3 = np.array([0.5, 0.5, 0.0])*a

# outputFile = open('bravais_lattice/sc.xyz','w')

# outputFile.write(str(nx*ny*nz)+'\n')
# outputFile.write('\n')

# for n1 in range(nx):
#     for n2 in range(ny):
#         for n3 in range(nz):
#             R = n1*a1 + n2*a2 + n3*a3
#             print(R)
#             outputFile.write('X ' + str(R[0]) + ' ' + str(R[1]) + ' ' + str(R[2]) + '\n' ) 
# outputFile.close()

def writeXYZFile(posGrid, path='None', scale='None'):
    if scale=='Angstrom':
        posGrid = posGrid/1e-10
    if path=='None':
        outputFile = open('bravais_lattice/xyzFile.xyz','w')
    else:
        outputFile = open(path,'w')
    outputFile.write(str(posGrid.shape[0]*posGrid.shape[1]*posGrid.shape[2])+'\n')
    outputFile.write('\n')

    for n1 in range(posGrid.shape[0]):
        for n2 in range(posGrid.shape[1]):
            for n3 in range(posGrid.shape[2]):
                R = posGrid[n1, n2, n3]
                outputFile.write('X ' + str(R[0]) + ' ' + str(R[1]) + ' ' + str(R[2]) + '\n' ) 
    outputFile.close()    

def Force(posGrid):
    N[0] = posGrid.shape[0]
    N[1] = posGrid.shape[1]
    N[2] = posGrid.shape[2]
    force = np.zeros([N[0], N[1], N[2],3])
    for i in range(N[0]):
        for j in range(N[1]):
            for k in range(N[2]):
                fx=0; fy=0; fz=0
                fx = forceLJ3(i, j, k, posGrid)[0]
                fy = forceLJ3(i, j, k, posGrid)[1]
                fz = forceLJ3(i, j, k, posGrid)[2]
                force[i, j, k, 0] = fx
                force[i, j, k, 1] = fy
                force[i, j, k, 2] = fz
    return force

def defForce2D(force_grid, X=0, Y=0, Z=0):
    shapeX = force_grid.shape[0]
    shapeY = force_grid.shape[1]
    shapeZ = force_grid.shape[2]
    if X!=0:
        for j in range(shapeY):
            for k in range(shapeZ):
                force_grid[0,j,k,0] = -X/shapeY/shapeZ
                force_grid[shapeX-1,j,k,0] =  X/shapeY/shapeZ                
    if Y!=0:
        for i in range(shapeX):
            for k in range(shapeZ):
                force_grid[i,0,k,1] = -Y/shapeX/shapeZ
                force_grid[i,shapeY-1,k,1] = Y/shapeX/shapeZ
    if Z!=0:
        for i in range(shapeX):
            for j in range(shapeY):
                force_grid[i,j,0,2] = -Z/shapeY/shapeX
                force_grid[i,j,shapeZ-1,2] = Z/shapeY/shapeX
    return force_grid
                








