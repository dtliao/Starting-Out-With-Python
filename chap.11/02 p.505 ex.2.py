from Employee1 import *

s_name = input('Enter the employee name: ')
s_number = input('Enter the employee number: ')
s_salary = float(input('Enter the annual salary: '))
s_bonus = float(input('Enter the bonus: '))

sup1 = ShiftSupervisor(s_name, s_number, \
                                     s_salary, s_bonus)

print('Shift supervisor worker information: ')
print('Name:', sup1.get_name())
print('ID number:', sup1.get_number())
print('Annual Salary: $', \
      format(sup1.get_salary(), ',.2f'), \
      sep='')
print('Annual Production Bonus: $', \
      format(sup1.get_bonus(), ',.2f'), \
      sep='')