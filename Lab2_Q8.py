x = int(input('enter the year you wish to check: '))
l = x % 400
if l==0:
    print(x,'is a leap year.')
else:
    print(x,'is not a leap year.')
