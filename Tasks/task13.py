access_email = 'admin@mail.com'
access_password = 'Admin@123'

email = input('Enter the email: ')
password = input('Enter the password: ')

for i in range(3):
    email = input('Enter the email: ')
    password = input('Enter the password: ')
    
    if email == access_email and password == access_password:
        print('Login is Successful.')
    else:
        print('Invalid username or password.')
    break
print('You have been blocked')