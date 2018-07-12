s = input('Enter a string:')
s = list(s)
for i in range(1,len(s)):
    if s[i].isupper():
        s[i] = s[i].lower()
        s.insert(i,' ')

s = ''.join(s)
print(s)