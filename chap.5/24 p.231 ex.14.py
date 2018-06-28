def kinetic_energy(m,v):
    KE=(1/2)*m*v**2
    return KE

m=float(input('Enter the mass(in kilograms):'))
v=float(input('Enter the velocity(in meters per second):'))
x=kinetic_energy(m,v)
print('The kinetic energy is', format(x, ',.0f'), 'joules')