number = int(input())
sum = None

if number > 0:
    unidade = number % 10
    number = number - unidade

    dezena = number % 100
    number = number - dezena
    dezena = dezena // 10

    centena = number % 1000
    number = number - centena
    centena = centena // 100

    unidadeDeMilhar = number // 1000

    print(unidadeDeMilhar + centena + dezena + unidade, "(", unidadeDeMilhar, "+", centena, "+", dezena, "+", unidade, ")")
else:
    print("Invalid number")
