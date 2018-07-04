total = 0
daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for i in range(7):
    daily_sales[i] = float(input('Enter the sales for ' + week[i] + ':' ))

for r in daily_sales:
    total += r
print('Total sales for the week is:', format(total, ',.2f'), sep='')
