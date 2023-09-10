n = int(input('enter a 3 digit no.: '))
h= n//100
p = n%100
t = p//10
o = p%10
x = h**3 + t**3 + o**3
if n==x:
    print(n,'is a Armstrong no.')
else:
    print(n,'is not a Armstong no.')
