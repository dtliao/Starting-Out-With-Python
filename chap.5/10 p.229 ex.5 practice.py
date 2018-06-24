def display(actual,assessment,property):
    print('Assessment Value is $', format(assessment, ',.2f'))
    print('Property Tax is $', format(property, ',.2f'))

actual=float(input('Enter the actual value: '))
assessment=actual*0.6
pRate=0.72/100
property=pRate*assessment
display(actual,assessment,property)