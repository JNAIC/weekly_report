import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

chu =np.loadtxt('D:\exdata1.txt',header=None)
x = np.array(chu.iloc[:, 0],dtype=np.float)
y = np.array(chu.iloc[:, 1],dtype=np.float)
N=len(x)
rate=0.0001
ci=100000
w=x[0]/y[0]
b=0
def loss(x,y,w,b):
    return np.sum((w*x+b)-y)**2/(2*N)#损失函数
def graloss(x,y,w,b):
    return (np.sum(w*x*x+b*x-y*x)/N,np.sum((w*x+b-y))/N)#导数
def gradient_descent(x,y,w,b,rate,ci):           
    for i in range(ci):
        w=w-rate*graloss(x,y,w,b)
        b=b-rate*graloss(x,y,w,b)
          
    return w,b

w,b=gradient_descent(x,y,w,b,rate,ci)
print(w,b)
plt.scatter(x,y,s=50,c='c')
plt.plot(x,w*x+b)
plt.show()