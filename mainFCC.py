
# coding: utf-8

# # Finding Elastic Modulus of Aluminium (FCC)

# ## Importing Libraries

#importing required libraries
import sys;sys.path.append('/home/krish/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np

from classes.constantsmd import *
from classes.functionsmd import *#(forceLJ3FCC, forceXLJ3, forceYLJ3, forceZLJ3, verlet_pos, writeXYZFile, numberOfAtoms, r, TimeGridAndForceGrid)
from classes.gridmd import (N_steps, makeLattice, makeLatticePos, plotPosGrid,
                            plotStructure)
print("-----------start-----------")


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
    ]            ])
N = np.array([3, 3, 3])
latticeGrid = makeLattice(brick, N[0], N[1], N[2])
posGrid = makeLatticePos(brick, N[0], N[1], N[2], ial/2)
#writeXYZFile(latticeGrid, posGrid,name='temp.xyz')
plotPosGrid(posGrid)

N[0] = posGrid.shape[0]
N[1] = posGrid.shape[1]
N[2] = posGrid.shape[2]

time_grid, force_grid = TimeGridAndForceGrid(posGrid, latticeGrid)

time_forceMean, time_stress, time_stress_applied = timeForceMeanAndTimeStress(force_grid, time_grid)

endStrain = myStrain(time_grid, latticeGrid)
#abs(time_grid[1,0,0,2,0]-time_grid[1,N[0]-1,0,2,0])/abs(time_grid[0,0,0,0,0]-time_grid[0,N[0]-1,0,0,0])

endStrain[:,0]
time_strainXYZ = StrainXYZ(time_grid)

# ## Strain-Time Diagram

time_strainMean = timeStrainMean(time_grid, latticeGrid)
# plt.plot(range(N_steps) ,time_strainMean[:,0])

refStrain = np.zeros([N_steps,3])
for t in range(N_steps):
    refStrain[t,0] = np.mean(time_strainXYZ[t,:,:,:,0])
    refStrain[t,1] = np.mean(time_strainXYZ[t,:,:,:,1])
    refStrain[t,2] = np.mean(time_strainXYZ[t,:,:,:,2])
# print(time_strainMean-refStrain)


# ## Stress-Time Diagram
plt.plot(range(N_steps) ,time_stress[:,0])
# ## Stress-Strain Diagram
n=N_steps
#fig, axs = plt.subplot(1,2)

plt.plot(time_strainMean[:n,0], time_stress[:n,0])
plt.plot(refStrain[:n,0], time_stress[:n,0])
plt.gca().legend(('time_strainMean','refStrain'))
#plt.show()
plt.scatter(time_strainMean[:n,0], time_stress[:n,0])
plt.scatter(refStrain[:n,0], time_stress[:n,0])
plt.gca().legend(('time_strainMean','refStrain'))
plt.show()
for t in range(N_steps):
    print(endStrain[t,0],'\t',time_strainMean[t,0],'\t', refStrain[t,0])


# ## Stress/Strain Value
for i in range(N_steps):
    print((time_stress[i,0]/time_strainMean[i,0])/1e9, '\t', (time_stress[i,0]/refStrain[i,0])/1e9, '\t', (time_stress[i,0]/endStrain[i,0])/1e9, "GPa")

# ## Completion Alert
import platform
platform.system()
if(platform.system()=='Windows'):
    import winsound
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
if(platform.system()=='Linux'):
    import os
    os.system('spd-say "your program is done"')


# ## Program End
print("------------end------------")

