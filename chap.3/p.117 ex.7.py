primary_color=input('Enter the name of a primary color in uppercase:')
primary_color_two=input('Enter the name of another primary color in Uppercase:')
red='Red'
blue='Blue'
yellow='Yellow'
if primary_color != red and primary_color != blue and primary_color != yellow:
    print('Error: not primary color')
elif primary_color_two != red and primary_color_two != blue and primary_color_two != yellow:
    print('Error: not primary color')
elif primary_color == primary_color_two:
    print('Error: the same color')
else:
    if primary_color==red:
        if primary_color_two==blue:
            print('purple')
        else:
            print('orange')
    elif primary_color==blue:
        if primary_color_two==red:
            print('purple')
        else:
            print('green')
    else:
        if primary_color_two==blue:
            print('green')
        else:
            print('orange')
