for i in range(6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(1,i*2,1):
        print('*', end='')
    print()