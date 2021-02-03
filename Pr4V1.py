a=int(input())
n=' '
z=0
for i in range(2,a):
    x,y=i,a
    while(y!=x):
        if x>y:
            x=max(y,x)-min(x,y)
        else:
            y=max(y,x)-min(x,y)
        if(x==1 and y==1):
            n=n+' '+str(i)
            z+=1
print(z,n)