x = 6
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for j in range(x-i):
        print('* ', end='')
    print()