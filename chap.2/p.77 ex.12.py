Joe_Paid_Stock= 2000* 40
Joe_Commission= 0.03* Joe_Paid_Stock
Joe_Sold_Stock= 2000* 42.75
Joe_Second_Commission= 0.03* Joe_Sold_Stock
Profit= Joe_Sold_Stock-Joe_Paid_Stock-(Joe_Commission+ Joe_Second_Commission)

#Version1
x = 'Amount Joe paid for the stock $' + format(Joe_Paid_Stock, ',.2f')
x = x + 'Commission for buying $' + format(Joe_Commission, ',.2f')
x = x + 'Amount Joe sold for the stock $' + format(Joe_Sold_Stock, ',.2f')
x = x + 'Commission for selling $' + format(Joe_Second_Commission, ',.2f')
x = x + 'Profit or Loss is $' + format(Profit, ',.2f')
print(x)

#Version2
print('Amount Joe paid for the stock $' + format(Joe_Paid_Stock, ',.2f'), \
'Commission for buying $' + format(Joe_Commission, ',.2f'), \
    'Amount Joe sold for the stock $' + format(Joe_Sold_Stock, ',.2f'), \
    'Commission for selling $' + format(Joe_Second_Commission, ',.2f'), \
    'Profit or Loss is $' + format(Profit, ',.2f'))
