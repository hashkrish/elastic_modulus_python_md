import sys;sys.path.append('/home/krish/elastic_modulus_python_md/')
import matplotlib.pyplot as plt
import numpy as np
import random

from classes.constantsmd import ial
from classes.functionsmd import bravais, forceLJ3, forceLJ, r, plotPosGrid
from classes.gridmd import N_xyz
from bravais import writeXYZFile, Force, defForce2D

def main():
    posGrid = bravais(3, 3, 3, a=ial, type='FCC')#, ax=8e-10)
    #writeXYZFile(PosGrid, path='bravais_lattice/test.xyz', scale='Angstrom')
    force = np.zeros([posGrid.shape[0], posGrid.shape[1], posGrid.shape[2], 3])
    force += defForce2D(force, X=100e3)
    force += Force(posGrid)
    print(force)
    print("----END----")

if __name__ == '__main__':
    main()
        