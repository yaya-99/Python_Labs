s = str(input('enter a hyphen sep string:'))
s = s.replace('-',' ')
s= s.split()
print(s)
l= len(s)

i=0
a=['-']
while i <l:
    x = min(s)
    a.append(x)

    s.remove(x)
    

    i=i+1
a.remove('-')
print('-'.join(a))