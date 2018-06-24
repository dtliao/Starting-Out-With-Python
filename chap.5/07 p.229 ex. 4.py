def main():
    loan_payment=0
    insurance=0
    gas=0
    oil=0
    tires=0
    maintenance=0

    loan_payment=float(input('Enter the loan payment cost: $'))
    insurance=float(input('Enter the insurance cost: $'))
    gas=float(input('Enter the gas cost: $'))
    oil=float(input('Enter the oil cost: $'))
    tires=float(input('Enter the tires cost: $'))
    maintenance=float(input('Enter the maintenance cost: $'))
    total_cost(loan_payment, insurance, gas, oil, tires, maintenance)

def total_cost(loan_payment, insurance, gas, oil, tires, maintenance):
    total_monthly_cost=0
    total_monthly_cost=loan_payment+insurance+gas+oil+tires+maintenance
    total_annual_cost=0
    total_annual_cost=12*total_monthly_cost
    print('Total Monthly Cost $', format(total_monthly_cost, ',.2f'))
    print('Total Annual Cost $', format(total_annual_cost,',.2f'))
main()