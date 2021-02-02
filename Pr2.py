b=0
with open('input.txt','r')as f:
    a=list(f.readline())
for k in range(len(a)-1):
    if(int(a[k])<int(a[k+1])):
        b=1
    else:
        b=0
        break
with open('output.txt','w')as f:
    c1="Da"
    c2="Nu"
    if(b==0):
        f.write(c2)
    else:
        f.write(c1)