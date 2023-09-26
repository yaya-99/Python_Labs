N =int(input('enter the no: '))
x = int(input('enter the value of x: '))
s = 1
for i in range(1,N+1):
    b= (x**i)/i
    s = s+b
print(f'the sum is {s:.9f}')
