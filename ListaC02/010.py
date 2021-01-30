height = float(input())
gender = input()

if gender == 'h' or gender == 'H':
    print("Ideal weight:", (72.7 * height) - 58)
elif gender == 'M' or gender == 'm':
    print("Ideal weight:", (62.1 * height) - 44.7)
