import numpy as np
import matplotlib.pyplot as plt

a=0
b=10

alpha=1
beta=2

t =np.linspace(0,10,800)
h=t[1]-t[0]

f = lambda dy,y,t: -2*y-dy

y0=np.zeros(len(t))
y1=np.zeros(len(t))
z0=np.zeros(len(t))
z1=np.zeros(len(t))

s=1
y0[a]=alpha
y1[a]=s

z0[a]=0
z1[a]=1

while abs(y0[len(t)-1]-beta)>0.001:
    for i in range(0, len(t) - 1):
        y0[i+1]=y0[i]+h*y1[i]
        y1[i + 1] = y1[i] + h *f(y1[i],y0[i],t[i])
        f2=(f(y1[i]+h, y0[i], t[i])- f(y1[i],y0[i],t[i]))/h
        f1=(f(y1[i],y0[i]+h,t[i])-f(y1[i],y0[i],t[i]))/h
        z0[i+1] = z0[i] + h* z1[i]
        z1[i+1] = z1[i] + h*(f1*z0[i]+f2*z1[i])
    s=s-(y0[len(t)-1]-beta)/z0[len(t)-1]
    y1[0] = s

print(s)
plt.plot(t,y0,'r.-')

plt.axis([-10,50,-20,20])
plt.grid(True)

plt.show()
