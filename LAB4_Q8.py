n  = int(input('enter the number: '))
i =2
c = 1
if n<2:
    print('not a prime no.')
elif n==2:
    print('prime no.')
else:
    while i<((n/2)+1):
        if n%i==0:
            c = 0
            break
        else:
            i = i+1
    

if c == 0:
    print('not a prime no')

else:
    print('prime no.')

    

    

        