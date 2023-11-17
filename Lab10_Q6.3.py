# function for fibonacci series
def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)

x= int(input('Enter the no. of terms in the series: '))
print('Fibonacci series: ')
for i in range(x):
    print(fib(i), end=',')

