n1 = int(input('enter the length of 1st list: '))
n2 = int(input('enter the length of 2nd list: '))
l1=[]
l2=[]
s1=set(l1)
s2=set(l2)
for i in range (0,n1):
    x= int(input('enter a integer for 1st list: '))
    if x<0:
        print('invalid input')
    else:
        l1.append(x)
for i in range(0,n2):
    y=int(input('enter elements of 2nd list: '))
    if y<0:
        print('invalid')
    else:
        l2.append(y)

for i in l1:
    if i not in s1:
        s1.add(i)
for i in l2:
    if i not in s2:
        s2.add(i)

su= s1.union(s2)
print(su)
si = s1.intersection(s2)
print(si)
sd= s1-s2
print(sd)
sd1= s1-s2
sd2= s2-s1
sdu = sd1.union(sd2)
print(sdu)




