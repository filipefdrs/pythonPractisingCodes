apostador1 = float(input())
apostador2 = float(input())
apostador3 = float(input())
valorDoPremio = float(input())

totalInvestido = apostador1 + apostador2 + apostador3

proporcao1 = valorDoPremio * (((apostador1 * 100.0) / totalInvestido) / 100)
proporcao2 = valorDoPremio * (((apostador2 * 100.0) / totalInvestido) / 100)
proporcao3 = valorDoPremio * (((apostador3 * 100.0) / totalInvestido) / 100)

print("Apostador 1 ganharia:", proporcao1)
print("Apostador 2 ganharia:", proporcao2)
print("Apostador 3 ganharia:", proporcao3)
