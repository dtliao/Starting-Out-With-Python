def main():
    kilometers=0
    kilometers=float(input('Enter a distance in kilometers:'))
    convert_k(kilometers)
def convert_k(k):
    m=0
    m=k*0.6214
    print('The convertion of', format(k, ',.2f'), \
          'kilometers', 'to', format(m,',.2f'), 'miles')
main()