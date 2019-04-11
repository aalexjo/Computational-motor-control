# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:35:35 2019

@author: Alexander

For a given set of attachment points, compute and plot the muscle length and
moment arm as a function of θ between[−π/4,π/4]using equations in eqn:3 and
discuss how it influences the pendulum resting position and the torques muscles
can apply at different joint angles. You are free to implement this code by yourself
as it does not have any other dependencies.

"""

import numpy as np
from matplotlib import pyplot as plt

a1 = 0.17
a2 = 0.17

theta = np.arange(-np.pi/4, np.pi/4, 0.001)

L = np.zeros(len(theta))
h = np.zeros(len(theta))

for i in range(len(theta)):
    L[i] = np.sqrt(pow(a1,2) + pow(a1,2) + 2*a1*a2*np.sin(theta[i]))
    h[i] = a1*a2*np.cos(theta[i])/L[i]


plt.figure('Length')
plt.title('Muscle length')
plt.plot(theta,L)
plt.ylabel('Length [m]')
plt.xlabel('θ [rad]')
plt.grid()

plt.figure('Moment arm')
plt.title('Moment arm')
plt.plot(theta,h)
plt.ylabel('Moment arm [m]')
plt.xlabel('θ [rad]')
plt.grid()