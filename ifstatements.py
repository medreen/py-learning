number = float(input('Enter a number: '))

if number%2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

age = int(input("Enter your age: ")) 

if abs(age) < 18:
    print("You must be above 18 years!!!")
else:
    print("Welcome!!!")