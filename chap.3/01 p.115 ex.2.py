areaA= lengthA* widthB
areaB= lengthB* widthB

lengthA= float(input('Enter length A:'))
widthA= float(input('Enter width A:'))
lengthB= float(input('Enter length B:'))
widthB= float(input('Enter width B:'))

If areaA>areaB:
    print('Area A is larger than Area B')
elif areaB>areaA:
    print('Area B is larger than Area A')
else:
    print('Area A is euqal to Area B')

