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
    return Fxij#/avagadro

def LJ(r):
    return 4*epsilon*( (sigma/r)**12 - (sigma/r)**6 ) 

def verlet_pos(pos, posPrevious, t, ts, acc):
    pos_t_dt = 2*pos - posPrevious + (acc*ts**2); pos = pos_t_dt
    # pos_t_plus_dt = pos + vel*ts + ( 0.5 * acc * ts**2 ); pos = pos_t_plus_dt
#    pos_t_minus_dt = pos - vel*ts + ( 0.5 * acc * ts**2 ); pos = pos_t_minus_dt
# the above given post_t_dt is found by adding above given two taylor equations
    return pos

def verlet_posd(pos, t, ts, acc):
    pos_t_dt = 2*pos - pos*(t-ts) + (acc*ts**2); pos = pos_t_dt
    return pos

def verlet_acc(pos,t,ts,posPlusDt):
    return (posPlusDt - 2*pos + pos*(t-ts))/ts**2

def forceLJ3(x, y, z, xyz_grid):#Force along x-axis
    rg = np.array([-1, 0 , 1])
    fx = 0;fy=0;fz=0
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
    # print("force along x: ", fx)
    return np.array([fx,fy,fz])

def forceLJ3FCC(x, y, z, xyz_grid, latticeGrid):#Force along x-axis
    rg = np.array([-1, 0, 1])
    #rg = np.array([-3, -2, -1, 0 , 1, 2, 3])
    pot = 0
    fx = 0;fy=0;fz=0;
    N[0] = xyz_grid.shape[0]
    N[1] = xyz_grid.shape[1]
    N[2] = xyz_grid.shape[2]
    for ri in rg:
        for rj in rg:
            for rk in rg:
                if (ri==0 and rj==0 and rk==0):
                    pass
                else:
                    i=ri;j=rj;k=rk;check=1;checki=1;checkj=1;checkk=1;
                    
                    if(x+ri<0 or x+ri>=N[0]):
                        i=0;check=0;checki=0
                    if(y+rj<0 or y+rj>=N[1]):
                        j=0;check=0;checkj=0
                    if(z+rk<0 or z+rk>=N[2]):
                        k=0;check=0;checkk=0
                    if(check==1 and latticeGrid[i, j, k]==1):
                        #print(ri,rj,rk)
                        #print(r(x,y,z,x+i,y+j,z+k))
                        #pot += LJ(r(x,y,z,x+i,y+j,z+k))
                        try:
                            fx += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][0],xyz_grid[i+1][j][k][0])
                            fy += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][1],xyz_grid[i][j+1][k][1])
                            fz += forceLJ(r(x,y,z,x+i,y+j,z+k, xyz_grid),xyz_grid[i][j][k][2],xyz_grid[i][j][k+1][2])
                        except Exception as e:
                            print('Error at:',ri,rj,rk)
                            print(e)
                            print('------------------')
                            quit()
                        #print("LJ: ",LJ(r(x,y,z,x+i,y+j,z+k)))
    #print("potential: ", pot)
    #print("force along x: ", fx)
    return np.array([fx,fy,fz])

def r(x1, y1, z1, x2, y2, z2, xyz_grid):
    return np.sqrt( (xyz_grid[x2][y2][z2][0]-xyz_grid[x1][y1][z1][0])**2 
        + (xyz_grid[x2][y2][z2][1]-xyz_grid[x1][y1][z1][1])**2 
        + (xyz_grid[x2][y2][z2][2]-xyz_grid[x1][y1][z1][2])**2 )

def forceXLJ3(x, y, z, xyz_grid):#Force along x-axis
    rg = np.array([-1,0,1])
    #pot = 0
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
                    i=ri;j=rj;k=rk;check=1;#checki=1;checkj=1;checkk=1;
                    
                    if(x+ri<0 or x+ri>=N[0]):
                        i=0;check=0;#checki=0;
                    if(y+rj<0 or y+rj>=N[1]):
                        j=0;check=0;#checkj=0;
                    if(z+rk<0 or z+rk>=N[2]):
                        k=0;check=0;#checkk=0;
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

