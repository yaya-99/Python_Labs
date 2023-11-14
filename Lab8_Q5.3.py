n= int(input('enter the length of list: '))
l=[]
for i in range(0,n):
    a=int(input('enter a no: '))
    l.append(a)
for i in l:
    if i in range(10,21):
        print(i*i)