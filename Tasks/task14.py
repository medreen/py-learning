for i in range(3):
    num_1 = input('Enter any number: ')
    num_2 = input('Enter any number: ')

    try:
        # convert to numbers first
        int_num1 = int(num_1)
        int_num2 = int(num_2)

        sum_1 = int_num1 + int_num2
        sum_2 = float(num_1) + float(num_2)

        print("Integer sum:", sum_1)
        print("Float sum:", sum_2)

    except ValueError:
        print("Invalid character entered")
        break




