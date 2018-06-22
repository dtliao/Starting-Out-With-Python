n=0
total=1
while n<=0:
    n=int(input('Enter a nonegative integer:'))

for i in range(1,n+1):
    total*=i
print('The factorial is', total)