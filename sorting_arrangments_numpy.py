# *************sorting Arrangments using numpy in python

# //////////////// if we want to sort the arrays than we use this function
# ////////we sorting as a assending, desending,by rows,by colums,by merging,by name, by int

import numpy as np

# creating the 2d array 3X3
# arr=np.arange(1,10).reshape(3,3)
# /////seed function to getting the same values
# /////random function to creating the different values 1 to 9
np.random.seed(20)
arr1=np.random.randint(1,9,(3,3))
# print(arr1)

# /////this is sorting by colums by default
# print(np.sort(arr1))


# ////sorting by rows
# print(np.sort(arr1,axis=1))

# ////when we want to assending the sorting than we use this function
# print(np.sort(arr1, axis=None))

# ///if we want to desending the array than we use this method
# ///////for single array
arr2=np.arange(1,10)
print(arr2)
# ////desending the array using slicing
print(np.sort(arr2)[::-1])
# /////this is for 2d array and it reverse the rows and also assending the order
# print(np.sort(arr1)[::-1])

# //////if we want to know that how places are sorted first than we use argsort function
print(np.argsort(arr))

# //////numpy is workiong as a pointer if we creat new variable and slicing the previous variable than it is the as a pointer
# //////and when we change the new variable than automatically change previous variable 
# /////if we avoid the changes of previous variable than we use copy function like following

# ///with changing arr
# arr1=arr[3,5]
# ////without changing arr
arr1=arr[3,5].copy()
arr1[0]=9
print(arr1)
print(arr)
