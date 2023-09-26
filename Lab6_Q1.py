s = str(input('enter the sentence: '))
l= len(s)
word =1
i=0
v=0
c=0
V = ['A','E','I','O','U','a','e','i','o','u']
S = [' ']
C = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in range (0,l):
    if s[i] in V:
        v=v+1
    elif s[i] in C:
        c=c+1
    elif s[i] in S:
        word = word+1
        
    else:
        print('there is a invalid input.')
print(f'number of vowels is {v}')
print(f'no. of consonants is {c}')
print(f'no. of words is {word}')


 
