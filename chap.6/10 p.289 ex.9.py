total = 0
average=0

try:
    infile=open('numbers.txt', 'r')
    
    for content in infile:
        number = int(content)
        total+=number
        print(number)

    infile.close()
    average = format((total/number), '.2f')
    print('The average is:',average)


except IOError:
    print('An error occurred while trying to read the file.')
except ValueError:
    print('Non-numeric data found in the file')
except:
    print('An error occurred')