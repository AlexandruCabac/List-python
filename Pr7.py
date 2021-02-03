with open('input.txt','r')as f:
    n=int(f.readline())
    a=str(f.readline()).split()
z,b=0,[]
for i in range(n):
    b.extend(map(int,a[i]))
    if(b[0]+b[1]==13 and b[2]+b[3]==13):
        z+=1
    b.clear()
with open('output.txt','w')as f:
    f.write(str(z))