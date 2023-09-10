n = int(input('enter a 3 digit no.: '))
h= n//100
p = n%100
t = p//10
o = p%10

s = h+t+o
print('The sum of digits is ',s,'.')
if s%3==0:
    print('The sum of digits is divisible by 3.')
else:
    print('The sum is not divisible by 3.')


