N = int(input('enter the no. to find the factorial: '))
i = 1
F= 1
if N==0:
    print(f'the factorial of {N} is 1.')
elif N<0:
    print(f'{N} is a negative integer.')
else:
    while i <= N:
        F = i*F
        i=i+1

print(f'the factorial of {N} is {F}.')




