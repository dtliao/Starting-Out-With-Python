import random
def count():
    number = list()
    parity = list()
    oddCount = 0
    evenCount = 0

    for i in range(0,100):
        number.append(random.randint(1, 1000))
        if number[i] % 2 == 1:
            parity.append('Odd')
            oddCount += 1
        else:
            parity.append('Even')
            evenCount += 1
    print(number)
    print(parity)
    print(oddCount, 'numbers is odd', evenCount, 'numbers is even')

count()
