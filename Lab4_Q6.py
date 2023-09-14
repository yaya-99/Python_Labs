N = int(input('enter the no.: '))
s = str(N)
l = len(s)
i= 0
r= 0
while i<l:
    dig = N%10
    r = r*10 + dig

    N = N//10
    i= i+1
if int(s)==r:
    print(f'{int(s)} is a palindrome.')
else:
    print(f'{int(s)} is not a palindrome.')


