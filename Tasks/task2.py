number = float(input('Enter a number: '))

if number % 2 == 0:
    if number % 4 == 0:
        print(f'{number} is an even number and is also divisible by 4.')
    else:
        print(f'{number} is an even number but is not divisible by 4.')
elif number % 2 != 0:
    print(f'{number} is an odd number')
else:
    print(f'{number} is not a number')