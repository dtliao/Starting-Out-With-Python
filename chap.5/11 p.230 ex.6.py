def main():
    fat_consumed=0
    carbs_consumed=0
    fat_consumed=float(input('Enter the fat grams you consumed in a day:'))
    carbs_consumed=float(input('Enter the carbohydrate grams you consumed in a day:'))
    calories_fat=0
    calories_carbs=0
    calories_fat=fat_consumed*9
    calories_carbs=carbs_consumed*4
    calories(calories_fat, calories_carbs)

def calories(calories_fat, calories_carbs):
    print('Calories from fat', format(calories_fat, ',.2f'))
    print('Calories from carbs', format(calories_carbs, ',.2f'))
main()
