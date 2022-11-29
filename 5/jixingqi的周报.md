# 吉兴琦的周报 

## 吉xq 22.11.20

## 本周阅读：CSDN中关于最小二乘法和梯度下降法的相关内容

## 本周工作
注册kaggle，看了pandas，发现完全看不懂。
开始搞钱佬的小任务了，目前完成了，但教麻烦。
luogu题单暂时未写
## 思路：设预测后的直线方程，按两个系数分别求偏差，将这作为梯度进行梯度下降，将所有数据导入矩阵中，利用矩阵乘法来求相关数据


## 下周计划
先把课内搞搞，再继续py+kaggle

## 小任务代码
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_table(r"ex1data1.txt",sep = ",",header = None)
data.columns = ({'x','y'})

a = 0.01
m = 97

x0 = np.ones((m,1))
x1 = np.array(data.x).reshape(m, 1)
X = np.hstack((x0, x1))
Y = np.array(data.y).reshape(m, 1)

def tidu_1(theta, X, Y):
    hy = np.dot(X, theta) - Y
    return (1./m) * np.dot(np.transpose(X), hy)

def tidu_diedai(X, Y, a):
    theta = np.array([1, 1]).reshape(2, 1)
    tidu = tidu_1(theta, X, Y)
    while not np.all(np.abs(tidu) <= 1e-5):
        theta = theta - a * tidu
        tidu = tidu_1(theta, X, Y)
    return theta

theta = tidu_diedai(X,Y,a)
x = np.arange(5,30,1)
y = theta[0] + theta[1]*x

print(data.head(97)) 
plt.scatter(data.x,data.y,s=30,c="b",marker="s")  
plt.plot(x,y,'black')
plt.show()
```

