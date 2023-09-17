N = int(input('enetr a no.: ')) # N is the count of +ve numbers.
hcf = 1
i = 0
l=[]

while i<N:
    n  = int(input("enter the next +ve integer : "))
    if N<2:
        print('invaild input.')
    else:
        l.append(n)
    i=i+1
print(l)
g=l[0]
c=1
while c<len(l):
    x=l[c]
    while g!=x:
        if g>x:
            g = g-x
        else:
            x=x-g
    c=c+1

    

print(f'the GCD of {N} positive numbers is {g}.')
