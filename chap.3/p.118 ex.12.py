Packages_Purchased=int(input(('Enter the number of packages purchased:'))
Retail_Price=99
Discount=0
Total_Price= 99* Packages_Purchased
If Packages_Purchased>=100:
    Discount=0.4                                                                                                                                          / print()* 0.4
elif Packages_Purchased>=50:
    Discount=0.3
elif Packages_Purchased>=20:
    Discount=0.2
elif Packages_Purchased>=10:
    Discount=0.1
else:
    Discount=0
Discount_amount= Total_Price* Discount
print('The amount of the discount is $' format(Discount_amount, '.2f'))
print('Total amount after the discount is $' format(Total_Price-Discount_amount, '.2f'))



