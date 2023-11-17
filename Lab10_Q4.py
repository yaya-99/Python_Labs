# creating func for the menu.
def add(x,y):
    return(x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        print('invalid')
    else:
        return x/y
def mod(x,y):
    if y==0:
        print('invalid')
    else:
        return x%y
def exp(x,y):
    return x**y

# writing code for the menu operations.
while 1==1:
    q= input('Continue or Quit ? ')
    if q== 'Quit':
        break
    else:
        a= int(input('Enter the first operand: '))
        b= int(input('Enter the 2nd operand: '))
        print('The available choices are: ')
        print('1. Addition','2. Subtration','3. Multiplicaion','4. Division','5. Modulus','6. Exponentiation')
        z = input('Your Choice: ')
        if z== 'Addition':
            print('Sum is ', add(a,b))
        elif z=='Subtraction':
            print('Difference is ', sub(a,b))
        elif z=='Multiplication':
            print('Product is ', mul(a,b))
        elif z=='Division':
            print('Qoutient is ', div(a,b))
        elif z=='Modulus':
            print('Mod/Remainder is ', mod(a,b))
        elif z=='Exponentiation':
            print(f'Exponent of {a} to the power of {b} is {exp(a,b)}.')
        else:
            print('choose a valid option.')

