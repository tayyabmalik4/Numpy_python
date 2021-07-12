# ************random sampling using numpy in python***********
# *********this is the web link which all the random functions are written it************
# *********link---------https://numpy.org/doc/1.16/reference/routines.random.html-----------------


import numpy as np
import random

# /////it returs the array which we wish the values and the values is between 0 to 1 floot
r=np.random.random(6)
# print(r)
# /////if we want to creat 2d array using random function than  we use thios function
r1=np.random.random((3,3))
# print(r1)
# /////if we want to get values in int then we use np.random.randint function
# //////first of all we take to define that the who many numbers given that means 1 to 4 and 4 is not included than we take touple
# -----------in touple we take a shape means (rows,colums)
r2=np.random.randint(1,4)
r3=np.random.randint(1,4,(3,3))
# print(r2)
print(r3)

# ***********creating 3d array
# ////////in 3d array 1st value is shows who many arrays than 2nd shows how many rows and 3rd value shows how many colums
r4=np.random.randint(1,5,(2,4,4))
# print(r4)


# ///////if we want to same values in all the outputs than we use np.random.seed(argument)
np.random.seed(29)
r5=np.random.randint(1,7,(3,5,5))
# print(r5)



# //////if we want to given 0 to 1 value and we created multyple arrays using this module
r6=np.random.rand(3,3,3)
r7=np.random.rand(3,3)
r8=np.random.rand(3)
# print(r6)
# print(r7)
# print(r8)


# ///////if we want to creat positive and nagitive numbers than we use np.random.randn function
r9=np.random.randn(3,3)
# print(r9)


# ///////if we want to getting just one value than we use np.random.chooice(variable) function
# //////in this function the array is must be 1d because it is not sported 2d or 3d array
r10=np.arange(4,16)
# print(r10)
# r11= np.random.randint(8,18,(4,4,4))
# print(r11)
# print(random.choice(r10)) 
# for i in range(10):
#     print(np.random.choice(r10)) 


# /////for shafling the array than we use permotation function
# /////if we run this function in 1d then shaffles the attributes 
# ////when we use this function in the 2d array then shuffle the rows
# /////when we use this function in 3d array than no change accures
print(np.random.permutation(r3))
