#largest input
val_1 = input('Enter any value: ')
val_2 = input('Enter any value: ')
val_3 = input('Enter any value: ')

def largest():
    if len(val_1) > len(val_2) and len(val_1) > len(val_3):
     largest = {val_1}
    elif len(val_2) > len(val_1) and len(val_2) > len(val_3):
     largest ={val_2} 
    elif len(val_3) > len(val_1) and len(val_3) > len(val_2):
     largest = {val_3} 
    else:
     largest = (f'{val_2}, {val_1} and {val_3} are equal in length.')

    return f'{largest} is the largest in length.'
 
print(largest()) 

#even or odd number 
number = float(input('Enter a number: '))

def even_odd():
    if number % 2 == 0:
        if number % 4 == 0:
            value = f'{number} is an even number and is also divisible by 4.'
        else:
            value = f'{number} is an even number but is not divisible by 4.'
    elif number % 2 != 0:
        value = f'{number} is an odd number'
    else:
       value = f'{number} is not a number'

    return value

print(even_odd())

#area
base = float(input('Enter a base value(cm): '))
height = float(input('Enter a height value(cm): '))

def area():
    triangle_area = 1/2 * (base * height)

    return f'Area of a triangle with a base value of {base}cm and a height value of {height}cm is {triangle_area}cm.'

print(area())


#slide 70
maths = float(input('Enter Math score: '))
eng = float(input('Enter English score: '))
swa = float(input('Enter Kiswahili score: '))
sci = float(input('Enter Science score: '))
sos = float(input('Enter Social Studies score: '))

def total_marks():
    sum = maths + eng + swa + sci + sos
    average = sum // 5

    if average > 79:
        grade = 'A'
    elif average > 60 and average <= 79:
        grade = 'B'
    elif average > 59 and average <= 49:
        grade = 'C'
    elif average > 49 and average <= 40:
        grade = 'D'
    elif average > 40 and average <= 0:
        grade = 'E'
    else:
        grade = ''

    return f'Total Marks = {sum} \n Average Score = {average} \n Grade = {grade}'
    
x = total_marks()
print(x)



        
        

    
    

    
        

