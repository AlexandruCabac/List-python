def gcd(x, z): 
    if x==0:
        return z
    return gcd(z%x, x)
a=int(input())
n=' '
z=0
for i in range(2,a):
    if(gcd(i,a)==1):
        z+=1
        n=n+' '+str(i)
print(z,n)