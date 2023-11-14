n= int(input('enter the no. of numbers: '))
l= []
s=0
p=1
for i in range(0,n):
    x = int(input('enter the integers: '))
    l.append(x)
print(l)
for i in l:
    s=s+i
    p=p*i
print(f'sum is {s}')
print(f'product is {p}')
print(max(l))
for i in l:
    for j in range(0,n):
        m= l[0]
        if m<l[j]:
            m= l[j]
print(f'largest elememt is {m}')