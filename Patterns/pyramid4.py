n =int(input('Enter the number of rows: '))
for i in range(n, 0, -1):
    for j in range(i ,n):
        print(' ', end='')
    for k in range(0, i*2-1):
        print('*', end='')
    print()

