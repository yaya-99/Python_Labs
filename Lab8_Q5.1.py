n= int(input('enter the length of list: '))
l=[]
for i in range(0,n):
    s=input('enter a string: ')
    l.append(s)
samp= input('enter sample string: ')
for i in l:
    c= l.count(samp)
print(c)