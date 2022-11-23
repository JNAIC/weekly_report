### 本周通过观看梯度下降算法有关的慕课和博客,初步了解梯度下降

#### 梯度下降算法思路

#因为梯度是函数上升最快的方向，所以如果我们要寻找函数的最小值，只需沿着梯度的反方向寻找即可

#小任务(尝试了N次,各种报错)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#读取数据
df = pd.read_csv('./train.txt',sep=' ')
x = df.iloc[:,0]
y = df.iloc[:,1]

alpha = 0.001
#上面提到alpha,又叫步长，它决定了为了找到极小值点而尝试在目标函数上前进的步伐到底走多大。步长必须由外界制定，这种需要人为设定的参数，叫超参数。步长参数是梯度下降算法中非常重要的超参数。这个参数设置的大小需要合适。
#步长太大，可能会找不到最低点
#步长太小，需要的迭代次数多，相应需要的运算时间也就越多

#设定初始k,b,下降次数
b = 0
k = 0
n = 200

#损失函数
def compute_mse(x,y,k,b):
     mse = np.sum((y-(k*x+b))**2)/len(x)/2
     return mse


#梯度下降
def gradient_descent(x,y,k,b,learning_rate,n_iterables):
    m = len(x)
    start_loss = compute_mse(x,y,k,b)
    #初始损失函数
    loss_value = [start_loss]
    for i in range(n):
        #求偏导
        b1 = np.sum((k*x+b)-y)/m
        k1 = np.sum(((k*x+b)-y)*x)/m
        #更新b、k（减去偏导乘以步长）
        b = b - (learning_rate*b1)
        k = k - (learning_rate*k1)
        #损失函数的值越来越小
        loss_value.append(compute_mse(x,y,k,b))
        #输出每一步的斜率和截距,发现其逐渐收敛
        print(b,k)     
    return b,k,np.array(loss_value)
#调用函数
b1,k1,loss_list = gradient_descent(x,y,k,b,learning_rate,n_iterables)
y_predict = k1*x+b1
print(b1,k1)
#最后画图
plt.scatter(x,y)
plt.plot(x,y_predict)