def timeForceMeanAndTimeStress(force_grid, time_grid):
    time_forceMean = np.zeros([N_steps, 3])
    time_stress = np.zeros([N_steps, 3])
    time_stress_applied = np.zeros([N_steps, 3])
    fxMean = 0;fyMean = 0;fzMean = 0
    for t in range(N_steps):
        for i in range(N[0]):
            for j in range(N[1]):
                for k in range(N[2]):
                    fxMean+=force_grid[t][i][j][k][0]
                    fyMean+=force_grid[t][i][j][k][1]
                    fzMean+=force_grid[t][i][j][k][2]
        fxMean = fxMean/N[0];fyMean = fyMean/N[1];fzMean = fzMean/N[2];
        time_stress[t] = np.array([fxMean/(N[1]*N[2]*ial**2), fyMean/(N[2]*N[0]*ial**2), fzMean/(N[1]*N[0]*ial**2)])*74
        time_forceMean[t] = np.array([fxMean, fyMean, fzMean])
        time_stress_applied[t,0] = np.array([Fa/( abs(time_grid[t,0,0,0,1] - time_grid[t,0,N[1]-1,0,1]) * abs(time_grid[t,0,0,0,2] - time_grid[t,0,0,N[2]-1,2]))])
    return time_forceMean, time_stress, time_stress_applied

def numberOfAtoms(latticeGrid):
    c=0
    for i in range(latticeGrid[:,0,0].size):
        for j in range(latticeGrid[0,:,0].size):
            for k in range(latticeGrid[0, 0, :].size):
                if(latticeGrid[i, j, k] == 1):
                    c+=1
    return c

def writeXYZFile(latticeGrid, posGrid, name='None'):
    if name == 'None':
        file = open("pos.xyz", "w")
    else:
        file = open(name, "w")
    file.write(str(numberOfAtoms(latticeGrid))
                + '\n')
    file.write('[ FCC ]\n')
    c=1
    for i in range(posGrid.shape[0]):
        for j in range(posGrid.shape[1]):
            for k in range(posGrid.shape[2]):
                if(latticeGrid[i, j, k] == 1):
                    file.write('atom' + str(c) + ' ' 
                                + str(posGrid[i, j, k, 0]) + ' '  
                                + str(posGrid[i, j, k, 1]) + ' ' 
                                + str(posGrid[i, j, k, 2]) + ' ' 
                                + '\n')
                    c += 1

def TimeGridAndForceGrid(posGrid, latticeGrid):
    #N = np.array(3)
    N[0] = posGrid.shape[0]
    N[1] = posGrid.shape[1]
    N[2] = posGrid.shape[2]
    time_grid = np.zeros([N_steps,N[0],N[1],N[2],3])
    time_grid[0] = np.array([posGrid])

    force_grid = np.zeros([N_steps, N[0], N[1], N[2],3])
    for t in range(N_steps):
    #     file = open("dump/pos/timestep_"+str(t+1)+".xyz", "w")
    #     file.write(str(numberOfAtoms(latticeGrid))+'\n')
    #     file.write('\n')
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
                            time_grid[t+1][i][j][k][0] = xj
                            time_grid[t+1][i][j][k][1] = yj
                            time_grid[t+1][i][j][k][2] = zj
                        elif (t == N_steps-1):
                            pass
                        else:
                            xj=verlet_pos(time_grid[t][i][j][k][0], time_grid[t-1][i][j][k][0], t,ts,acc)
                            yj=verlet_pos(time_grid[t][i][j][k][1], time_grid[t-1][i][j][k][1], t, ts, 
                                        fy/mass)
                            zj=verlet_pos(time_grid[t][i][j][k][2], time_grid[t-1][i][j][k][2], t, ts, 
                                        fz/mass)
                            time_grid[t+1][i][j][k][0] = xj
                            time_grid[t+1][i][j][k][1] = yj
                            time_grid[t+1][i][j][k][2] = zj
    #                     file.write('X '+str(xj)+' '+str(yj)+' '+str(zj)+'\n')
                        force_grid[t][i][j][k][0] = fx;force_grid[t][i][j][k][1] = fy;force_grid[t][i][j][k][2] = fz
    #     file.close()                     
    return time_grid, force_grid

