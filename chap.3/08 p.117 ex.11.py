number_books=int(input('Enter the number of books purchased this month:'))
if number_books==2:
    print('award 5 points')
elif number_books==4:
    print('award 15 points')
elif number_books==6:
    print('award 30 points')
elif number_books>=8:
    print('award 60 points')
else:
    print('award 0 points')