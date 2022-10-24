# 吉兴琦的周报 

## 吉xq 22.10.24

## 一b2002
## import warnings
## print('Hello,World!')

## 二b2025
import warnings
print("  *")
print(" ***")
print("*****")
print(" ***")
print("  *")

## 三p1001
a=input().split()
print(int(a[0])+int(a[1]))

## 四b2005
a=input();
print("  "+a)
print(" "+a+a+a)
print(a+a+a+a+a)

## 五p5703
a=input().split()
print(int(a[0])*int(a[1]))

## 六p5704
a=input()
print(a.upper())

## 七p5705
x = input()
print(x[::-1])

## 八p5706
ml, num = map(float, input().split())
print("%.3f" % (ml / num))
print("%d" % (2 * num))

## 九p5708
a, b, c = map(float, input().split())
p = (a + b + c) / 2
S = p * (p - a) * (p - b) * (p - c)
print("%.1f"%(S ** 0.5))

## 十p5707
def isge(x):
    if 0 <= x < 10:
        return "0" + str(x)
    return str(x)

s, v = map(int, input().split())
div, mod = divmod(s, v)
if mod != 0:
    div += 1
div += 10
h, m = divmod(div, 60)
if m != 0:
    h += 1
hour = 8 - h
min = 60 - m
if hour < 0:
    hour += 24
print("%s:%s" % (isge(hour), isge(min)))

## 十一
s=input().split()
h,r=int(s[0]),int(s[1])
v1=(3.14159*r*r*h)/1000
if 20%v1 == 0:
    n=20//v1
else:
    n=1+(20//v1)
print("%d" % n)        


## 十二p1425
begin_h, begin_m, end_h, end_m = map(int, input().split())
last_h = end_h - begin_h
last_m = end_m - begin_m
if last_m < 0:
    last_m += 60
    last_h -= 1
print("%d %d" % (last_h, last_m))

## 十三p1421
a, b = map(int, input().split())
print((10*a+b)//19)

## 十四p3954
A, B, C = map(int, input().split())
print("%d"%(0.2*A+0.3*B+0.5*C))

## 冒泡排序
def bubble_sort(list):
    for i in range(0, len(list)):
        is_sorted = True
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_sorted = False
        if is_sorted:
            return        
list1 = [12, 52, 30, -64, -995, 786, 1, 520, 55, -78, 888, 10]  
bubble_sort(list1)
print(list1)

## 选择排序
def choose_sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        for j in range(i + 1, list_len):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

list1 = [35, 5, 85, -99, 454, -845, 454, 1, 44]    
choose_sort(list1)
print(list1)            
