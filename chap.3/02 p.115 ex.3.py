Age=int(input('Please enter your age:' ))
if Age<=1:
    print('You are an infant')
elif Age>1 and Age<13:
    print('You are a child')
elif Age>13 and Age<20:
    print('You are an teenager')
else:
    print('You are an adult')