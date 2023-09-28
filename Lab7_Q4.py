s = str(input('enter the sentence: '))
s = s.lower()
s= s.replace('',' ')
p= s.split()
l = len(p)

p1 = []
for i in range(-1,-l-1,-1):
    p1.append(p[i])
    

if p==p1:
    print('palindrome')
else:
    print('not a palindrome')
    

