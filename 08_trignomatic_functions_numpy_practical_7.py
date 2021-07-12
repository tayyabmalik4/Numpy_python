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


