def main():
    actual=0
    actual=float(input('Enter the actual value of the property:'))
    assessment=0
    assessment=actual*0.6

    property_tax = 0
    property_rate = 0.72 / 100
    property_tax = assessment * property_rate

    value(assessment, property_tax)

def value(assessment, property_tax):
    print('Assessment Value: $', format(assessment, ',.2f'), sep='')
    print('Property Tax: $', format(property_tax, ',.2f'), sep='')
main()