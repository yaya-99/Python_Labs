n= int(input('enter the length of string:  '))
l=[]
for i in range (0,n):
    x= int(input('enter a positive integer: '))
    if x<0:
        print('invalid input')
    else:
        l.append(x)
print(l)
u= []
for i in l:
    if i not in u:
        u.append(i)

print(u)

