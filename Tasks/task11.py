import datetime

today = datetime.datetime.now()

birthday = list(input("Enter a date(yyyy, mm, dd): "))
birthday = ' '.join(birthday).replace(' ', '').replace(',', ' ')

if len(birthday) == 10:
    year = int(birthday[0:5])
    month = int(birthday[5:8])
    day = int(birthday[8:10])

    user_birthday = datetime.datetime(year, month, day)
    age = today.year - user_birthday.year
    print(age)

else:
    print('Enter valid date!')


 





