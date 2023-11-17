p = str(input('Enter your paragraph: '))
p =p.lower()
p=p.replace('',' ')
s=p.split()
print(s)
d={'a':0,'e':0,'i':0,'o':0,'u':0} # creating a dictionary of vowels.
for i in s:
    if i=='a':
        d['a']+= 1
    elif i=='e':
        d['e'] +=1
    elif i=='i':
        d['i']+= 1
    elif i=='o':
        d['o']+= 1
    elif i=='u':
        d['u']+= 1

print(d)
print(max(d.values()))

sd = dict(sorted(d.items(), key=lambda item: item[1])) # sorting the dictionary according to the values.

# displaying the result.
for key, value in sd.items():
    print(key, value)