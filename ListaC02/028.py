a = int(input())
b = int(input())
c = int(input())

geometrica = (a * b * c) ** (1/3)
ponderada = (a * 2 * b + 3 * c) / 6
harmonica = 1 / ((1/a) + (1/b) + (1/c))
aritmetica = (a + b + c) / 3

print("Média Geométrica:", geometrica)
print("Média Ponderada:", ponderada)
print("Média harmonica:", harmonica)
print("Média aritmética:", aritmetica)
