km = float(input())
litrosQuantidade = float(input())

kmPorLitro =  litrosQuantidade / km

if kmPorLitro < 8.0:
    print("Venda o carro!")
elif kmPorLitro >= 8.0 and kmPorLitro <= 14.0:
    print("Econômico!")
elif kmPorLitro > 14.0:
    print("Super econômico!")
