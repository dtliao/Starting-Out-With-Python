def is_prime(i):
        half = int(i/2)
        status = True

        for r in range(2, half + 1):
            if i % r == 0:
                status = False

        return status


print('Number', '\t', 'Prime/Not Prime')
print('--------------------------')
for i in range(2, 101):
    x=is_prime(i)
    if x:
        print(i, '\t', 'Prime')

    else:
        print(i, '\t\t', 'Not Prime')


