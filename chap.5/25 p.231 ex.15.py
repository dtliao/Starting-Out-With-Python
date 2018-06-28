def calc_average():
    average=(firstScore + secondScore + thirdScore + fourthScore + fifthScore)/5
    return average
def determine_grade(x):
    if x>=90 and x<=100:
        return 'A'
    elif x>=80:
        return 'B'
    elif x>=70:
        return 'C'
    elif x>=60:
        return 'D'
    else:
        return 'F'

firstScore = int(input('Enter the first score:'))
secondScore = int(input('Enter the second score:'))
thirdScore = int(input('Enter the third score:'))
fourthScore = int(input('Enter the fourth score:'))
fifthScore = int(input('Enter the fifth score:'))

x=calc_average()
y=determine_grade(x)
print(y)

print('Score', '\t\t', 'Grade', '\t', 'Letter Grade')
print('----------------------------------------------------')

print('Score 1:\t', firstScore, '\t\t', determine_grade(firstScore))
print('Score 2:\t', secondScore, '\t\t', determine_grade(secondScore))
print('Score 3:\t', thirdScore, '\t\t', determine_grade(thirdScore))
print('Score 4:\t', fourthScore, '\t\t', determine_grade(fourthScore))
print('Score 5:\t', fifthScore, '\t\t', determine_grade(fifthScore))
print('----------------------------------------------------')
print ('Average:\t', x, '\t\t', y)