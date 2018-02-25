import numpy as np
from datetime import datetime
from .constantsmd import *
from .gridmd import *
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
    pos_t_dt = 2*pos - (pos*(t-ts)) + (acc*ts**2); pos = pos_t_dt
# the above given post_t_dt is found by adding above given two taylor equations
    return pos

def verlet_acc(pos,t,ts,posPlusDt):
    return (posPlusDt - 2*pos + pos*(t-ts))/ts**2

def forceLJ3(x, y, z, xyz_grid):#Force along x-axis
    rg = np.array([-1,0,1])
    pot = 0
    fx = 0;fy=0;fz=0;
    for ri in rg:
        for rj in rg:
            for rk in rg:
                if (ri==0 and rj==0 and rk==0):
                    pass
                else:
                    i=ri;j=rj;k=rk;check=1;checki=1;checkj=1;checkk=1;
                    
                    if(x+ri<0 or x+ri>=N[0]):
                        i=0;check=0;checki=0;
                    if(y+rj<0 or y+rj>=N[1]):
                        j=0;check=0;checkj=0;
                    if(z+rk<0 or z+rk>=N[2]):
                        k=0;check=0;checkk=0;
                    if(check==1):
                        #print(ri,rj,rk)
                        #print(r(x,y,z,x+i,y+j,z+k))
                        #pot += LJ(r(x,y,z,x+i,y+j,z+k))
                        fx += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][0],xyz_grid[i+1][j][k][0])
                        fy += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][1],xyz_grid[i][j+1][k][1])
                        fz += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][2],xyz_grid[i][j][k+1][2])

                        #print("LJ: ",LJ(r(x,y,z,x+i,y+j,z+k)))
    #print("potential: ", pot)
    #print("force along x: ", fx)
    return np.array([fx,fy,fz])

def r(x1, y1, z1, x2, y2, z2, xyz_grid):
    return np.sqrt( (xyz_grid[x2][y2][z2][0]-xyz_grid[x1][y1][z1][0])**2 +  (xyz_grid[x2][y2][z2][1]-xyz_grid[x1][y1][z1][1])**2 + (xyz_grid[x2][y2][z2][2]-xyz_grid[x1][y1][z1][2])**2 )

def forceXLJ3(x, y, z, xyz_grid):#Force along x-axis
    rg = np.array([-1,0,1])
    pot = 0
    fx = 0
    for ri in rg:
        for rj in rg:
            for rk in rg:
                if (ri==0 and rj==0 and rk==0):
                    pass
                else:
                    i=ri;j=rj;k=rk;check=1;checki=1;checkj=1;checkk=1;
                    
                    if(x+ri<0 or x+ri>=N[0]):
                        i=0;check=0;checki=0;
                    if(y+rj<0 or y+rj>=N[1]):
                        j=0;check=0;checkj=0;
                    if(z+rk<0 or z+rk>=N[2]):
                        k=0;check=0;checkk=0;
                    if(check==1):
                        #print(ri,rj,rk)
                        #print(r(x,y,z,x+i,y+j,z+k))
                        #pot += LJ(r(x,y,z,x+i,y+j,z+k))
                        fx += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][0],xyz_grid[i+1][j][k][0])
                        #print("LJ: ",LJ(r(x,y,z,x+i,y+j,z+k)))
    #print("potential: ", pot)
    #print("force along x: ", fx)
    return fx

def forceYLJ3(x, y, z, xyz_grid):#Force along x-axis
    rg = np.array([-1,0,1])
    pot = 0
    fy = 0
    for ri in rg:
        for rj in rg:
            for rk in rg:
                if (ri==0 and rj==0 and rk==0):
                    pass
                else:
                    i=ri;j=rj;k=rk;check=1;checki=1;checkj=1;checkk=1;
                    
                    if(x+ri<0 or x+ri>=N[0]):
                        i=0;check=0;checki=0;
                    if(y+rj<0 or y+rj>=N[1]):
                        j=0;check=0;checkj=0;
                    if(z+rk<0 or z+rk>=N[2]):
                        k=0;check=0;checkk=0;
                    if(check==1):
                        #print(ri,rj,rk)
                        #print(r(x,y,z,x+i,y+j,z+k))
                        #pot += LJ(r(x,y,z,x+i,y+j,z+k))
                        fy += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][1],xyz_grid[i][j+1][k][1])
                        #print("LJ: ",LJ(r(x,y,z,x+i,y+j,z+k)))
    #print("potential: ", pot)
    #print("force along y: ", fy)
    return fy

def forceZLJ3(x, y, z, xyz_grid):#Force along x-axis
    rg = np.array([-1,0,1])
    pot = 0
    fz = 0
    for ri in rg:
        for rj in rg:
            for rk in rg:
                if (ri==0 and rj==0 and rk==0):
                    pass
                else:
                    i=ri;j=rj;k=rk;check=1;checki=1;checkj=1;checkk=1;
                    
                    if(x+ri<0 or x+ri>=N[0]):
                        i=0;check=0;checki=0;
                    if(y+rj<0 or y+rj>=N[1]):
                        j=0;check=0;checkj=0;
                    if(z+rk<0 or z+rk>=N[2]):
                        k=0;check=0;checkk=0;
                    if(check==1):
                        #print(ri,rj,rk)
                        #print(r(x,y,z,x+i,y+j,z+k))
                        #pot += LJ(r(x,y,z,x+i,y+j,z+k))
                        fz += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][2],xyz_grid[i][j][k+1][2])
                        #print("LJ: ",LJ(r(x,y,z,x+i,y+j,z+k)))
    #print("potential: ", pot)
    #print("force along z: ", fz)
    return fz