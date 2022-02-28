import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    y=-x**3-2*np.cos(x)
    return y
A=-2
B=2
NUM_POINTS=100
x=np.linspace(A,B,NUM_POINTS)
y=func1(x)
plt.figure(0)