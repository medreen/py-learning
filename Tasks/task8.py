speed = int(input('Enter the car speed(km/hr): '))
demerit_point = 0


if speed < 70:
    print('Ok')
elif speed > 70:
    
    for 5 in range(speed - 70):
        demerit_point = demerit_point + 1
        print(demerit_point)

