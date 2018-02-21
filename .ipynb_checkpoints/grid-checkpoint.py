
# coding: utf-8

# In[144]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import time
import sympy as sy
sy.init_printing()


# In[131]:


x=np.arange(0,10,1)
y=np.arange(0,6,1)
z=np.arange(0,3,1)


# In[142]:


def xyz_grid(x,y,z):
    x_y_z = np.empty([x.size,y.size,z.size,3])
    
    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                x_y_z[i][j][k][0]=x[i]
                x_y_z[i][j][k][1]=y[j]
                x_y_z[i][j][k][2]=z[k]
                #print(x_y[i][j][k])
    
    return x_y_z


# In[203]:


def xyz(x,y,z):
    x_y_z = np.empty([x.size,y.size,z.size])
    
    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                x_y_z[i][j][k]=x[i]
                x_y_z[i][j][k]=y[j]
                x_y_z[i][j][k]=z[k]
                #print(x_y[i][j][k])
    
    return x_y_z

def xy(x,y):
    x_y = np.empty([x.size,2])
    
    for i in range(x.size):
        x_y_z[i][j]=x[i]
    for j in range(y.size):
        x_y_z[i][j]=y[j]
           
    
    return x_y


# In[229]:


#plt.scatter(range(10),range(10))#,range(5),np.multiply(range(5),5))
#plt.scatter(range(5),np.multiply(range(5),2))

for i in x:
    for j in y:
        plt.scatter(i,j,c='b')
plt.show()


# In[202]:


xyz_grid(x,y,z)[0,:3,:]


# In[234]:


fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
for i in x:
    for j in y:
        for k in z:
            ax.scatter(i,j,k,c='b')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()


# In[228]:


fig3 = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(x, x*x, x/2, c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

