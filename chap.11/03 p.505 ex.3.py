from Person import *
name = input('Enter the name: ')
address = input('Enter the address: ')
phone_number = input('Enter the phone_number: ')
c_number = input('Enter the customer number: ')
on_list = input('Does the customer wish to be ' \
                    'on the mailing list?(Yes/No): ')
on_list_flag = False
if on_list == 'Yes':
    on_list_flag = True

#while on_list != 'Yes' and on_list != 'No':
    #print('Please type Yes or NO')
    #on_list = input('Does the customer wish to be ' \
                    #'on the mailing list?(Yes/No): ')
#if on_list == 'Yes':
    #print('Yes')
#else:
    #print('No')



customer1 = Customer(name, address, phone_number, \
                           c_number, on_list_flag)
print ('Customer information: ')
print ('Name:', customer1.get_p_name())
print ('Address:', customer1.get_p_address())
print ('Phone number:', customer1.get_p_telephone())
print ('Customer Number:', customer1.get_c_number())
print ('On Mailing List:', customer1.get_m_list())