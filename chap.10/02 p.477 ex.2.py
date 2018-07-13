from Car import Car

car1= Car('Totoya', 'Corolla', 5)

print('car is accelerating: ')
for i in range(5):
    car1.accelerate()
    print('Current speed: ', car1.get_speed())
print()


print('car is braking: ')
for i in range(5):
    car1.brake()
    print('Current speed: ', car1.get_speed())

