budget=0
expenses=1
total=0
differences=0

budget=float(input('Enter your budgeted for a month:'))
while expenses !=0:
    expenses=float(input('Enter your expenses(quit for 0):'))
    total+=expenses
if total>budget:
    differences=total-budget
    print('Over budget $', differences)
elif total<budget:
    differences=budget-total
    print('Under budget $', differences)
else:
    print('Nice planning!')