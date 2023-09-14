a = float(input('enter the cofficient of x^2: '))
b = float(input('enter the cofficient of X: '))
c = float(input('enter the cofficient of x^0: '))
d = ((b)**2 -(4*a*c))
if a==0:
    print('you have not entered a quadratic eq.')
elif d<0:
    print('the roots are not real.')
else:
    r1 = ((-b + (d)**0.5))/2*a
    r2 = ((-b - (d)**0.5))/2*a
    print(f'the roots are {r1:.2f}, {r2:.2f}')


