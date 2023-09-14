x= int(input('enter number:'))
y= int(input('enter number:'))
N = int(input('enter number of which you want to check divisibility'))
i=x+1
if x>y:
    print('invalid input')
else:
    while i<=y:
        if N%i==0:
            print(i)
        else:
            print('invalid intput')
        i=i+1







            
    


