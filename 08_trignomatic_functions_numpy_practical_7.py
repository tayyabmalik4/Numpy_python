# *******************trignomatic functions in numpy**************
# //////sin(),cos(),tan() functions using numpy as python
# /////if we want to plot the graph than we use matplotlib 
# /////matplotlib is a python module which we use to plotting the graph using values
# ********NOTE(sec,cosec,cot values are not defined in this case)




import numpy as np
import matplotlib.pyplot as plt
# /////using sin value
# /////sin(angle_value)
val=np.sin(180)
# print(val)
val1=np.sin(90)
# print(val1)
# //////if we want to get value in radian than (angle * np.pi/180)



# //////getting cos vlaue in radian
# *********np.pi=3.14
val2=np.cos(180 * np.pi/180)
# print(val2)

# ///////starting tan value
val3=np.tan(180)
# print(val3)

# ///////starting arcsin value
val4=np.arcsin(0.23344)
# print(val4)

# ///////starting arccos value
val5=np.arccos(0.1234142)
# print(val5)

# ///////starting arctan value
val6=np.arctan(180)
# print(val6)

# /////to plotting the graph we required the 2 arrays 
# /////creating first value in sin 
# /////first value is shows starting 2nd value is shows ending and 3rd value is showing sequance of starting and ending values
# //////creating 1d array
x_sin=np.arange(0,3*np.pi,0.1)
# print(x_sin)

# //////starting sin value
y_sin=np.sin(x_sin)
# print(y_sin)

# ////starting cos value
y_cos=np.cos(x_sin)
# print(y_cos)

# /////starting tan value
y_tan=np.tan(x_sin)
# print(y_tan)

# ////starting arcsin value
# y_arcsin=np.arcsin(x_sin)
# print(y_arcsin)

# ////starting arccos value
# y_arccos=np.arccos(x_sin)
# print(y_arccos)

# ////starting arctan value
# y_arctan=np.arctan(x_sin)
# print(y_arctan)


# //////// plootiny the graph using matplotlib module
# --------------format-----------plt.plot(1st_val_trignomatry,2nd_val_trignomatry)
# /////plotting graph for sin
# plt.plot(x_sin,y_sin)
# plt.show()

# ////plotting graph for cos
# plt.plot(x_sin,y_cos)
# plt.show()


# ////////plotting graph for tan
# plt.plot(x_sin,y_tan)
# plt.show()

# /////plotting graph for arcsin
# plt.plot(x_sin,y_arcsin)
# plt.show()


# /////plotting graph for arcsin
# plt.plot(x_sin,y_arccos)
# plt.show()


# /////plotting graph for arctan
# plt.plot(x_sin,y_arctan)
# plt.show()


# /////when we want to convert the angle from radian to degree
# print(np.degrees(x_sin))


# /////when we want to convert the angle from degree to radian
# print(np.deg2rad(x_sin))
# print(np.radians(x_sin))


# ////when we want to determine the hypotanious of the right angle triangle
# -------formula-------hypotanious=(sqrt(base**2+perpendicular**2))
base=[10,2,5,50]
per=[3,10,23,6]
hyp=np.hypot(base,per)
# print(hyp)


# //////rounds the values if the input in flost than we want to convert the integer than we use these functions
r=np.array([0.23,0.9,1.56,1.5,9.99,1.1])
print(r)
# ////////if we want to vales are must to upper than we use ceil function
print(np.ceil(r))
# ////////if we want to wish that the values are must floor than we use floor function
print(np.floor(r))
print(np.fix(r))
print(np.trunc(r))
# ///////if we want to wish that which values is less than 0.5 then goes to floor and who is greater than 0.5 it goes to ceil than we use this function
# //////and this is the also the mathematics rule
print(np.round(r))
# //////rint also use as the round function
print(np.rint(r))