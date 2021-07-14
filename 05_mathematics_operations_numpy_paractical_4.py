# /////////mathematical operations by using numpy//////
# //////like adding,subtracting, dividing, multiplying in matrics
# ////// this is use as a same matrixs







import numpy as np
arr1=np.arange(1,10).reshape(3,3)
# print(arr1)
arr2=np.arange(1,10).reshape(3,3)
# print(arr1)
# print(arr2)


#/////////// for addition of matrix
# //////this is the simple way
# print(arr1+arr2)
# /////this is for pythonic way using numpy
# print(np.add(arr1,arr2))

# ////////for subtracting the matrics
# /////this is for simple way
# print(arr1-arr2)
# /////this is the pythonic way using numpy
# print(np.subtract(arr1,arr2))





# //////for dividing the matrics
# ////this is for simple way
# print(arr1/arr2)
# ////this is the pythoinic way using numpy
# print(np.divide(arr1,arr2))



# /////for simple multiply the matrics
# /////this is for simple way
# print(arr1*arr2)
# ////this is for pythonioc way using numpy
# print(np.multiply(arr1,arr2))


# ////for muliplying using matrics where multiply rows and colums
# ////this is for simple way
# print(arr1@arr2)
# //////this is for pythonic way using numpy
# print(np.dot(arr1,arr2))



# ////////for checking the maximum value
# max=arr1.max()
# print(max )
# //////if we want to check the maximum value position than we use argmax function
# max1=arr1.argmax()
# print(max1)
# //////if we find the maximun values in all the colums 
# /////"1" represents the maximum value of rows and "0" represent the maximum value of colums
max2=arr1.max(axis=1)
max3=arr1.max(axis=0)
# print(max2)
# print(max3)



# //////////to find the minmum values than we use min function and than all the procedure same as max values means all the functions
min=arr2.min()
# print(min)
# print(arr2.argmin())
# print(arr2.min(axis=1))
# print(arr2.min(axis=0))




# /////if we want to add the all values in one matrics than we use np.sum(matrics_name
# print(np.sum(arr1)) 
# ////////if we want to add the only colums or rows than we use also sum function like following
# print(np.sum(arr1, axis=0))
# print(np.sum(arr1, axis=1 ))



# //////if we want to find out average(mean) of the matrics than we use mean function
# print(np.mean(arr1)) 



# /////if we want to find out squreroot of the matrics than we use sqrt function in numpy
# print(np.sqrt(arr2))



# /////if we want to find out standerd deviation than we use std function in numpy
# print(np.std(arr1))


# ////if we want to find out exponencial of the matrics than we use exp function
# print(np.exp(arr1))



# ////if we want to find out the natural log than we use np.log(variable)
# print(np.log(arr1))

# ////if we want to find out the log base 2 than we use np.log2(varoable)
# print(np.log2(arr1))


# ////if we want to find out the log base 10 than we use np.log(variable)
# print(np.log10(arr1))



