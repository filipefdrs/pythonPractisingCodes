weekDay = int(input())

if weekDay >= 1 and weekDay <= 7:
    if weekDay == 1:
        print("Sunday")
    elif weekDay == 2:
        print("Monday")
    elif weekDay == 3:
        print("Tuesday")
    elif weekDay == 4:
        print("Wednesday")
    elif weekDay == 5:
        print("Thursday")
    elif weekDay == 6:
        print("Friday")
    elif weekDay == 7:
        print("Saturday")
else:
    print("Invalid number of weekDay")
