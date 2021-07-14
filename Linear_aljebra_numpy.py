# *****************************Linear Algebra functions using numpu in python**********************************





import numpy as np

ln=np.arange(1,10).reshape((3,3))
ln1=np.arange(1,10).reshape((3,3))
print(ln)

# ///////if we want to check rank of the 2d array than we use np.linalg.matrix_rank(variable)
# print("Rank of the matrix",np.linalg.matrix_rank(ln))

# ///////if we want to trace the matrix or 2d array than we use np.trace(variable)
# print(np.trace(ln))

# //////if we want to determine the determinent than we use this function-------np.linalg.det(variable)
# //////but the determinent is just the square matrix
# print(np.linalg.det(ln))

# ////if we want to determine the inverse of the matrix than we use this function-----np.linalg.inv(variable)
# print(np.linalg.inv(ln))

# ////if we want to determine the power of the matrix than we use this function------np.linalg.matrix_power(variable, power)
# print(np.linalg.matrix_power(ln, 3))


# ////////when we determine the linear equation than we use this function --------np.linalg.solve(coeficients,constants)
# --------------------y=mx+c using this formula
# //////array must be square
coff=np.array([[1,2],[3,4]])
cont=np.array([8,3])
# print("linear equation solution",np.linalg.solve(coff,cont))


#////////////// if we want to determine scalar product of the matrix than we use this function-------------np.dot(variable_1,variable_2)
# print(np.dot(ln,ln1))

# /////////if we want to determine vertor product of the matrix than we use this function-------np.vdot(variable_1,variable_2)
# print(np.vdot(ln,ln1))


# /////if we want to determine the inner product than we use this function ----------np.inner(variable_1,variable_2)
# ------format------multiply midvalues and add +1
# print(np.inner(ln,ln1))


# ////if we want to determine the outer product of two vextors than wwe use this function----------np.outer(vector)
# /////when we use outer function it returns 1d array in colums if we put one value.
# the value which we put that is multiply every element indiviually------- as following
# print(np.outer(ln,1))
# print(np.outer(ln,[2,3]))


# ***************************Norm(lenght) of the matrix*****************
# ///////if we want to check or determine the lenght of the matrix than we use this function
# print(np.linalg.norm(ln))
# print(np.linalg.norm(ln,'fro'))
# print(np.linalg.norm(ln,np.inf))
# print(np.linalg.norm(ln,-np.inf))

# *******************Condition Matrix************************
# //////////////////Compute the condition number of a matrix.
# ////////////////// This function is capable of returning the condition number using one of seven different norms, depending on the value of p (see Parameters below
# print(np.linalg.cond(ln))
# print(np.linalg.cond(ln,'fro'))
# print(np.linalg.cond(ln,np.inf))
# print(np.linalg.cond(ln,-np.inf))

 
# /////////////////if we want to multoply more than two matrix than we use this fuction----------multi_dot([vector1,vector2,vector3,vector4])
# print(multi_dot([vector1,vector2,vector3,vector4]))


# //////////if we want to printout the dilonal array using just 1d array
dilonall=np.array([2,3,5,7])
# print(np.diag(dilonall))


# ///////if we want to search of show the spacific indexes than we use ----------np.where(condition,variable,condition(optional))
# print(np.where(ln<4,ln,5*ln))


# /////if we want to differance of two or more matrix than we use this function-------np.diff(variable,(optional axis=?))