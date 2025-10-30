#Find largest input
num = input('Enter a number of your choice: ')
string = input('Enter text of your choice: ')
name = input('Enter your name: ')

if len(num) > len(string) and len(num) > len(name):
    print(f'{num} is greater than {string} and {name}')
elif len(string) > len(num) and len(string) > len(name):
    print(f'{string} is greater than {name} and {num}')    
elif len(name) > len(string) and len(name) > len(num):
    print(f'{name} is greater than {string} and {num}') 
 
#temperature
temp = input("Enter the temp(in degrees celcius): ")  

if int(temp) > 30 and int(temp) >= 15:
    print('The temperature is too high.')
elif int(temp) > 15 and int(temp) >= 0:
    print('Normal temperature.')
else:
    print('Cold temperature.')

#checks variable
x = 11
y = 890

if x >= 10 and x <= 20:
    if y > 100:
        print('Conditions met')
else:
    print('Conditions not met')

#password checker
password = 'Secret123'

if password == 'secret123':
    print('Access granted.')
else:
    print('Access denied.')

#student
student_score = 92
attendance = 89

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print('Good score, but attendance needs improvement')


    
#nested if
transaction_amount = input('Enter transaction amount: ')
account_type = input('Is account Standard or Premium: ')

if account_type.title() == 'Standard':
    if int(transaction_amount) > 500:
        print('Transaction exceeds the limit for Standard accounts.')
    else:
        print('Transaction approved.')
elif account_type.title() == 'Premium':
    if int(transaction_amount) > 1000:
        print('Transaction exceeds the limit for Premium accounts.')
    else:
        print('Transaction approved.')


#date
start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date < end_date:
    print('Valid period.')
elif start_date > end_date:
    print('Invalid period.')
elif start_date == end_date:
    print('One-day period.')

#string
str1 = 'Henry'
str2 = 'Juo'

if len(str1) > len(str2):
    print(f'{str1} is longer than {str2}')
elif len(str2) > len(str1):
    print(f'{str2} is longer than {str1}')  
if len(str1) == len(str2):
    print(f'Both {str1} and {str2} are equal length') 
    
     

   