def latticeMean3X(latticeGrid, grid):
    
    temp = np.zeros([latticeGrid.shape[1],latticeGrid.shape[2]])
    for j in range(N[1]):
        for k in range(N[2]):
            if (latticeGrid[0,j,k]==1 or latticeGrid[N[0]-1,j,k]==1):
                temp[j,k] = grid[j,k]
    return np.mean(temp)

def myStrain(time_grid, latticeGrid):
    strain = np.zeros([N_steps,3])
    for t in range(N_steps):
        tempMat = np.zeros([N[1],N[2]])
        for j in range(N[1]):
            for k in range(N[2]):
                try:
                    tempMat[j,k] = abs(time_grid[t,0,j,k,0]-time_grid[t,N[0]-1,j,k,0])/abs(time_grid[0,0,j,k,0]-time_grid[0,N[0]-1,j,k,0])
                except:
                    print("error:",t,j,k)

        strain[t,0] = latticeMean3X(latticeGrid, tempMat)
    return strain

def StrainXYZ(time_grid):
    strainXYZ = np.zeros([N[0], N[1], N[2], 3])
    time_strainXYZ = np.zeros([N_steps, N[0], N[1], N[2], 3])
    time_strainXYZ[0] = strainXYZ
    for t in range(N_steps):
        if t==0:
            pass #strainX[t] = 0
        else:
            strainXYZ = abs(time_grid[t]-time_grid[1])/ial
            time_strainXYZ[t] = strainXYZ
    return time_strainXYZ

def timeStrainMean(time_grid, latticeGrid):
    time_strainXYZ = StrainXYZ(time_grid)
    no = numberOfAtoms(latticeGrid)
    time_strainMean = np.zeros([N_steps, 3])
    StrainX = 0;StrainY = 0;StrainZ = 0
    for t in range(N_steps):
        for i in range(N[0]):
            for j in range(N[1]):
                for k in range(N[2]):
                    if(latticeGrid[i, j, k]==1):
                        StrainX +=time_strainXYZ[t][i][j][k][0]
                        StrainY +=time_strainXYZ[t][i][j][k][1]
                        StrainZ +=time_strainXYZ[t][i][j][k][2]
        StrainXMean = StrainX/no;StrainYMean = StrainY/no;StrainZMean = StrainZ/no;
        time_strainMean[t] = np.array([StrainXMean, StrainYMean, StrainZMean])
    return time_strainMean

def bravais(nx, ny, nz, a, type='None', ax=0, ay=0, az=0):
    if ax==0:
        ax=a
    if ay==0:
        ay=a
    if az==0:
        az=a
        
    if type=='FCC':
        a1 = np.array([0.0, 0.5, 0.5])*ax
        a2 = np.array([0.5, 0.0, 0.5])*ay
        a3 = np.array([0.5, 0.5, 0.0])*az
    
    if type=='SC':
        a1 = np.array([1.0, 0.0, 0.0])*ax
        a2 = np.array([0.0, 1.0, 0.0])*ay
        a3 = np.array([0.0, 0.0, 1.0])*az
    
    if type == 'None':
        print("\n------Descripe lattice structure------\n")
        exit()

    posGrid = np.zeros([nx, ny, nx, 3])
    for i in range(nx):
        n1 = list(range(nx//2, nx+nx//2))[i]
        for j in range(ny):
            n2 = list(range(ny//2, ny+ny//2))[j]
            for k in range(nz):
                n3 = list(range(nz//2, nz+nz//2))[k]
                #R = i*a1 +  j*a2 + k*a3
                R = n1*a1 + n2*a2 + n3*a3
                posGrid[i, j, k] = R
    return posGrid













