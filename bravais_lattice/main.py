import getpass; username=getpass.getuser()
import sys;sys.path.append('/home/'+username+'/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np
import random
import scipy as sp

from classes.constantsmd import ial, N_steps, N
from classes.functionsmd import (
    bravais, forceLJ3, forceLJ, r, plotPosGrid, TimeGridAndForceGrid, 
    StrainXYZ, CustomPlotPosGrid, LJ, potentialLJ3, GridPotential, MinimizeMD, MinimizeNR
    )
from classes.gridmd import N_xyz
from bravais import writeXYZFile, Force, defForce2D

def main():
    posGrid = bravais(N[0], N[1], N[2], a=ial, type='FCC', ax=1.01*ial)
    # plotPosGrid(posGrid)#, point=[5,5,5])
    # writeXYZFile(posGrid, path='bravais_lattice/test.xyz', scale='Angstrom')
    # time_grid, force_grid = TimeGridAndForceGrid(posGrid, np.ones([3,3,3]))
    # ai=5;aj=5;ak=5
    # print('Number of atoms: '+str(N))
    # print('Force: '+str(forceLJ3(ai,aj,ak,posGrid)))
    # print('Potential: '+str(potentialLJ3(ai,aj,ak,posGrid)))
    Minimized = MinimizeMD(posGrid, ts=0.001e-15, fixends=['x'])
    # Minimized = MinimizeNR(posGrid, fixends=['x'], ItType='NR')
    # plotPosGrid(Minimized)
    writeXYZFile(Minimized, path='bravais_lattice/test.xyz', scale='Angstrom')
    try:
        print(np.mean(Force(posGrid)[:,:,:,0]))
        print(np.mean(Force(Minimized)[:,:,:,0]))
    except:
        pass
    
if __name__ == '__main__':
    main()