s = str(input('enter a sentence: '))
a = s.split()
l = len(a)
print(s)
for i in range(-1,-l-1,-1):
    print(a[i],end=' ')