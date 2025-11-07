#bank
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
    if "@" in email and ".com" in email and email.count("@") == 1 and len(email) >= 8:
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
        "amount" : amount,
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

#log in
def log_in(username, password):
    if username == user_name and password == password:
        message = "Logged in!"
    else:
        message = "Would you like to create an account?"

    return message

log_in = log_in('medreen', 'password')
print(log_in)

#deposit
def deposit(u_id, amount):
    if u_id == user_id:
        user['amount'] = user['amount'] + amount
        message = f'Deposited amount is ksh.{amount}'        
    else:
        message = 'User not found!'

    return message

deposit_total_amount = deposit(user_id, 1000)
print(deposit_total_amount)

#withdraw
def withdraw(u_id, amount):
    if u_id == user_id:
        user['amount'] = user['amount'] - amount
        message = f'Withdrawn amount is ksh.{amount}'       
    else:
        print('User not found')
    return message

withdraw_total_amount = withdraw(user_id, 100)
print(withdraw_total_amount)

#check balance
def check_balance(u_id):
    if u_id == user_id:
        balance = user["amount"]        
    else:
        balance = 'NULL'

    return f'Balance is ksh.{balance}'

balance = check_balance(user_id)
print(balance)

def delete_account(u_id):
    if u_id == user_id:
        message = f'User {u_id}\'s account has been deleted.'
        user.clear()
    else:
        message = 'User not found'
    
    return message

del_account = delete_account(user_id)
print(del_account)








    




