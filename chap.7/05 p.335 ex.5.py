infile = open('charge_accounts.txt', 'r')
content = []
for line in infile:
    content.append(line)

account= input('Enter a charge account number:')
if account.isdigit():
    if account in content:
        print('Account number', account, 'is valid')
    else:
        print('Account number', account, 'is invalid')
    infile.close()
else:
    print("Don\'t 讀 that")