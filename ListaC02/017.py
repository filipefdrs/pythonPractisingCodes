altura = float(input())
baseMaior = float(input())
baseMenor = float(input())
area = None

if baseMaior > 0.0 and baseMenor > 0.0:
    area = ((baseMaior + baseMenor) * altura) / 2.0
    print("Area do trapezio:")
else:
    print("Base(s) invalida(s)")
