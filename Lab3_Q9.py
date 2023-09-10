bs = int(input('enter the basic salary in Rs: '))
hra = 0.2*bs
ta = 0.05*bs
da = 0.1*bs
gs = bs+hra+ta+da

if gs< 300000:
    print('The income tax slab for gross salary ',gs,'is 0%.')
elif 300000<gs<1000000:
    print('The income tax slab for gross salart ',gs,'is',gs*0.1,'.')
elif 1000000<gs<2500000:
    print('The income tax slab for gross salary ',gs,'is',gs*0.2,'.')
elif gs>2500000:
    print('The income tax slab for gross salary ',gs,'is',gs*0.3,'.')