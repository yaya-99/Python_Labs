r = 7.1 # bank calculates interest on RD accounts at 7.1% p.a.
p = float(input('enter the principle amount in rupees: '))
t = float(input('enter the duration of RD in years: '))
n= t*12
if p<500 or t<0.5:
    print('invalid input.')
else:
    a = p*(1+r/100)*n*t
print('amount is Rs ',a)
print('monthly return is ',a/12)


