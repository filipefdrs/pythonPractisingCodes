lab = float(input())
avs = float(input())
exf = float(input())
media = None

if lab >= 0.0 and avs >= 0.0 and exf >= 0.0 and lab <= 10.0 and avs <= 10.0 and <= exf 10.0:
    media = (lab + avs + exf) / 3.0
    if media >= 0.0 and media <= 2.9:
        print("Media:", media)
        print("Aluno reprovado")
    elif media >= 3.0 and media <= 4.9:
        print("Media:", media)
        print("Aluno em recuperação")
    else:
        print("Media:", media)
        print("Aluno aprovado")
