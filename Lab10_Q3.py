Odd = {}
Even = {}
while 1==1:
    x= str(input('over or not? '))
    if x=='over':
        break
    else:
        n= int(input())
        s= n*n
        c=n*n*n

    if n%2==0:
        Even[n]=[s,c]
    else:
        Odd[n]=[s,c] 
print(Even)
print(Odd)
