def main():
    replacement=0
    replacement=float(input('Enter the replacement cost: '))
    minimum(replacement)
def minimum(replacement):
    minimum_insurance=0
    minimum_insurance=0.8*replacement
    print('Minimum of insurance you should buy $ ', format(minimum_insurance, ',.2f'))
main()
