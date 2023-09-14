N = int(input('enter a no.: '))
i = 1
if N >0:
    while i < 21:
        print(N,'*',i,'=', N*i)
        i = i+1
else:
    print('invalid input')    