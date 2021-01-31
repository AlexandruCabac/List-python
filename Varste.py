#a=["Mihai","George","Ana","Dan","Ion","Geta","Vio"]
#b=[14, 23, 15, 14, 12, 41, 39]
with open('list.txt','r')as f:
    a=eval(f.readline())
    b=eval(f.readline())
for i in range(len(a)):
    print("{}{}{}".format(a[i],' are vârsta de ',b[i]))
a.extend(["Andreea","Ioan"])
b.extend([34,23])
print(a,'\n',b)
c=a.index("Ana")
del(a[c],b[c])
print(a[:3],'\n',a[::-1])
print(a[2],b[2],'\n',a[4],b[4],'\n',a[0:6],b[0:6])
#with open('list.output.txt','w')as f:
#    c=" are varsta de "
#    for i in range(len(a)):
#        f.write("{}{}{}".format(a[i],c,b[i]))
#    a.extend(["Andreea","Ioan"])
#    b.extend([34,23])
#    f.write("{}{}{}".format(a,'\n',b))
#    c=a.index("Ana")
#    del(a[c],b[c])
#    f.write("{}{}{}".format(a[:3],'\n',a[::-1]))
#    f.write("{0}{1}{2}{3}{4}{2}{5}{2}{6}".format(a[2],b[2],'\n',a[4],b[4],a[0:6],b[0:6]))