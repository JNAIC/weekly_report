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
