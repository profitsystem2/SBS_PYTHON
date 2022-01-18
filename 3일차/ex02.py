import random as r
import math as m
a=[]
s=0
A=[]
B=[]
C=[]
F=[]
x=[]
for i in range(0,1000):
    k=r.randint(0,100)
    a.append(k)
for i in range(0,1000):
    if a[i]>=90:
        A.append(a[i])
    elif a[i]>=80:
        B.append(a[i])
    elif a[i]>=70:
        C.append(a[i])
    else:
        F.append(a[i])    
    s+=a[i]
q=len(A)/10
w=len(B)/10
e=len(C)/10
t=len(F)/10
av=s/1000
for i in range(0,1000):
    m=a[i]-av
    n=m**2
    x.append(n)
X=sum(x)
O=X/1000
o=O**0.5
    
print('%3d명이 A등급입니다 상위%.2f%%입니다.'%(q*10, q))
print('%3d명이 B등급입니다 상위%.2f%%입니다.'%(w*10, q+w))
print('%3d명이 C등급입니다 상위%.2f%%입니다.'%(e*10, q+w+e))
print('%3d명이 F등급입니다 상위%.2f%%입니다.'%(t*10, t))
print('평균은 %.2f점, 표준편차는%.2f점입니다.'%(av,o))