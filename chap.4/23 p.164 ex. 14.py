for i in range(0,6):
    print('#', end='')

    for r in range(0,7):
        if i==r:
            print("#",end='')
        else:
            print(' ',end='')
    print()