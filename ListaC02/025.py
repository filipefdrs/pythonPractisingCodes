a = float(input())
b = float(input())
c = float(input())
delta = None
x = None

if a == 0.0:
    print("It's not a second degree function")
else:
    delta = (b ** 2) - (4 * a * c)
    if delta < 0.0:
        print("There is no real root")
    elif delta == 0.0:
        x = (-b) / (2 * a)
        print(x, "is the root. Unique root.")
    elif delta > 0.0:
        x = (-b + ((delta) ** (1/2))) / (2 * a)
        print(x, "is the one real root.")

        x = (-b - ((delta) ** (1/2))) / (2 * a)
        print(x, "is a second real root.")
