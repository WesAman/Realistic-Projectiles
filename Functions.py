#A program to plot solutions using RK4 Method (step manually set)
#Import the necessary libraries
import matplotlib.pyplot as plt #Necessary to plot stuff
from numpy import * #For things like pi, linspace, etc
#constants:
g=9.81 #grav constant on earth
m =50 #mass
v_o = 100 #initial velocity
def f(r): # ODE
#if wind is zero
placeholder = np.zeros(2)
placeholder[0] = 0
placeholder[1] = -g
return placeholder
def trajectory(theta, Vo):
#initialize r --> x and y pos and velocity of x&y
r = np.zeros(2)
r[0] = Vo * np.cos(np.degrad(theta)) #x component traj times initial Vel
r[1] = Vo * np.sin(np.degrad(theta)) #y component traj times initial Vel
return r
def projectilemotion(h,theta):
#Function that finds motion of projectile from definitions states whilst in air
#h == unit/step length
#theta == initial shooting angle
#will return xlist and y list: which will be the array of x pos and y pos.
r = trajectory(theta,v_o)
X_list = np.zeros(0)
Y_list = np.zeros(0)
while w[1] >= 0:
w=RK4Meth(f,r,h)
X_list = np.append(X_list, w[0])
Y_list = np.append(Y_list, w[1])
return X_list, Y_list
#Define a function to handle the RK4 Method update
def RK4Meth(f, r, h):
k1 = f(r)
k2 = f(r + (h/2) * k1)
k3 = f(r + (h/2),* k2)
k4 = f(r + h, k3)
return r + h/6 * (k1 + (2*k2) + (2*k3) + k4) #returns approx of r at time t+h)
#Plot that stuff
plt.figure()
plt.plot(X_list, Y_list, 'bo')
plt.show()
