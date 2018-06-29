def is_prime(n):
    half=int(n/2)
    status=True

    for i in range(1, half+1):
        if n%i==0:
            status=False
    return status

n=int(input('Enter a number:'))
x=is_prime(n)

if is_prime(n):
    print('The number you entered is a prime number.')
else:
    print('The number you entered is not a prime number.')
