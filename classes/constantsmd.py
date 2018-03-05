#import configparser
import ast
import numpy as np
avagadro = 6.023e23
ial = 4.04e-10 # 3.84e-10 #interatomic length
#ial = 3.84e-10 #interatomic length
epsilon = 0.5 * 1.6e-19 #1.5 #dummy value
sigma = 2.85e-10 #dummy value
#vel = 0.1e-10 #velocity per step
#acc = 1e-10 #acceleration
ts = 0.005e-12 #timestep ex: 0.005 nano seconds as 0.005e-9
N_steps = 10


def N_xyz_(Nx,Ny,Nz): 
    #defining number of atoms along x, y and z axis
    return np.array([Nx,Ny,Nz])


N = N_xyz_(100,6,6)

Fa = 100e6 * (N[1]*N[2]*ial**2)



mass = 26.982e-3/avagadro
FaByMass = Fa/mass


"""

config=configparser.ConfigParser()
config.read('config.ini')
ts = ast.literal_eval(config['DEFAULT']['TimeStep'])
N_steps = ast.literal_eval(config['DEFAULT']['NumTimeSteps'])
avagadro = ast.literal_eval(config['DEFAULT']['Avagadro'])
acc = ast.literal_eval(config['DEFAULT']['Acceleration'])
epsilon = ast.literal_eval(config['DEFAULT']['Epsilon'])
ial = ast.literal_eval(config['DEFAULT']['interatomiclength'])
sigma = ast.literal_eval(config['DEFAULT']['sigma'])


Algorithm = config['DEFAULT']['Algorithm']
PotList = ast.literal_eval(config['POTENTIALS']['PotList'])
PotParameters = ast.literal_eval(config['POTENTIALS']['PotParameters'])
Dimension = ast.literal_eval(config['DEFAULT']['Dimension'])
"""  
def printhello():
    return "hello"

print("called constantmd")