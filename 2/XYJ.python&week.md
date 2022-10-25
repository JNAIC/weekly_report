# 冒泡排序
s1 = input().split ()
arr = list(map(int, s1))
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1): 
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
arr

# 选择排序
s1 = input().split ()
arr = list(map(int, s1))
n = len(arr)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if arr[min]>arr[j]:
            min = j
        
    arr[i],arr[min] = arr[min],arr[i]
arr

# 本周总结
梦游的一周,唯一学到的就是会用github提交周报和写md格式
# 下周计划
从飞桨上找找慕课学学机器学习中的线性回归
