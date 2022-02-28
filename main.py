import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    y = -x**3-2*np.cos(x)
    return y
A=-2
B=2
NUM_POINTS=100
x=np.linspace(A,B,NUM_POINTS)
y=func1(x)
plt.figure(0)
plt.plot(x,y,label='f(x)')
plt.axhline(0,c='black')
plt.axvline(0,c='black')
plt.xlabel('x')
plt.ylabel('f(x)=y')
plt.grid()
plt.legend()
plt.show()

def dfunc1(x):
    y=-3*x**2+2*np.sin(x)
    return y

def newton_raphson(f,df,x0,eps):
    k=0
    conditie=eps
    while conditie>=eps:
        k=k+1
        x_new=x0-f(x0)/df(x0)
        conditie=np.abs(x_new-x0)/np.abs(x0)
        x0=x_new
    return x_new,k

X0=-2
EPS=1e-5
x_num,nr_iteratii=newton_raphson(f=func1,df=dfunc1,x0=X0,eps=EPS)
print(f'Solutia ecuatiei f(x)=0 cu metoda Newton Raphson este x_sol={x_num:.8f} gasita in N={nr_iteratii} pasi.')