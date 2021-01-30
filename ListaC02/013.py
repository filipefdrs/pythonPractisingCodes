prova1 = float(input())
prova2 = float(input())
prova3 = float(input())


mediaPonderada = (prova1 * 1 + prova2 * 1 + prova3 * 2) / 4.0

print("Media:", mediaPonderada)
if mediaPonderada >= 60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
