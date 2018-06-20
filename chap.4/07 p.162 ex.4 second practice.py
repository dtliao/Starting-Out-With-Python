distance=0
speed=0
time=0

speed=float(input('What is the speed of the vehicle in mph?'))
hour=(int(input('How many hours has it traveled?')))

print('Hours', '\t', 'Distance Traveled')
print('----------------------------')


for i in range(1,hour+1):
    distance=speed* i
    print(i, '\t\t', format(distance, '.1f'))

