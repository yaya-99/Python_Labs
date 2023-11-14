n= int(input('enter the length of list: '))
l=[]
for i in range(0,n):
    a= int(input('enter the numbers of list: '))
    l.append(a)
print(l)
s=[]
for i in l:
    h=0
    while h <n:
        m= l[0]
        
        if m>l[n-1]:
            m= l[n-1]
        s.append(m)
        l.remove(m)
        h=h+1
        n=n-1
        
            
s.append(l[0])       
print(f'sorted list is {s}')