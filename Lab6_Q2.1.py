N = int(input('enter the no. till you the sum: '))
s=0
for i in range(1,N+1):
    x = 1/i
    s = s+x
print(f'the sum of the series is {s:.9f}')

