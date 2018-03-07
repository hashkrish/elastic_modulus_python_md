
#%%
import sys
sys.path.append('/home/krish/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np

from classes.constantsmd import *
from classes.functionsmd import (forceLJ3FCC, forceXLJ3, forceYLJ3, forceZLJ3, verlet_pos,
                                 writeXYZFile, numberOfAtoms)
from classes.gridmd import (N_steps, makeLattice, makeLatticePos, plotPosGrid,
                            plotStructure)








brick = np.array([
    [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ],

    [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ],

    [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ] ])
#brick = np.multiply(0.5,brick)
N = np.array([3, 3, 3])
#%%
latticeGrid = makeLattice(brick, N[0], N[1], N[2])
posGrid = makeLatticePos(brick, N[0], N[1], N[2], ial/2)
#writeXYZFile(latticeGrid, posGrid,name='temp.xyz')
#plotPosGrid(posGrid)
#%%
N[0] = posGrid.shape[0]
N[1] = posGrid.shape[1]
N[2] = posGrid.shape[2]

time_grid = np.zeros([N_steps,N[0],N[1],N[2],3])
time_grid[0] = np.array([posGrid])

force_grid = np.zeros([N_steps, N[0], N[1], N[2],3])
for t in range(N_steps - 1):
    file = open("dump/pos/timestep_"+str(t+1)+".xyz", "w")
    file.write(str(numberOfAtoms(latticeGrid))+'\n')
    file.write('\n')
    for i in range(N[0]):
        for j in range(N[1]):
            for k in range(N[2]):
                if (latticeGrid[i, j, k] == 1):
                    fx=0; fy=0; fz=0;acc=0
                    fx = forceLJ3FCC(i, j, k, posGrid, latticeGrid)[0]
                    fy = forceLJ3FCC(i, j, k, posGrid, latticeGrid)[1]
                    fz = forceLJ3FCC(i, j, k, posGrid, latticeGrid)[2]
                    #fx, fy, fz += forceLJ3(i, j, k, posGrid)
                    acc = (fx/mass) + (force_grid[t, i, j, k , 0]/mass)
                    if (t-1==-1):
                        xj=verlet_pos(time_grid[t][i][j][k][0], time_grid[t][i][j][k][0], t,ts,acc)
                        yj=verlet_pos(time_grid[t][i][j][k][1], time_grid[t][i][j][k][1], t, ts, 
                                        fy/mass)
                        zj=verlet_pos(time_grid[t][i][j][k][2], time_grid[t][i][j][k][2], t, ts, 
                                        fz/mass)
                    else:
                        xj=verlet_pos(time_grid[t][i][j][k][0], time_grid[t-1][i][j][k][0], t,ts,acc)
                        yj=verlet_pos(time_grid[t][i][j][k][1], time_grid[t-1][i][j][k][1], t, ts, 
                                    fy/mass)
                        zj=verlet_pos(time_grid[t][i][j][k][2], time_grid[t-1][i][j][k][2], t, ts, 
                                    fz/mass)
                    time_grid[t+1][i][j][k][0] = xj
                    time_grid[t+1][i][j][k][1] = yj
                    time_grid[t+1][i][j][k][2] = zj
                    file.write('X '+str(xj)+' '+str(yj)+' '+str(zj)+'\n')
                    force_grid[t][i][j][k][0] = fx;force_grid[t][i][j][k][1] = fy;force_grid[t][i][j][k][2] = fz
    file.close() 
#%%
print(force_grid[:,2,1,0,0])