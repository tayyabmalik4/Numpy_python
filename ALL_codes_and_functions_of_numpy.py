# ************************modules***********************
import numpy as np
import matplotlib.pyplot as plt
import random


# ***********************Array Types********************
arr_1d=np.array([1,4,3,65,1,2])
print(type(arr_1d))
print(arr_1d.ndim)
arr_2d= np.array([[2,4,6,8,10],[1,3,5,7,9]])
print(arr_2d.size)
print(arr_2d.shape)
print(arr_2d.dtype)

# **********************Ones and Zeroes and Empty Arrays *******************
mx=np.array([[1,1,1],[1,1,1]])
mx_1 =np.ones((4,4))
mx_1d =np.ones((4,4),int)
mx_1dd =np.ones((4,4),str)
mx_1 =np.ones((4,4),bool)
mx_0=np.zeros((4,4))
mx_0=np.zeros((4,4),dtype=int)
mx_0=np.zeros((4,4),str)
mx_0=np.zeros((4,4),bool)
mx_em=np.empty((4,4))


# *******************Arrange And Different Functions*************************
ar_1d = np.arange(6,30)
ar_1d=np.arange(5,30,2)
arr=np.linspace(3,30,4)
arr_2d=ar_1d.reshape(4,6)
arr_3d=ar_1d.reshape(4,3,2)
a_convert=arr_3d.ravel()
ar_convert=arr_3d.flatten()
arr_convert=arr_3d.transpose()
arr_con=arr_2d.transpose()


# *******************Mathematical Operations*********************************
arr1=np.arange(1,10).reshape(3,3)
arr2=np.arange(1,10).reshape(3,3)
print(arr1+arr2)
print(np.add(arr1,arr2))
print(arr1-arr2)
print(np.subtract(arr1,arr2))
print(arr1/arr2)
print(np.divide(arr1,arr2))
print(arr1*arr2)
print(np.multiply(arr1,arr2))
print(arr1@arr2)
print(np.dot(arr1,arr2))
max=arr1.max()
max1=arr1.argmax()
max2=arr1.max(axis=1)
max3=arr1.max(axis=0)
min=arr2.min()
print(min)
print(arr2.argmin())
print(arr2.min(axis=1))
print(arr2.min(axis=0))
print(np.sum(arr1)) 
print(np.sum(arr1, axis=0))
print(np.sum(arr1, axis=1 ))
print(np.mean(arr1)) 
print(np.sqrt(arr2))
print(np.std(arr1))
print(np.exp(arr1))
print(np.log(arr1))
print(np.log2(arr1))
print(np.log10(arr1))


# ***********************Array Slicing**************************************
mx = np.arange(1,101).reshape(10,10) 
print(mx[2])
print(mx[:,4])
print(mx[:, 0:3])
print(mx[:, 0:3].ndim)
print(mx[1:4,1:4])
print(mx[:])
print(mx[:,])
print(mx[:,:])
print(mx.itemsize)


# ********************Concatenate and Split**********************
arr1=np.arange(1,17).reshape(4,4)
arr2=np.arange(1,17).reshape(4,4)
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
print(lst1+lst2)
print(np.concatenate((arr1,arr2)))
print(np.vstack((arr1,arr2)))
print(np.vstack((lst1,lst2)))
print(np.concatenate((arr1,arr2),axis=1))
print(np.hstack((arr1,arr2)))
print(np.split(arr1,4))
print(np.split(arr2,2,axis=1))
d1=np.array([2,4,6,8,1,4,46,2])
print(np.split(d1,[2,4]))



# ******************Trignomatric***********************
val=np.sin(180)
val2=np.cos(180 * np.pi/180)
val3=np.tan(180)
val4=np.arcsin(0.453523)
val5=np.arccos(0.211423)
val6=np.arctan(0.86782367)
x_sin=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x_sin)
y_cos=np.cos(x_sin)
y_tan=np.tan(x_sin)
y_arcsin=np.arcsin(x_sin)
y_arccos=np.arccos(x_sin)
y_arctan=np.arctan(x_sin)
plt.plot(x_sin,y_sin)
plt.show()
plt.plot(x_sin,y_cos)
plt.show()
plt.plot(x_sin,y_tan)
plt.show()
plt.plot(x_sin,y_arcsin)
plt.show()
plt.plot(x_sin,y_arccos)
plt.show()
plt.plot(x_sin,y_arcsin)
plt.show()
print(np.degrees(x_sin))
print(np.deg2rad(x_sin)) 
print(np.radians(x_sin))
base=[10,2,5,50]
per=[3,10,23,6]
hyp=np.hypot(base,per)
r=np.array([0.23,0.9,1.56,1.5,9.99,1.1])
print(np.ceil(r))
print(np.floor(r))
print(np.fix(r))
print(np.trunc(r))
print(np.round(r))
print(np.rint(r))



