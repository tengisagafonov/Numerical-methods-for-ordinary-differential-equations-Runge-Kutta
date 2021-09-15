import numpy as np
import matplotlib.pyplot as plt

def runge(f1,f2,y0_1,y0_2,t,c,a,b):
    y1 = np.zeros(len(t))
    y2 = np.zeros(len(t))

    k1 = np.zeros(len(c))
    k2 = np.zeros(len(c))

    #Initial condition
    y1[0] = y0_1
    y2[0] = y0_2
    tmp1=1
    tmp2=1

    h=t[1]-t[0]
    for n in range(0,len(t)-1):
        for i in range(0, len(c)):
            k1[i]=f1(y1[n] +h*a.sum(axis=1)[i]*tmp1 ,y2[n] + h * a.sum(axis=1)[i] * tmp2, t[n]+c[i]*h)
            k2[i]=f2(y1[n] +h*a.sum(axis=1)[i]*tmp1, y2[n] + h * a.sum(axis=1)[i] * tmp2, t[n]+c[i]*h)
            tmp2=k2[i]
            tmp1=k1[i]
        y1[n+1] = y1[n] +np.dot(k1, b)*h
        y2[n+1] = y2[n] +np.dot(k2, b)*h
        tmp1=1
        tmp2=1
    return y1,y2

#---- Butcher tableu
a=np.tril([[0,0,0,0],[1/2,0,0,0],[0,1/2,0,0],[0,0,1,0]])
c=[0,1/2,1/2,1]
b=[1/6,1/3,1/3,1/6]
#---- Stays for Butcher tableau

#--- Initial conditions
y0_1=0
y0_2=1

t = np.linspace(0,400,2000)

f1 = lambda y1,y2,t: y2
f2 = lambda y1,y2,t: -0.002*y1

y = runge(f1,f2,y0_1,y0_2,t,c,a,b)

plt.plot(t,y[0],'b-',t,y[1],'r-')
plt.legend(['p','q'])
plt.axis([0,400,-50,50])
plt.grid(True)
plt.xlabel("t-Axes")
plt.show()
