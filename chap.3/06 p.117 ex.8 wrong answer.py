Attending=int(input('Enter the number of people:'))
Given=int(input('Enter the number of hot dogs each person wil be given:'))
hot_dogs_p=Attending *Given//10
buns_p= Attending *Given//8
hot_dogs_l= Attending *Given%10
buns_l= Attending *Given%10
print(hot_dogs_p)
print(buns_p)
print(hot_dogs_l)
print(buns_l)
