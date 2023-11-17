# function for factorial.
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
x = int(input('enter the no. :'))
print(f'The factorial of {x} is {fact(x)}.')