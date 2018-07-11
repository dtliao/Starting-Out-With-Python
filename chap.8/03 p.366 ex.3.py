date = input('Enter a date in the format mm/dd/yyyy:')
date_form = date.split('/')             #01/17/1987

month_list = ['January', 'February','March',
                  'April', 'May','June', 'July',
                  'August', 'September', 'October',
                  'November', 'December']

print(month_list[int(date_form[0])-1], date_form[1] +',' + date_form[2])



