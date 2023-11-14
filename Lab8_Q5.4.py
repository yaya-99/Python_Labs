n = int(input('enter the length of list: '))
l=[]
for i in range(0,n):
    s=input('enter a string: ')
    if s[0].islower():
        l.append(s)
    else:
        s.upper()
        l.append(s)
print(l)
