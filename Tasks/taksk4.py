email = input('Enter your email: ')

if '@' in email:
    if '.' in email[-5:-1]:
        print('Email is valid.')
    else:
        print('Email is lacking a period')
else:
    print('Check email')