# /////first of all we import numpy
# ////than use np.array to creat a array 
# ////if we check the type than we use type(variable name)
# ////if we check that the array is id,2d or 3d than we use ------variable_name.ndim



# /////in this section we import numpy as np 
# /////np as a shortcut we use numpy as also name numpy
# import numpy
import numpy as np
# /////starting 1d array
# arr_1d=numpy.array([1,4,3,65,1,2])
# # arr_1d=np.array([1,4,3,65,1,2])
# print(arr_1d)
# # ////check that the outout is numpy array or list
# print(type(arr_1d))
# # /////check that the array is 1d,2d or 3d ------ndim means number of dimentions
# print(arr_1d.ndim)



# /////starting 2d array
arr_2d= np.array([[2,4,6,8,10],[1,3,5,7,9]])
print(arr_2d)
# ////to check the size of the array using size function------variable_name.size
print(arr_2d.size)
# ////to check the shape of the array ----to check the no.of rows and colums
# /////this is the return of touple and (rows,colums)
print(arr_2d.shape)
# ////to check the data type whether it is int,float,string or others than we use variuable_name.dtype
print(arr_2d.dtype)