def line():
    print('='*100)

firstName = input('First Name: ')
midName = input('Middle Name: ')
lastName = input('Last Name: ')

print(f'Your full name is {firstName} {midName} {lastName}')
print(f'Your Initials are {firstName[0]} {midName[0]} {lastName[0]}')

line()

lotNumber = '037-00901-00027'
print(f'Country Code {lotNumber[0:3]}')
print(f'Product Code {lotNumber[4:9]}')
print(f'Batch Code {lotNumber[10:16]}')