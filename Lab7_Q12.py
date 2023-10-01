N = int(input('enter the input: '))
for i in range(1, N + 1):
   if i == 1 or i == N:
    print('+' + '/\\/\\/\\/\\' + '+')
   else:
     print('|' + ' ' * (N * 2 - 2) + '|')
     