x = int(input('enter the 1st integer: '))
y = int(input('enter the 2nd integer: '))
if x<0 or y<0:
    print('invalid input')
elif (y%x)==0:
    print('y =',y,'is divisible by x =',x,'.')
elif (y%x)!=0:
    print('y =',y,'is not divisible by x =',x,".")




