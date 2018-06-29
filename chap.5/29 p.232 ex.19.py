
def formula():
    I=i/100
    f=p*(1+I)**t
    return f



p=float(input('Enter the acount\'s present value:'))
i=float(input('Enter the monthly interest rate:'))
t=int(input('Enter the number of months:'))
x=formula()
print('The future value of the account', \
      'after the specified time period is $:', format(x, ',.2f'))
