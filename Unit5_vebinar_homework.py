#!/usr/bin/env python
# coding: utf-8

# In[75]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import itertools
import math


# In[ ]:





# In[16]:


# Unit 5, task 1
for i in range (0,5):
    a = input()
    x = np.random.uniform (0,36)
    print (int(x))


# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:


# Unit 5, task 2.1
k, m = 0, 0
n = 100
for i in range (0, n):
    x = np.random.uniform (0,10)
    if x<5:
        k = k + 1
    else:
        m = m + 1
print (f"Вероятность выпадения 'Орла' равна {k/n}")
print (f"Вероятность выпадения 'Решки' равна {m/n}")
if k/n+m/n == 1:
    print ("Теорема сложения вероятностей истинна!")


# In[47]:


# Unit 5, task 2.2
l = []
for i in range (0,10):
    x = np.random.rand (10)
    sum_x = np.sum (x)
    l.append (sum_x) 
print (l)
num_bins = 3
n, bins, patches = plt.hist (l, num_bins)
plt.xlabel ("x")
plt.ylabel ("Probability")
plt.title ("Histogram")


# In[55]:


# Unit 5, task 3.1
k, n = 0, 10000
a = np.random.randint(0,2,n)
b = np.random.randint(0,2,n)
c = np.random.randint(0,2,n)
d = np.random.randint(0,2,n)
x = a + b + c + d
for i in range (0, n):
        if x[i] == 2:
            k = k + 1
print ("Данные симуляции Монте-Карло: ", k, n, k/n)
ckn = np.math.factorial(4)/(np.math.factorial(2)*np.math.factorial(2))
pnk = ckn * (1/2**4)
print (f"Расчет вероятности по формуле Бернулли {pnk}")


# In[58]:


# Unit 5, task 3.2
k, n = 0, 100000
a = np.random.randint(0,2,n)
b = np.random.randint(0,2,n)
c = np.random.randint(0,2,n)
d = np.random.randint(0,2,n)
x = a + b + c + d
for i in range (0, n):
        if x[i] == 3:
            k = k + 1
print (x)
print ("Данные симуляции Монте-Карло: ", k, n, k/n)
ckn = np.math.factorial(4)/(np.math.factorial(3)*np.math.factorial(1))
pnk = ckn * (1/2**4)
print (f"Расчет вероятности по формуле Бернулли {pnk}")


# In[62]:


# Unit 5, task 4
s = 0
for p in itertools.permutations ("0123", 3):
    print ("".join(str(x) for x in p))
    s+=1
print (s)


# In[77]:


# Unit 5, task 5

n = 100
r = 0.65
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)

plt.plot([0, 1], [b, a + b])
plt.show()

ym = y/n
xm = x/n

R_isk = (np.sum((x-xm)*(y-ym)))/(math.sqrt (np.sum((x-xm)**2)*np.sum((y-ym)**2)))
print (R_isk)


# In[ ]:




