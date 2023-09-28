s= str(input('enter a sentence: '))
w = str(input('enter a word: '))
s =s.split()
l = len(s)
c=0
for i in range(0,l):
    if w == s[i]:
        c+=1
print(f'{w} comes {c} times in the sentence ')