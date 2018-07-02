def file():
    infile = open('numbers.txt', 'r')
    contents = infile.read()
    infile.close()
    print(contents)
file()