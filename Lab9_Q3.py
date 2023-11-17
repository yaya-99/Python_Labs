N = int(input('enter the size of square matrix: '))
M= []
print('enter matrix elements:')
for i in range(N):
    r= [int(x) for x in input().split()]
    M.append(r)
print(M)   

# sum of diagonals of matrix
d1 = sum(M[i][i] for i in range(len(M))) # principle diagonal
d2 = sum(M[i][len(M)-1-i] for i in range(len(M))) # non-principle diagonal
print('sum of principle diagonal: ',d1)
print('sum o non-principle diagonal: ',d2)

# transpose
def t(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

MT= t(M)
print('transpose is: ',MT)

# check for symmetric
if M==MT:
    print('Matrix is symmetric.')
else:
    print('Not symmetric.')

# check for upper and lower triangular
def up_tr(matrix):
    return all(matrix[i][j] == 0 for i in range(1,len(matrix)) for j in range(i))

def lo_tr(matrix):
    return all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(i+1, len(matrix[0])))

print('is this matrix upper triangular? :', up_tr(M))
print('is this matrix lower triangular? :', lo_tr(M))


