s = str(input('enter a sentence: '))
p =''
for i in s:
    if i not in p:
        p= p+i
print(p)
