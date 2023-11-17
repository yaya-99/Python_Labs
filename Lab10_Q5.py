def shift(lst,k):
    if not lst:
        return lst
    else:
        n= len(lst)
        if k>n or k<0:
            print('invalid')
        else:
            return lst[k:] + lst[:k]
    
l= [0,1,2,3,4,5,6,7,8,9]
k=4
r = shift(l,k)
print(r)


def shift_d(lst,k,direction='left'):
    if not lst:
        return lst
    else:
        n= len(lst)
        if k>n or k<0:
            print('invalid')
        if direction == 'left':
            return lst[k:] + lst[:k]
        elif direction == 'right':
            return lst[-k:] + lst[:-k]
        else:
            print("Use 'left' or 'right'.")

l=[0,1,2,3,4,5,6,7,8,9]
k=4
r1= shift_d(l,k,'left')
r2= shift_d(l,k,'right')
print(r1)
print(r2)