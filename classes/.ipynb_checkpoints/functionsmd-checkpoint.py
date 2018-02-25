import numpy as np
from datetime import datetime
from .constantsmd import *
#from gridmd import *
#------------------------------
print("called functionsmd")
#------------------------------

def timetaken(startTime):
    return datetime.now - startTime

def forceLJ(r, x1, x2):
    f=sigma/r
    Fxij = 24*epsilon*f**6*(2*f**6 - 1)/r*(x1-x2)/r
    return Fxij/avagadro

def LJ(r):
    return 4*epsilon*( (sigma/r)**12 - (sigma/r)**6 ) / avagadro

def verlet_pos(pos,t,ts,acc):
#    pos_t_plus_dt = pos + vel*ts + ( 0.5 * acc * ts**2 ); pos = pos_t_plus_dt
#    pos_t_minus_dt = pos - vel*ts + ( 0.5 * acc * ts**2 ); pos = pos_t_minus_dt
    pos_t_dt = 2*pos - pos*(t-ts) + acc * ts**2; pos = pos_t_dt
# the above given post_t_dt is found by adding above given two taylor equations
    return pos