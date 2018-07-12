def sentenceCapitalizer(s):
    word_list = s.split()
    for i in range(0,len(word_list)):
        word_list[i] = word_list[i].capitalize()
    return ' '.join(word_list)

#s = input('Enter a string:')
print(sentenceCapitalizer("hello. my name is joe."))

