infile = open('text.txt', 'r')

uppercase = 0
lowercase = 0
digits =0
whitespace = 0

for line in infile:
    character = list(line)
    for i in range(0,len(character)):
        if character[i].isupper():
            uppercase += 1
        elif character[i].islower():
            lowercase += 1
        elif character[i].isdigit():
            digits += 1
        elif character[i].isspace():
            whitespace += 1

infile.close()

print('The number of uppercase letters:', uppercase)
print('The number of lowercase letters:', lowercase)
print('The number of digits:', digits)
print('The number of whitespace characters:', whitespace)

