from coordinate import Coordinate
from parallelepiped import Parallelepiped

print('What do YOu want to do? ')
print('1. Sum of two points')
print('2. Magnitude of the point')
print('3. Direction of the point')
print('4. Volume of the parallelepiped')
print('5. Display the point')

a= int(input('Your Choice (1-5): '))

if a==1:
    l=[]
    for i in range(2):
        x,y,z = map(int, input('Enter the coordinates of the point: ').split())
        p = Coordinate(x,y,z)
        l.append(p)
    r=0
    for i in range(len(l)):
        r = l[0] + l[1]
    print('Sum of the coordinates :',r.dis())

elif a==2:
    x,y,z = map(int, input('Enter the coordinates of the point: ').split())
    p = Coordinate(x,y,z)
    print('Magintude of the point is: ', p.mag())

elif a==3:
    x,y,z = map(int, input('Enter the coordinates of the point: ').split())
    p = Coordinate(x,y,z)
    print('Direction of the point is: ', p.dir().dis())


elif a==4:
    l=[]
    for i in range(3):
        x,y,z = map(int, input('Enter the coordinates of the point: ').split())
        p = Coordinate(x,y,z)
        
        l.append(p)
    pp = Parallelepiped(l[0],l[1],l[2])
    print('Volume is :', pp.volume())

elif a==5:
    x,y,z = map(int, input('Enter the coordinates of the point: ').split())
    p = Coordinate(x,y,z)
    print(p.dis())
    
else:
    print('Invalid input !!!')
    print('Choose a valid input(1-5).')



    

    



