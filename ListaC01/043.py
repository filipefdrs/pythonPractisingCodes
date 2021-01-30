valorTotalLido = float(input())

totalAPagarComDesconto = valorTotalLido - valorTotalLido * 0.1
valorDeCadaParcela = valorTotalLido / 3.0
comissaoDoVendedorVendaAVista = totalAPagarComDesconto * 0.05
comissaoDoVendedorVendaParcelada = valorTotalLido * 0.05

print(totalAPagarComDesconto)
print(valorDeCadaParcela)
print(comissaoDoVendedorVendaAVista)
print(comissaoDoVendedorVendaParcelada)
