s = str(input('enter a paragragh: '))
print(ord('0'))
print(ord('9'))

uc= 0
lc = 0
d = 0
sp = 0
l=len(s)
i=0
for i in s:
    if ord(i) in range(65,91):
        uc= uc+1
    elif ord(i) in range(97,123):
        lc=lc+1
    elif ord(i) in range(48,57):
        d = d+1
    else:
        sp = sp+1

print(f'upper case are {uc}, lowercase are {lc}, digits are {d} and special chracters are {sp}.')