# *******************Random*******************
r=np.random.random(6)
r1=np.random.random((3,3))
r2=np.random.randint(1,4)
r3=np.random.randint(1,4,(3,3))
r4=np.random.randint(1,5,(2,4,4))
np.random.seed(29)
r5=np.random.randint(1,7,(3,5,5))
r6=np.random.rand(3,3,3)
r7=np.random.rand(3,3)
r8=np.random.rand(3)
r9=np.random.randn(3,3)
r10=np.arange(4,16)
r11= np.random.randint(8,18,(4,4,4))
print(random.choice(r10)) 
print(np.random.choice(r10)) 
print(np.random.permutation(r3))


# ***************string******************
dream="I want to bulild Sultan Robort  "
future="This is my future and I Will "
print(np.char.add(dream,future))
print(np.char.upper(dream))
print(np.char.lower(future))
print(np.char.center(future,60,fillchar="*"))
print(np.char.split(dream))
print(np.char.splitlines("hello\nAI\nI am coming soon"))
str1="this is my dream"
str2="Artificial Intalligasnce"
print(np.char.join(["/",":"],[str1,str2]))
print(np.char.replace(str1,"this","who"))
print(np.char.replace(str1,"this","who is that and that"))
print(np.char.equal(str1,str2)) 
print(np.char.count(str1,"a"))
print(np.char.find(str1,"a"))




# *************Sorting*********************
arr=np.arange(1,10).reshape(3,3)
np.random.seed(20)
arr1=np.random.randint(1,9,(3,3))
print(np.sort(arr1))
print(np.sort(arr1,axis=1))
print(np.sort(arr1, axis=None))
arr2=np.arange(1,10)
print(np.sort(arr2)[::-1])
print(np.sort(arr1)[::-1])
print(np.argsort(arr))
arr1=arr[3,5].copy()



# ****************Linear Algebra*************
ln=np.arange(1,10).reshape((3,3))
ln1=np.arange(1,10).reshape((3,3))
print("Rank of the matrix",np.linalg.matrix_rank(ln))
print(np.trace(ln))
print(np.linalg.det(ln))
print(np.linalg.inv(ln))
print(np.linalg.matrix_power(ln, 3))
# -------------------y=mx+c using this formula
coff=np.array([[1,2],[3,4]])
cont=np.array([8,3])
print("linear equation solution",np.linalg.solve(coff,cont))
print(np.dot(ln,ln1))
print(np.vdot(ln,ln1))
print(np.inner(ln,ln1))
print(np.outer(ln,1))
print(np.outer(ln,[2,3]))
print(np.linalg.norm(ln))
print(np.linalg.norm(ln,'fro'))
print(np.linalg.norm(ln,np.inf))
print(np.linalg.norm(ln,-np.inf))
print(np.linalg.cond(ln))
print(np.linalg.cond(ln,'fro'))
print(np.linalg.cond(ln,np.inf))
print(np.linalg.cond(ln,-np.inf))
print(np.multi_dot([ln,ln1]))
dilonall=np.array([2,3,5,7])
print(np.diag(dilonall))
print(np.where(ln<4,ln,5*ln))





# *************************numpy.mashgrid(variable_1,variable_2)
# ///////mashgrid id the function of the numpy module which is shows the matplotlib grapph with different numbers to different colors



# *****************numpy.histrogram(variable)**********************
# //////this function is use to the count the frequancy(how many are present there) of the elements 



# ***************numpy.pad(variable_name)*************************
# //////thius function is use when we want to add some arguments as the first or last of the array
# //////pad means to spaces






