#s = input('Enter a sentence:')
s = 'I SLEPT MOST OF THE NIGHT'
#word_list = s.split()
#sentence = ""
#for word in word_list:
    #w = list(word)
    #w.append(w[0])
    #del(w[0])
    #w.append("AY")
    #sentence += ' ' + ''.join(w)
#sentence = sentence[1:len(sentence)]
#print(sentence)

s = 'I SLEPT MOST OF THE NIGHT'
word_list = s.split()
sentence = ""

for i in range(0, len(word_list)):
    w = word_list[i]
    w = w[1:len(w)] + w[0] + "AY"
    sentence += ' ' + ''.join(w)
sentence = sentence[1:len(sentence)]
print(sentence)

