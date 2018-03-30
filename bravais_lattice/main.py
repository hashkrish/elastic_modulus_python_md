import getpass; username=getpass.getuser()
import sys;sys.path.append('/home/'+username+'/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np
import random

from classes.constantsmd import ial, N_steps, N
from classes.functionsmd import (
    bravais, forceLJ3, forceLJ, r, plotPosGrid, TimeGridAndForceGrid, 
    StrainXYZ, CustomPlotPosGrid, LJ, potentialLJ3
    )
from classes.gridmd import N_xyz
from bravais import writeXYZFile, Force, defForce2D

def main():
    posGrid = bravais(N[0], N[1], N[2], a=ial, type='FCC')#, ax=2.5e-10)
    # plotPosGrid(posGrid)#, point=[5,5,5])
    # writeXYZFile(posGrid, path='bravais_lattice/test.xyz', scale='Angstrom')
    # time_grid, force_grid = TimeGridAndForceGrid(posGrid, np.ones([3,3,3]))
    ai=5;aj=5;ak=5
    print('Number of atoms: '+str(N))
    print('Force: '+str(forceLJ3(ai,aj,ak,posGrid)))
    print('Potential: '+str(potentialLJ3(ai,aj,ak,posGrid)))
    print("----END----")

if __name__ == '__main__':
    main()
