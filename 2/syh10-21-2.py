a=[1,2,3,4,5,6]
ttp=0
tmp=0
for i in range(0,len(a)):
    ttp=i
    for j in range(i,len(a)):
        if a[ttp]<a[j]:
            tmp=a[ttp]
            a[ttp]=a[j]
            a[j]=tmp
for i in range(0,len(a)):
    print(a[i])

    print('Hello,World!')

print("  *")
print(" ***")
print("*****")
print(" ***")
print("  *")

a=input().split()
print(int(a[0])+int(a[1]))

a=input();
print("  "+a)
print(" "+a+a+a)
print(a+a+a+a+a)

a=input().split()
print(int(a[0])*int(a[1]))

a=input()
print(a.upper())

x = input()
print(x[::-1])

a, num = map(float, input().split())
print("%.3f" % (a / num))
print("%d" % (2 * num))

a, b, c = map(float, input().split())
p = (a + b + c) / 2
S = p * (p - a) * (p - b) * (p - c)
print("%.1f"%(S * 0.5))

def isge(x):
    if 0 <= x < 10:
        return "0" + str(x)
    return str(x)

a, b = map(int, input().split())
c, d = divmod(a, b)
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

s=input().split()
h,r=int(s[0]),int(s[1])
v1=(3.14159*r*r*h)/1000
if 20%v1 == 0:
    n=20//v1
else:
    n=1+(20//v1)
print("%d" % n)        


begin_h, begin_m, end_h, end_m = map(int, input().split())
last_h = end_h - begin_h
last_m = end_m - begin_m
if last_m < 0:
    last_m += 60
    last_h -= 1
print("%d %d" % (last_h, last_m))

a, b = map(int, input().split())
print((10*a+b)//19)

A, B, C = map(int, input().split())
print("%d"%(0.2*A+0.3*B+0.5*C))
