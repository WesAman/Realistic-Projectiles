import matplotlib.pyplot as plt
import numpy as np
import math
#FEEL FREE TO MODIFY ANY OF THESE INITAL PARAMETERS/CONDITIONS 
AngleRadian = 0.0
InitialSpeed = 0.0
Mass = 0.0
LiftCoefficient = 0.0
TerminalSpeed = 0.0
Gravity = np.array([0, 0])
Timestep = 0.0001
TimeInitial = 0.0
AngleRadian = math.radians(30)
InitialSpeed = 2
Mass = 1
TerminalSpeed = 1
LiftCoefficient = 0.25
Gravity = np.array([0, -9.8])
Timestep = 0.0001
OptionsArray = [1]
#end initial parameters/conditions


#initialize the program with starting conditions
x = []
v = []
t = []

#set initial velocities (s)
VelocityInitial = np.array([InitialSpeed * math.cos(AngleRadian), InitialSpeed * math.sin(AngleRadian)])

#set Initial position(s)
PositionInitial = np.array([0, 0])
x.append(PositionInitial)
v.append(VelocityInitial)
t.append(TimeInitial)
Time = TimeInitial
Velocity = VelocityInitial
Position = PositionInitial

x_values = np.transpose(x)[0]
y_values = np.transpose(x)[1]
vx_values = np.transpose(v)[0]
vy_values = np.transpose(v)[1]
print(t[-1])
print(x[-1])
print(v[-1])
plt.plot(x_values, y_values)

#functions
def f(t, V, G, M, K, L):
    Lift = 0
    Drag = (np.linalg.norm(V)*(K/M)) * V
    NetForce = G - Drag
    if OptionsArray[0] == 1:
        Lift = np.empty_like(Drag)
        Lift[0] = -Drag[1]
        Lift[1] = Drag[0]
        Lift = L*Lift
        NetForce = NetForce + Lift
    return (NetForce)

def RK4(Time, Position, Velocity, TimeStep, Gravity, Mass, TerminalSpeed, LiftCoefficient):
    k1v = f(Time, Velocity, Gravity, Mass, TerminalSpeed, LiftCoefficient)
    k2v = f(Time + TimeStep/2, Velocity + k1v*TimeStep/2, Gravity, Mass, TerminalSpeed, LiftCoefficient)
    k3v = f(Time + TimeStep/2, Velocity + k2v*TimeStep/2, Gravity, Mass, TerminalSpeed, LiftCoefficient)
    k4v = f(Time + TimeStep, Velocity + k3v*TimeStep, Gravity, Mass, TerminalSpeed, LiftCoefficient)
    RK4Velocity = Velocity + (k1v + 2*k2v + 2*k3v + k4v)*(TimeStep/6)
    k1x = Velocity
    k2x = Velocity + k1v*TimeStep/2
    k3x = Velocity + k2v*TimeStep/2
    k4x = Velocity + k3v*TimeStep
    RK4Position = Position + (k1x + 2*k2x + 2*k3x + k4x)*(TimeStep/6)
    return RK4Velocity, RK4Position

