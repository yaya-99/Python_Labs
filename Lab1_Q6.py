a = int(input('enter the cofficient of x^2 :'))
b = int(input('enter the cofficient of x :'))
c = int(input('enter the constant :'))
d = b**2 - 4*a*c
if d < 0:
    print('The roots are not real.')
elif d >= 0:
    r1 = (-b + d**0.5)/(2*a)
    r2 = (-b - d**0.5)/(2*a)
    print('The roots are ',r1,' ',r2,)