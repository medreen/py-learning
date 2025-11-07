#A function that can create an account
#user name and 
import datetime
accounts = []


user_id = int(input('Enter user id: '))
user_name = input('Enter username: ')

#checking password input is valid
while True:
    password = input('Enter password: ')

    if len(password) < 10:
        print('Password is too short!')
    elif len(password) >= 10:
        break

#checking is amount valid
while True:
    amount = float(input('Enter amount: '))
    
    if amount < 500:
        print('Amount should be above 500')
    elif amount >= 500:
        break
    else:
        print("Invalid amount.")    

age = int(input('Enter age: '))

#checks phone validity
while True:
    phone_number = input('Enter phone_number: ')
    if len(phone_number) < 10:
        print("Phone number is too short")
    elif len(phone_number) == 10 and phone_number.startswith('0'): 
        print('Phone number is valid!')
        break
    else:
        print('Phone number is not valid.')


#checking email validity
while True:
    email = input('Enter email: ')
    if "@" in email and email.count("@") == 1 and len(email) >= 8:
        print('Email is valid.')
        break
    else:
        print('Enter a valid email.')

#account creation
def create_account(user_id, username, password, amount, age, phone_number, email):

    if age < 18:
        status = 'Piggy-Bank'
    else:
        status = 'Saving'
    
    user = {
        "userid" : user_id,
        "username" : username,
        "password" : password,
        "age" : age,
        "phone" : phone_number,
        "email" : email,
        "date-of-registration" : datetime.datetime.now(),
        "status" : status,
    }

    return user

user = create_account(user_id, user_name, password, amount, age, phone_number, email)
print(user)

#update account
accounts.append(user)
print(accounts)

    




