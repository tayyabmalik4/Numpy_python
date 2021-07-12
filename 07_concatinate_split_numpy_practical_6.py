# /////concatinate and split function using numpy in python//////
# ////if we use these functions than some rules are define 
#------------means arrays size are equal(rows,colums)



# ***************concatenate function
import numpy as np
arr1=np.arange(1,17).reshape(4,4)
arr2=np.arange(1,17).reshape(4,4)
# print(arr2)
# print(arr1)

# ////to join the matrix than we use concatinate funtion
# -----------when we use vector(1d array) than we use + function but in the 2d array its not really work
# /////for exaample
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
# print(lst1+lst2)
# ///////for 2d array this using this function but it is add the numbers but we don't want this 
# print(arr1+arr2)


# /////for using cincatination function and those arrays are join each other
# ///// 2d arrays are concatenated two or more arrays as we wish
# /////by default concatenated by colums
# print(np.concatenate((arr1,arr2)))
# /////this is the secend way to concatenated by colums
# ////vstake menas vertical stack
# print(np.vstack((arr1,arr2)))
# print(np.vstack((lst1,lst2)))


# //////if we want to concatenated by rows wise
# //////1 refers to rows and 0 refers to colums
# print(np.concatenate((arr1,arr2),axis=1))
# /////this is the 2nd way to concatenated row wise
# ////hstack means horizontal stack
# print(np.hstack((arr1,arr2)))



# *******************split function*********************
# //////if we want to split the array of 2 or more pieces than we use split function
# /////split function is divided the array in to eqaule parts if the parts are not made equals than it returns the error
# print(np.split(arr1,4))
# /////it returns the list


# ////if we want to split the array by rows than we use this function
# print(np.split(arr2,2,axis=1))



# /////////////////if we want to splits the values than as our wish than we use this function
# d1=np.array([2,4,6,8,1,4,46,2])
# ///////////////format----------------np.split(arraay,[first_array,2nd_art,all])
# print(np.split(d1,[2,4]))