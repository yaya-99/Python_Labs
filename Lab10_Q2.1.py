import random

# First function for the list of outcomes.
def roll(n):
    l = []
    for i in range(n):
        x = random.randint(1, 6)
        l.append(x)
    return l

# Second function for finding the frequency count of the outcomes.
def fco(lst):
    fc = {}
    for i in lst:
        if i in fc:
            fc[i] += 1
        else:
            fc[i] = 1
    return fc

# Third function for displaying the frequency count.
def d_fc(fc):
    for i, j in fc.items():
        print(f'{i}: {j}')

# Last bit of code for calling the functions
N = int(input('Enter a number greater than 10000: '))
if N < 10000:
    print('Enter a number > 10000.')
else:
    r = roll(N)
    f = fco(r)
    print('Frequency Count: ')
    d_fc(f)
