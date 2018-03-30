import getpass; username=getpass.getuser()
import sys;sys.path.append('/home/'+username+'/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np
import random

from classes.constantsmd import ial, N_steps
from classes.functionsmd import (
    bravais, forceLJ3, forceLJ, r, plotPosGrid, TimeGridAndForceGrid, StrainXYZ
    )
from classes.gridmd import N_xyz
from bravais import writeXYZFile, Force, defForce2D

def main():
    posGrid = bravais(3, 3, 3, a=ial, type='FCC')#, ax=8e-10)
    # writeXYZFile(PosGrid, path='bravais_lattice/test.xyz', scale='Angstrom')
    plotPosGrid(posGrid)
    # time_grid, force_grid = TimeGridAndForceGrid(posGrid, np.ones([3,3,3]))
    print("----END----")

if __name__ == '__main__':
    main()
