pSide1 = float(input())
pSide2 = float(input())
pSide3 = float(input())

if pSide1 < pSide2 + pSide3 and pSide2 < pSide1 + pSide3 and pSide3 < pSide1 + pSide2:
    if pSide1 == pSide2 and pSide2 == pSide3:
        print("Equilateral triangle")
    elif (pSide1 == pSide2 and pSide2 != pSide3) or (pSide1 != pSide2 and pSide2 == pSide3):
        print("Isosceles triangle")
    elif pSide1 != pSide2 and pSide2 != pSide3:
        print("Scalene triangle")
else:
    print("It's not a triangle")
