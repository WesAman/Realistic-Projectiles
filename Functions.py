import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
g = 9.81  # gravitational constant on Earth (m/s^2)
m = 50    # mass (kg)
v_o = 100  # initial velocity (m/s)

def f(r, theta):
    # ODE for projectile motion with gravity only
    ax = 0  # No acceleration in x due to no air resistance considered
    ay = -g  # Acceleration in y is due to gravity
    return np.array([r[2], r[3], ax, ay])

def trajectory(theta, Vo):
    # Initialize r --> x and y position and velocity components of x&y
    return np.array([0, 0, Vo * np.cos(np.deg2rad(theta)), Vo * np.sin(np.deg2rad(theta))])

def projectilemotion(h, theta):
    # Function that finds the motion of the projectile
    r = trajectory(theta, v_o)
    X_list, Y_list = [], []
    while r[1] >= 0:
        r = RK4Meth(r, theta, h)
        X_list.append(r[0])
        Y_list.append(r[1])
    return X_list, Y_list

def RK4Meth(r, theta, h):
    # RK4 method to update the projectile's position and velocity
    k1 = f(r, theta)
    k2 = f(r + 0.5 * h * k1, theta)
    k3 = f(r + 0.5 * h * k2, theta)
    k4 = f(r + h * k3, theta)
    return r + h / 6 * (k1 + 2*k2 + 2*k3 + k4)

# Example usage:
theta = 45  # launch angle in degrees
h = 0.1  # time step in seconds

X_list, Y_list = projectilemotion(h, theta)

# Plot the trajectory
plt.figure()
plt.plot(X_list, Y_list, 'bo-')
plt.title('Projectile Motion Trajectory')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.grid(True)
plt.show()
