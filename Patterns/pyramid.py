n = int(input('Enter the number of rows: '))
for i in range(0,n):
    for j in range(i, n-1):
        print(' ', end='')
    for k in range(0, i+1):
        print('*', end='')
    print()

