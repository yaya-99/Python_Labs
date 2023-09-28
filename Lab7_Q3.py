s = str(input('enter the sentence: '))
s = s.replace(' ','-')
print(s)



a= s.replace('-','_')
a= a.lower()
print(a)

c  = a.title()
c = c.replace('_','')
print(c)