number = int(input())

unidade = number % 10
number = number - unidade

dezena = number % 100
number = number - dezena
dezena = dezena / 10

centena = number / 100
number = number - centena

number = (unidade * 100) + (dezena * 10) + centena
print(int(number))
