number = float(input())
raiz = None

if number >= 0:
    raiz = number ** (1/2)
    print("Squared root is", raiz)
else:
    print(number, "to the power of two is", number ** 2)
