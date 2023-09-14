n = int(input('enter the no.: '))
s = str(n)
l = len(s)
i= 0
r= 0
sum = 0
while i<l:
    dig = n%10
    r = r*10 + dig
    s = s+dig

    n = n//10
    i= i+1
print(r)
print(sum)

