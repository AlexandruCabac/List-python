a=b=c=d=[]
with open('input.txt','r')as f:
    a.extend(f.readline().split())
for i in range(0, len(a)):
    a[i]=int(a[i])
b=sorted(a)
c=sorted(a,reverse=True)
d=a+[111]
with open('output.txt','w')as f:
    f.write("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}".format(a, b, c, len(a), max(a), min(a), d,'\n'))
    a.insert(1,222)
    f.write("{}".format(a))