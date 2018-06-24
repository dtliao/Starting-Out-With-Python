def calories(fatGram, carbsGram):
    print('Calories from fat = ', format(cFat, ',.2f'))
    print('Calories from fat = ', format(cCarbs, ',.2f'))

fatGram=float(input('Enter the number of fat grams:'))
carbsGram=float(input('Enter the number of carbs grams:'))
cFat=fatGram* 9
cCarbs=carbsGram*4
calories(fatGram, carbsGram)