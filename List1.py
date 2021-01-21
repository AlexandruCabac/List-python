a=b=c=d=[]
with open('input.txt','r')as f:
    a.extend(f.readline().split())
for i in range(0, len(a)):
    a[i]=int(a[i])
b=sorted(a)
c=sorted(a,reverse=True)
d=a+[111]
e=["lista1: ","lista2: ","lista3: ","lista4: ","lista5: ","numarul de elemente din lista: ","numarul MAX: ","numarul MIN: "]
with open('output.txt','w')as f:
    f.write("{8}{0}{7}{9}{1}{7}{10}{2}{7}".format(a, b, c, len(a), max(a), min(a), d,'\n',e[0],e[1],e[2]))
    f.write("{5}{0}{4}{6}{1}{4}{7}{2}{4}{8}{3}{4}".format(len(a), max(a), min(a), d,'\n',e[3],e[5],e[6],e[7]))
    a.insert(1,222)
    f.write("{1}{0}".format(a,e[4]))