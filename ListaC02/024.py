price = float(input())
province = input()

if province == "MG":
    price = price + (price * 0.07)
    print("Total is", price)
elif province == "SP":
    price = price + (price * 0.12)
    print("Total is", price)
elif province == "RJ":
    price = price + (price * 0.15)
    print("Total is", price)
elif province == "MS":
    price = price + (price * 0.08)
    print("Total is", price)
else:
    print("Invalid province")
