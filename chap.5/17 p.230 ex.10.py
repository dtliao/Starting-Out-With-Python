def main():
    feet=float(input('Enter a number of feet:'))
    inches=feet_to_inches(feet)
    print(feet, 'feet=', inches, 'inches')
def feet_to_inches(feet):
    return feet*12
main()
    