def main():
    a=20
    b=15
    c=10
    a_sold=0
    b_sold=0
    c_sold=0
    a_sold=int(input('How many tickets for class A seats were sold?'))
    b_sold = int(input('How many tickets for class B seats were sold?'))
    c_sold = int(input('How many tickets for class C seats were sold?'))

    a_income=0
    b_income=0
    c_income=0
    a_income=a_sold*a
    b_income=b_sold*b
    c_income=c_sold*c

    total(a_income, b_income, c_income)
def total(a_income, b_income, c_income):
    total_income=0
    total_income=a_income+b_income+c_income

    
    print('Income for A Class Seats $', format(a_income, ',.2f'), sep='')
    print('Income for B Class Seats $', format(b_income, ',.2f'), sep='')
    print('Income for C Class Seats $', format(c_income, ',.2f'), sep='')
    print('Income for Total Class Seats $', format(total_income, ',.2f'), sep='')
main()