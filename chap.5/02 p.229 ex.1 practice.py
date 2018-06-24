def convert_k(k):
    miles=k*0.6214
    print('Convert', format(k, ',.2f'), \
        'Kilometers', 'to', format(miles, ',.2f'), 'Miles')
k = float(input('Enter a distance in kilometers:'))
convert_k(k)

