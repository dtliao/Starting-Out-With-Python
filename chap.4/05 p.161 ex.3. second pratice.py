budgeted=0
Over_budgeted=0
Under_budgeted=0
expenses=2
budgeted=float(input('Enter your budgeted for a month:'))
total=0
while expenses!=0:
    expenses=float(input('Enter your expenses for the month(0 to quit):'))
    total+=expenses

print('Budget:', format(budgeted, ',.2f'))
print('Expense:', format(total, ',.2f'))

if budgeted>total:
    Under_budgeted=budgeted-total
    print('You are under budget $',format(Under_budgeted, ',.2f'))
elif total>budgeted:
    Over_budgeted=total-budgeted
    print('You are over budget $', format(Over_budgeted, ',.2f'))
else:
    print('Nice Saving!')
