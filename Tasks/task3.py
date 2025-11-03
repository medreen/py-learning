phone_number = input('Enter phone number: ')
num1 = phone_number[0]
print(type(num1))

if phone_number.startswith('+254'):
    print('Valid phone number.')
else:
    if len(phone_number) == 10:
        phone_number = phone_number.replace(num1, '+254')
        print(phone_number)
    else:
        phone_number = '+254' + phone_number
        print(phone_number)





