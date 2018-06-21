mass=float(input("Enter an object's mass in kilograms:"))
weight=mass* 9.8
if weight>500:
    print('It is too heavy')
elif weight<100:
    print('It is too light')
print('Weight is', format(weight, '.2f'), 'newtons')