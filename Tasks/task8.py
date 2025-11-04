speed = float(input("Enter speed: "))
speed_limit = 70

if speed < 70:
    print("OK")
else:
    speed_exceeded = speed - speed_limit
    demerit_points = speed_exceeded // 5

    if speed_exceeded%5 != 0:
        demerit_points += 1
    if demerit_points > 12:
        print(f"Demerit points -> {demerit_points}")
        print("License suspended")
    else:
        print(f"Demerit points -> {demerit_points}")

