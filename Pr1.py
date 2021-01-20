a=b=c=d=[]
a.extend(input().split())
for i in range(0, len(a)):
    a[i]=int(a[i])
b=sorted(a)
c=sorted(a,reverse=True)
d=a+[111]
print(a, b, c, len(a), max(a), min(a), d, sep='\n')
a.insert(1,222)
print(a)
#a=[7,-3,4,1,0-8,-11123,3412]
#b=sorted(a)
#c=sorted(a,reverse=True)
#d=a+[111]
#print(a, b, c, len(a), max(a), min(a), d, sep='\n')
#a.insert(1,222)
#print(a)