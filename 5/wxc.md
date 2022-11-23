### 洛谷：P5743	【深基7.习8】猴子吃桃	P5744	【深基7.习9】培训       P5461	赦免战俘      P2415 集合求和
         P5461	赦免战俘（主要是一开始犹豫如何实现递归，因为每次递归之后，剩下的三个小矩阵的首元素不好表示）
          1. 了解了什么是分治
           关于使用分治的条件：
              1 . 原问题规模通常比较大，不易直接解决，但问题缩小到一定程度就能较容易的解决。
              2 . 问题可以分解为若干规模较小、求解方式相同(似)的子问题。且子问题之间求解是独立的互不影响。
              3 . 合并问题分解的子问题可以得到问题的解。
          2. 最后将大矩阵化成1+3  其中其他三个，只要确定了小矩阵的首元素坐标，就可以表示出来
          P2415 集合求和（还是很明确的，集合的子集个数之前高中也都总结过，归纳最后得出，原集合的和*（2^0+2^1+......)
          好像之前没在洛谷上刷到利用scanf() 返回值的题 （浅浅再强化记忆一下） 
                             key:   while(scanf("%d",&num[i])!=EOF)
          (顺便看了C prime plus 上关于缓存区的内容）
          
### 接触到将浮点数转化为二进制数

### 小作业：
    大体思路： 
       1. 假设直线：y=theta0+theta1x
       2. 利用梯度下降法求得theta0,theta1 
           1). 构建一个代价函数：  
           2). 目标： 将关于(theta0,theta1) 的函数值最小化（利用梯度下降法）
       3. 注意 1）要是用矩阵相乘，要保持行列数的合理，为此在X矩阵添上 1，1···
               2）如果是迭代，注意同时更新theta0,theta1的值 
       4. 实现：
 迭代（纯手搓，就是结果呜呜和那个矩阵的有点小，啊不大差，，theta0偏大,theta1也偏大，增加了迭代次数，好像还不对，不知道为啥）：
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('ex1data1.txt', names=['x', 'y'])
X = df.iloc[:, 0]
Y = df.iloc[:, 1]
X = X.values.tolist()
Y = Y.values.tolist()
m = 97
def innerf1(theta0, theta1):
    sum = 0
    for i in range(97):
        sum= sum + (theta0+theta1*X[i]-Y[i])
        return sum/m
def sum1(theta0, theta1, X, Y):
    sum = 0
    i = 0
    for i in range(97):
        sum= sum + (theta0+theta1*X[i]-Y[i])*X[i]
        return sum/m

def gradientDescent(theta0, theta1, alpha, X, Y):
    tmp0 = theta0 - innerf1(theta0,theta1)*alpha
    tmp1 = theta1 - sum1(theta0,theta1,X,Y)*alpha
    theta0 = tmp0
    theta1 = tmp1
    t = [theta0, theta1]
    return t

theta0 = 0
theta1 = 0
alpha = 0.01
times = 1500
for i in range(1500):
    n = gradientDescent(theta0, theta1, alpha, X, Y)
    theta0 = n[0]
    theta1 = n[1]

print(theta0, theta1)


x = np.linspace(0, 25, 100)
y_ = theta0+theta1*x
fig, ax = plt.subplots()
ax.scatter(X, Y, label='raw data')
ax.plot(x, y_, 'r', label='predict outcome')
ax.legend()
ax.set(xlabel='population',
       ylabel='profit')
plt.show()

矩阵：
       ```c
         # time :2022/11/20  16:34
         import numpy as np
         import pandas as pd
         import matplotlib.pyplot as plt
         # 以csv的格式导入数据
         data = pd.read_csv('ex1data1.txt', names=['population', 'profit'])

         data.plot.scatter('population', 'profit')
         plt.show()
         # 构造数据集 X，y 并由DataFrame -> 数组
         data.insert(0, 'ones', 1)
         X = data.iloc[:, 0:2]
         y = data.iloc[:, 2]
         X = X.values
         y = y.values
         y = y.reshape(97, 1)

        # 损失函数
        def costf(X, y, theta):
        inner = np.power(X @ theta - y, 2)   # 矩阵相乘的.dot
        return np.sum(inner)/(2*len(X))  # len(X) 求的是样本数


        theta = np.zeros((2, 1))  # 初始化随意找一个theta0=0 ,theta1=0
        # 梯度下降
        def func(X, y, theta, alpha, times):
        costs = []
        for i in range(times):
        theta = theta - (X.T@(X@theta-y))*alpha/len(X)  # X*theta-y    # 这个相乘的矩阵公式没推出来···
        cost = costf(X, y, theta)
        costs.append(cost)
        return theta, costs  # 返回元组


       alpha = 0.01
       times= 1500
       theta, costs = func(X, y, theta, alpha, times)

        # 绘图 
       x = np.linspace(y.min(), y.max(), 100)
       y_ = theta[0, 0]+theta[1, 0]*x

      fig, ax = plt.subplots()
      ax.scatter(X[:, -1], y, label='raw data')
      ax.plot(x, y_, 'r', label='predict outcome')
      ax.legend()
      ax.set(xlabel='population',
       ylabel='profit')
       plt.show()
       
       ```
         
