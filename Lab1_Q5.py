reply = str(input('Do you know the base and height of the Triangle ? yes or no? '))
if reply == 'yes':
    b = float(input('Enter the base of the triangle in metre: '))
    h = float(input('Enter the height of the triangle in metre: '))
    a = 0.5*b*h
    print('Area of the triangle is ',a,'sq m.')
elif reply == 'no':
    x = float(input('Enter 1st side of triangle in m: '))
    y = float(input('enter 2nd side in m: '))
    z = float(input('enter 3rd side in m: '))
    s = (x+y+z)/2
    A = (s*(s-x)*(s-y)*(s-z))**0.5
    print('Area of the triangle is ',A,'sq m.')
else:
    print('please reply yes or no')
    