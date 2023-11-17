# function for finding sum of numbers.
def su(n):
    if n==0:
        return 0
    else:
        return n+su(n-1)

x= int(input('enter the no. you want the sum of: '))
print(f'The sum of {x} numbers is {su(x)}.')
