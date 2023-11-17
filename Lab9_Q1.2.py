n= int(input('enter the length of string:  '))
l=[]
for i in range (0,n):
    x= int(input('enter a positive integer: '))
    if x<0:
        print('invalid input')
    else:
        l.append(x)
print(l)
s= set(l)
print(s)
print(sorted(s))