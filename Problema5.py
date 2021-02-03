n=int(input())
b=[]
for k in range(n):
    b.extend([int(input())])
    x,y,z=b[k]//100,(b[k]//10)%10,b[k]%10
print(x,y,z)