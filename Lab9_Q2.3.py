n1 = int(input('enter the length of 1st list: '))
n2 = int(input('enter the length of 2nd list: '))
l1=[]
l2=[]
s= set()
for i in range (0,n1):
    x= int(input('enter a integer for 1st list: '))
    if x<0:
        print('invalid input')
    else:
        l1.append(x)
for i in range(0,n2):
    y=int(input('enter elements of 2nd list: '))
    if y<0:
        print('invalid')
    else:
        l2.append(y)
print(l1)
print(l2)
for i in l1:
    print(i)
    if i in l1 and i in l2:
        s.add(i)
print(s)