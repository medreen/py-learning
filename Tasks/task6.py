password = input('Enter the password: ')
actual_pasword = 'admin@123'
i = 0 

while i < 3:  
    i = i + 1  
    if password != actual_pasword:
        input('Enter the password: ')    
    elif password == actual_pasword:
        print('Access granted')
        break

print('Maximum attempts.')