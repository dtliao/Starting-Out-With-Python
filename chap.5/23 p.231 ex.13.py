def falling_distance():
    g = 9.8
    d=(1/2)*g*t**2
    return d


print('Time', '\t', 'Distance')
print('--------------------')
for t in range(1,11):
    d=falling_distance()
    print(t, '\t\t', format(d, ',.2f'))

