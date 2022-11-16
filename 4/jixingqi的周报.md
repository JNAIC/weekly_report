# 吉兴琦的周报 

## 吉xq 22.11.13

## 本周阅读：0

## 本周工作
注册kaggle，看了pandas，发现完全看不懂。
开始搞钱佬的小任务了，只能完成第一步用pandas导入数据并绘制散点图，线性回归线正在努力
luogu题单暂时未写

## 上周周考感想
直到真正开始考试才知道自己多水，6题就会一两道，对于c'和py的编程基础还是太少，需要多用心


## 下周计划
先把课内搞搞，再继续py+kaggle

## 小任务代码
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_table(r"ex1data1.txt",sep = ",",header=None)
data.columns = ({'x','y'})
print(data.head(98)) 
plt.scatter(data.x,data.y)  
plt.show()