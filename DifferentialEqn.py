import matplotlib.pyplot as plt #Necessary to plot stuff
import numpy as np
import math
from numpy import * #For things like pi, linspace, etc
def f(t, v, g, m, k):
    kmv = np.linalg.norm(v)*(k/m)
    return (g - kmv*v)
def RK4(tn, xn, vn, h, g, m, k):
    k1v = f(tn, vn, g, m, k)
    k2v = f(tn + h/2, vn + k1v*h/2, g, m, k)
    k3v = f(tn + h/2, vn + k2v*h/2, g, m, k)
    k4v = f(tn + h, vn + k3v*h, g, m, k)
    vn1 = vn + (k1v + 2*k2v + 2*k3v + k4v)*(h/6)
    k1x = vn
    k2x = vn + k1v*h/2
    k3x = vn + k2v*h/2
    k4x = vn + k3v*h
    xn1 = xn + (k1x + 2*k2x + 2*k3x + k4x)*(h/6)
    # xn1 = xn + vn*h + (k1v+k2v+k3v)*h**2/6
    return vn1, xn1
theta = math.radians(45)
initial_speed =20
v0= np.array([initial_speed * math.cos(theta), initial_speed * math.sin(theta)])
#set initial velocitie(s)
x0 = np.array([0, 0]) #set initial position(s)
t0 = 0
x = []
v = []
t = []
x.append(x0)
v.append(v0)
t.append(t0)
m = 1
k = 1
g = np.array([0, -1])
h = .01
tn = t0
vn = v0
xn = x0
#maxt = 1
#while (tn < maxt) and xn[1] >= 0:
while xn[1] >= 0:
    vn, xn = RK4(tn, xn, vn, h, g, m, k)
    tn = tn + h
    t.append(tn)
    x.append(xn)
    v.append(vn)
#ok lets seperate our x and y components by extracting it from v and x
x_values = transpose(x)[0]
y_values = transpose(x)[1]
vx_values= transpose(v)[0]
vy_values= transpose(v)[1]
print (t[-1])
print (x[-1])
print (v[-1])
plt.plot(x_values,y_values)
#figure, axis = plt.subplots(2, 2)
#axis[0, 0].plot(t, x_values)
#axis[0, 0].set_title('Time vs X-pos')
#axis[0, 1].plot(t, vx_values, 'tab:cyan')
#axis[0, 1].set_title('Time vs X-vel')
#axis[1, 0].plot(t, y_values, 'tab:blue')
#axis[1, 0].set_title('Time vs Y-pos')
#axis[1, 1].plot(t, vy_values, 'tab:cyan')
#axis[1, 1].set_title('Time vs Y Vel')
plt.show()
