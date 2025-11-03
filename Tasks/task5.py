val_1 = input('Enter anything: ')
val_2 = input('Enter anything: ')
val_3 = input('Enter anything: ')

if len(val_1) > len(val_2) and len(val_1) > len(val_3):
    print(f'{val_1} is greater than {val_2} and {val_3}.')
elif len(val_2) > len(val_1) and len(val_2) > len(val_3):
    print(f'{val_2} is greater than {val_1} and {val_3}.')
elif len(val_3) > len(val_1) and len(val_3) > len(val_2):
    print(f'{val_3} is greater than {val_1} and {val_2}.')
else:
    print(f'{val_2}, {val_1} and {val_3} are equal in length.')
