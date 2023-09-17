N= int(input('enter a no.: '))
c=0
d = 0
while 1==1:
    n = int(input('enter the no.: '))
    if n == -999:
        break
    else:
        if n%N ==0:
            c =c+1
        else:
            d= d+1

print(f'No. of numbers divisible by {N} are {c}.')
print(f'No. of numbers not divisible by {N} are {d}.')