N = int(input('enetr a no.: ')) # N is the count of +ve numbers.
hcf = 1
i = 0
l=[]

while i<N:
    n  = int(input("enter the +ve integer : "))
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

lcm = 1
j=0
while j<len(l):
    lcm = lcm*l[j]
    j=j+1

LCM = lcm/g
print(f'the LCM of {N} +ve no. is {LCM}.')

