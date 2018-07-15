from Employee1 import *

worker_name = input('Enter the employee name:')
worker_number = input('Enter the employee number:')
shift_number = int(input('Enter the shift number(1, 2, 3):'))
hourly_pay_rate = float(input('Enter the hourly pay rate:'))

emp1 = ProductionWorker(worker_name, worker_number, shift_number, hourly_pay_rate)

print('Production worker information:')
print('Name:', emp1.get_name())
print('ID number:', emp1.get_number())
print('Shift:', emp1.get_shift_number())
print('Hourly Pay Rate: $', format(emp1.get_hourly_rate(), ',.2f'), sep='')
