#ids
list = [101, 102, 103]
variable_id = 105

if variable_id == id in list:
    print('Access Granted')
else:
    print('Access Denied')

#type
my_var = 9038

if isinstance(my_var, str):
    print('String Detected..')
elif isinstance(my_var, int):
    print('Integer Detected')
else:
    print('Unknown Type.')

#nest
x = 7
y = 14

if y % 2 == 0:
    if x % 2 == 0:
        print(f'Both {y} and {x} are equal.') 
    else:
        print(f'Only {y} is an even number.')
else:
    print(f'Neither {x} or {y} are even.')

#loops
for x in range(51):
    print(x, end=", " )

#2
for x in range(51):
    if x % 7 == 0 or x % 5 == 0:
        print(f'Either divisible by 7 or 5: {x}')
    
#3
sum = 0
average = 0
for x in range(51):
    if x > 10 and x < 40:
        sum += x
        average = sum / (50/2)    
print(sum)
print(average)

#4
lst = []
for x in range(51):
    if x % 2 != 0:
        lst.append(x)
print(lst)

#5
num = int(input('Enter any number of your choice: '))
for x in range(11):
    print(f'Mutliplied by {x}: {num * x}.')

#6
even_numbers = []
for x in range(51):
    if x % 2 == 0:
        even_numbers.append(x)
        count_x = len(even_numbers)
print(f'Has {count_x} even numbers.')

#7
total = 0
ls1 = [("Jay", "20"), ("Mo", "30"), ("Mya", "32")]
for x in ls1:
    total = total + int(x[1])
print(f'Total quantity in {ls1} is : {total}.')


