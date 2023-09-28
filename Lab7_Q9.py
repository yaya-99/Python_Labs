s = str(input('enter a sentence: '))
s =s.lower()
s= s.replace(' ','')
p =''
for i in s:
    if i not in p:
        p= p+i
p = p.replace('',' ')
p = p.split()
p.sort()
print(p)

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
if p==l:
    print('pangram')
else:
    print('not a pangram')
    
