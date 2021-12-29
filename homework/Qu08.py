x=5
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for j in range(1, (x*2-i*2), 1):
        print('*', end='')
    print()