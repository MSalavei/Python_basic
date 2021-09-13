#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import math
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# task 1.2 unit 2
from math import sqrt
x = float (input ("Введите x: "))
y = float (input ("Введите y: "))
z = float (input ("Введите z "))
vector_length = sqrt (x**2 + y**2 + z**2)
print (f"Длина вектора с координатами {x}, {y}, {z} равна {vector_length}")


# In[47]:


# task 3 unit 2 окружность
get_ipython().run_line_magic('matplotlib', 'qt')
x1 = []
x2 = []
y1 = []
y2 = []
r = 1000

for i in range(1200):
    x1.append(-i)
    x2.append(i)
    y1.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))
    
plt.figure(figsize = (6, 6))    
plt.plot(x1, y1, color='r')
plt.plot(x1, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y1, color='r')
plt.axis('scaled')
plt.show()


# In[48]:


# task 3 unit 2 элипс
get_ipython().run_line_magic('matplotlib', 'qt')
x1 = []
x2 = []
y1 = []
y2 = []
a = 40
b = 20

for i in range(1200):
    x1.append(-i)
    x2.append(i)
    y1.append(np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    
plt.figure(figsize = (6, 6))    
plt.plot(x1, y1, color='r')
plt.plot(x1, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y1, color='r')
plt.axis('scaled')
plt.show()


# In[50]:


# task 3 unit 2 гипербола
get_ipython().run_line_magic('matplotlib', 'qt')
x1 = []
x2 = []
y1 = []
y2 = []
a = 400
b = 200

for i in range(1200):
    x1.append(-i)
    x2.append(i)
    y1.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    
plt.figure(figsize = (6, 6))    
plt.plot(x1, y1, color='r')
plt.plot(x1, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y1, color='r')
plt.axis('scaled')
plt.show()


# In[52]:


# task 5а unit 2 трехмерные графики 2 параллельных плоскостей
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = 2*X + 5*Y
Z2 = Z + 200
ax.plot_wireframe(X, Y, Z)
ax.plot_wireframe(X, Y, Z2)
ax.scatter(0, 0, 0,'z',50,'red')
show()


# In[56]:


# task 5б unit 2 трехмерный график конуса
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X**2 + Y**2)
ax.plot_surface(X, Y, Z)
ax.scatter(0, 0, 0,'z',50,'red')
show()


# In[60]:


# task 1 unit 3 нарисуйте график функции
x = np.linspace(-2*np.pi, 2*np.pi, 201)

k, a, b = np.linspace(2, 12, num = 3)
k1, a1, b1 = np.linspace(11, 24, num = 3)
k2, a2, b2 = np.linspace(21, 32, num = 3)

plt.figure(figsize = (10, 5))
plt.plot(x, k * np.cos(x - a) + b, label = "plot 1")
plt.plot(x, k1 * np.cos(x - a1) + b1, label = "plot 2")
plt.plot(x, k2 * np.cos(x - a2) + b2, label = "plot 3")

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()


# In[62]:


# task 3.1 перевод полярных координат в декартовы
def polar_to_decart(r,phi):
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return x,y

polar_to_decart(2,90)


# In[63]:


# task 3.2 график окружности в полярных координатах
phi = np.arange(0., 2., 1./180.)*np.pi 
plt.polar(phi, [10]*len(phi)) 
plt.show()


# In[65]:


# task 3.3 график отрезка прямой линии в полярных координатах
phi = np.arange(4, 8, 2)
rho = np.arange(4, 8, 2)
plt.polar(phi, rho)         
plt.show()


# In[7]:


# task 4.1 решить систему уравнений exp(x) + x∙(1 – y) = 1 и y = x2 – 1

x = np.linspace(-2, 3, 2000)

plt.figure(figsize = (6, 12))
plt.plot(x, (np.exp(x)+ x - 1)/x)
plt.plot(x, x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1,5) 
plt.grid(True)
plt.axis('scaled')
plt.show()

from scipy.optimize import fsolve

def equations (p):
    x,y = p
    return (x**2 - 1 - y, np.exp(x) + x * (1 - y) - 1)

x1,y1=fsolve (equations, (2,4))
x2,y2=fsolve (equations, (-1,1))
print (x1,y1)
print (x2,y2)
 


# In[13]:


# task 4.2 решить систему y = x**2 – 1 и exp(x) + x∙(1 – y)  - 1 > 0

x = np.linspace(-3, 5, 10000)
plt.plot(x, (np.exp(x) + x*(1 - (x**2-1))-1))

plt.plot(x, x**2 - 1)
plt.grid(linestyle='--')
plt.show()


# In[ ]:





# In[ ]:




