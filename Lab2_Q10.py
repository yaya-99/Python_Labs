x = int(input('enter the no. of sec :'))
if x in range(1,86400):
    h= x//3600
    m = x//60 - h*60


    s = x- h*3600- m*60
    print(x,'sec =',h,'hours',m,'min','and',s,'sec.')
else:
    print('enter sec in between 1 and 86400.')
