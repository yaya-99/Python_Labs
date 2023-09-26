N = int(input('enter the value of N: '))
s =0
i = 1
F= 1
if N==0:
    print(f'the factorial of {N} is 1.')
elif N<0:
    print(f'{N} is a negative integer.')
else:
    while i <= N:
        F = i*F
        x = 1/F
        s = s+x
        i=i+1

print(f'the sum is {s:.9f}')
