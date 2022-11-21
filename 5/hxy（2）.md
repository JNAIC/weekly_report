# 本周周报 <br>
### 洪鑫宇 <br>

# 小任务 <br>
## 目标 <br> 
    由提供的数据集，通过学习梯度下降法，完成简单的线性回归问题
    
## 学习到的 <br>
*   在这个小任务中，已经提供了自变量与因变量之间是 <u>y=a*x+b</u> 这样线性的关系。所以需要我们解决的是如何找到这个拟合函数的a与b。
    
### 1.梯度下降法  
*   首先理解为什么要用梯度下降法，以及什么是梯度下降。其主要目的是通过迭代找到目标函数的最小值，或者收敛到最小值。
    
#### 1.1 梯度意义  
*   在多变量函数中，梯度是一个向量，向量有方向，梯度的方向指出了函数在给定点上升最快的方向。
*   在单变量函数中，梯度是函数的微分，代表在给定点的切线斜率。

#### 1.2 数学理解  
*   梯度是多变量的微分，例如：y=3-(5*x1 + 3*x2)，其梯度就是分别对x1和x2进行微分，得到dy = （-5，-3）这也说明了梯度是一个向量。
*   进一步理解，f(x)是关于x的函数，当前位置为x0，要从这个点走到f(x)的最小值点，那就要找到方向，也就是梯度的反向，然后走一定的步长，到达x1这个点，即x1=x0 + k*d(f(x)。
*   这里的k就被称为学习率，用以控制每一步的距离，太大会跨过最低点，太小会走的很慢。
*   由于梯度是函数上升最快的方向，所以在使用时要加上一个负号。

### 2.实际例子  
#### 2.2 代价函数
*   选用均方误差代价函数  ![截屏2022-11-21 19.37.43](assets/%E6%88%AA%E5%B1%8F2022-11-21%2019.37.43.png)形如这个式子，m代表着数据集个数，1/2这个常量是为了微分方便，h则表示我们的预测函数a*x+b，对于这个代价函数，**<u>分别对a和b微分得到这个代价函数的梯度向量</u>**
*   为了方便代码的编写，将所有的公式都转换为矩阵的形式，python中计算矩阵是非常方便的，同时代码也会变得非常的简洁。为了转换为矩阵的计算，我们观察到预测函数的形式是y=a*x+b，所以给每个x增加一维，并固定为1（这里关于矩阵化以及将代价函数和梯度转化为矩阵向量相乘的形式不太能理解）

#### 2.3 代码实现
*   数据集的导入：运用pandas将数据读入为dateframe，然后运用numpy，用tolist()将x列读入为列表，再转化为数组，生成向量。同理y也是如此。
*   matplotlib的使用，dot()。。，向量组的生成
*   ```from numpy import *
    import pandas as pd
    df=pd.read_csv("/Users/hxy/Downloads/ex1data1.csv")
    m = 97
    # x的坐标以及对应的矩阵
    X0 = ones((m, 1))  # 生成一个m行1列的向量，也就是x0，全是1
    x = df['x'].tolist()
    X1= array(x).reshape(m,1) # 生成一个m行1列的向量，也就是x1，从1到m
    X = hstack((X0, X1))  # 按照列堆叠形成数组
    # 对应的y坐标
    y = df['y'].tolist()
    Y = array(y).reshape(m,1)
    # 学习率,这里我调过，用了不同的学习率尝试了一下
    alpha = 0.02


    # 代价函数，矩阵向量的形式
    def cost_function(theta, X, Y):
        diff = dot(X, theta) - Y  # dot() 数组需要像矩阵那样相乘，就需要用到dot()
        return (1/(2*m)) * dot(diff.transpose(), diff)


    # 代价函数对应的梯度函数，也同样是矩阵向量的形式
    def gradient_function(theta, X, Y):
        diff = dot(X, theta) - Y
        return (1/m) * dot(X.transpose(), diff)


    # 梯度下降迭代
    def gradient_descent(X, Y, alpha):
        theta = array([1, 1]).reshape(2, 1)
        gradient = gradient_function(theta, X, Y)
        while not all(abs(gradient) <= 1e-5):
            theta = theta - alpha * gradient
            gradient = gradient_function(theta, X, Y)
        return theta
    #这里theta[0]就是b，theta[1]就是a，反复迭代的过程其实就是在学习，在向最低点不断靠近，当小于1e-5的时候，就近似认为是最低点了。

    optimal = gradient_descent(X, Y, alpha)
    print('optimal:', optimal)
    print('cost function:', cost_function(optimal, X, Y)[0][0])

    def plot(X, Y, theta):
        import matplotlib.pyplot as plt
        ax = plt.subplot(111)  
        ax.scatter(X, Y, s=30, c="black", marker="s")
        plt.xlabel("X")
        plt.ylabel("Y")
        x = arange(5.0269, 22.203, 0.2)  
        y = theta[0] + theta[1]*x
        ax.plot(x, y)
        plt.show()


    plot(X1, Y, optimal)
    ```
*   得到结果![截屏2022-11-21 20.13.40](assets/%E6%88%AA%E5%B1%8F2022-11-21%2020.13.40.png)

### 问题
*   假如并不知道预测函数形式，就只靠猜嘛。
*   关于代价函数，以及梯度的迭代感觉没真的理解进去，<u>大致流程是懂了，明白机器学习大致是个怎么操作方式了</u>。
*   还有关于矩阵向量在python里的运算是咋样的。
*   进一步要学数据的标准化和清洗等问题。
*   中间的代码块函数部分，照着敲的。   


