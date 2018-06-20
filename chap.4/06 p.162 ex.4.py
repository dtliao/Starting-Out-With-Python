speed=0
time=0
distance=0
speed=float(input('What is the speed of the vehicle in mph?'))
time = int(float(input('How many hours has it traveled?')))
print('Hour' '\t' 'Distance Traveled')
print('_________________________________')

for i in range(1, time+1):
    distance=speed* i
    print(i, '\t\t', distance)
