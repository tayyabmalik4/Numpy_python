# /////////if we want to arrang the function means if we want to print numbers in arranged then we use arrange function 
# the pattern is-----------np.arrang(start,end,steps) 
# //////////start means the function is how to num start
# /////end means the number is where to end
# ///////step is optional it means the numbers who we want to not exicuted 
# //////////for example if we creat 2 in the step value than its means 2 or multiplier 2 is not printed
# //////arange function is start
import numpy as np
# //////30 in not included
ar_1d = np.arange(6,30)
# /////if we want to get odd numbers than we use as the follwing
# ar_1d=np.arange(5,30,2)
# print(ar_1d)


# ////linspace
# //////if we want to just those numbers who is printed and its seqance than we use linspace function
# ////its taking 3 arrguments first is starting than 2nd is ending and last is sequance

arr=np.linspace(3,30,4)
# print(arr)



# /////reshape()--------
# //////if we want to convert 1d array to 2d or 3d array than we use reshape function
# ///////assign_variable=1d_variable.reshape(exct_size(rows,colums))

# ////starting 2d array
arr_2d=ar_1d.reshape(4,6)
print(arr_2d) 
# ////starting 3d array
arr_3d=ar_1d.reshape(4,3,2)
# print(arr_3d)




# ///////ravel()------------------------
# //////if we want to 3d or 2d array to convert 1d array than we use ravel function
# /////syntax--------------variable.ravel()
a_convert=arr_3d.ravel()
# print(a_convert)


# //////flatten()
# /////this is the same functionality as ravel 
# /////converting 3d or 2d array to 1d arrray

ar_convert=arr_3d.flatten()
# print(ar_convert)



# ///////transport function
# ///////to converting rows to colums and colums to rows than we use transport function
arr_convert=arr_3d.transpose()
# print(arr_convert)
arr_con=arr_2d.transpose()
print(arr_con)