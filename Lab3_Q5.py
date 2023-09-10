n = int(input('enter a 5 digit no.: '))
a = n//10000
b = n%10000
c = b//1000
d = b%1000
e = d//100
f = d%100
g = f//10
h = f%10
i = h*10000+g*1000+e*100+c*10+a
if n<10000:
    print('not a 5 digit no.')
else:
    print(i)
    if n==i:
        print('the no.',n,' is a palindrome.')
    else:
        print('the no.',n,' is not a palindrome.')