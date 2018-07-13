from Pet import Pet

pName = input('Enter the pet\'s name:')
pType = input('Enter the pet\'s type:')
pAge = int(input('Enter the pet\'s age:'))

pet1=Pet(pName, pType, pAge)
print(pet1.result())