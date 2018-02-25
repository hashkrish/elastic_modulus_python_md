import configparser
import ast


avagadro = 6.023e23
ial = 4.04e-10 #interatomic length
epsilon = 0.5* 1.6e-19 #1.5 #dummy value
sigma = 2.85e-10 #dummy value
vel = 0.1e-10 #velocity per step
acc = 1e-10 #acceleration
ts = 5e-9 #timestep ex: 0.005 nano seconds as 0.005e-9
N_steps = 10
Fa = 1.73e-9
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