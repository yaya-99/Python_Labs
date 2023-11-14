n= int(input('enter the length of list: '))
l=[]
for i in range(0,n):
    a=int(input('enter a no: '))
    l.append(a)
print(l)

for i in l:
    h=0
    while h <n:
        m= l[h]
        
        if m>l[n-1]:
            m= l[n-1]
        l[0]=m
        l.remove(m)
        h=h+1
        n=n-1
        
            

print(l)