# ///// array slicing means if we want to any number according to our requirments than we use slicing
# //////
# 
# 
# 
# 
# 
# 
# 
import numpy as np
mx = np.arange(1,101).reshape(10,10) 
# print(mx)
# /////if we want to get the spacific value than we write the variable name and than [row_num,colum_num]
# /////for example
# print(mx)


# ////if we want to give single row than we use this 
# /////we get 3rd row
# print(mx[2])


# //////if we should want to give single colum than we use
# /////we get 5th colums
# print(mx[:,4])


# /////if we want to get all rows but one or spacific colums than we use this function
# print(mx[:, 0:3])


# /////to check the dimention
# print(mx[:, 0:3].ndim)


# /////if we want to some spacific rows and colums
# print(mx[1:4,1:4])


# ////if we want to access all the matrix
# print(mx[:])
# print(mx[:,])
# print(mx[:,:])


# /////to check the size of matrix
print(mx.itemsize)