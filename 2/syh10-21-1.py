a=[1,2,3,4,5,6]
ttp=0
tmp=0
for i in range(0,len(a)):
    ttp=i
    for j in range(0,len(a)-i-1):
        if a[j+1]>a[j]:
           tmp=a[j+1]
           a[j+1]=a[j]
           a[j]=tmp
for i in range(0,len(a)):
   print(a[i])
