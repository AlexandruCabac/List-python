i=p=0
with open('input.txt','r')as f:
    a=list(f.readline())
for k in range(len(a)):
    if(int(a[k])==0 or int(a[k])%2==0):
        p+=1
    else:
        i+=1
with open('output.txt','w')as f:
    c1="Numarul cifrelor impare sunt"
    c2="Numarul cifrelor pare sunt"
    f.write("{0}{1}{2}{3}{4}".format(c1,i,'\n',c2,p))