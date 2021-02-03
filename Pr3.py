import sys,math
a=sys.maxsize
for i in range(a+1):
    b=[]
    b.extend(str(i))
    d=0
    for k in range(len(b)):
        d+=math.factorial(int(b[k]))
    b.clear
    if(d==i):
        print(i)