def minimum():
    print('The minimum amount of insurance you should buy is $', format(m_i, ',.2f'))

r=float(input('Enter the replacement cost of the building:'))
m_i=r*0.8
minimum()