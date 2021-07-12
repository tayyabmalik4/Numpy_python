# /////if we want to creat default ones or zeros matrix than we use ones or zeros functions
# ////to creat ones function np.ones((touple),datatype-optional)
# ////to creat zeroes function np.zeros((rows,colums),datatype)
# ////to creat empty function np.empty((rows,colms),datatype)



import numpy as np
mx=np.array([[1,1,1],[1,1,1]])
# print(mx)

# /////to print all one in the matrics then we use ones function
# /////basically ones function return the float as a default if we want to change the datatype than we use as the folllowing

# //////------------starting ones function
# mx_1 =np.ones((4,4))
# mx_1 =np.ones((4,4),int)
# mx_1 =np.ones((4,4),str)
# //////if the output is one than bool is true and if return number is 0 than bool is false
mx_1 =np.ones((4,4),bool)
# print(mx_1)


# //////-----------starting zeros function
# mx_0=np.zeros((4,4))
# mx_0=np.zeros((4,4),dtype=int)
# when run the program as a str datatype than string return empty
# mx_0=np.zeros((4,4),str)
mx_0=np.zeros((4,4),bool)
# print(mx_0)


# //////////-------stating empty function
# # /////when empty program is exicute than is returns the any value
mx_em=np.empty((4,4))
print(mx_em)



