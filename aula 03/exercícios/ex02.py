# 03/05/2025

print("Executando antes da função")
def vendaCarro(valor, imposto, comissao):
    valorFinal = valor - (valor * imposto) - (valor * comissao)
    print(valorFinal)
print("Execução depois da função")
print("Começou o programa principal")
valorCarro = int(input("Digite o valor do carro: "))
impostoCarro = float(input("Digite o valor do imposto: "))
comissaoCarro = float(input("Digite o valor da comissão: "))
vendaCarro(valorCarro, impostoCarro, comissaoCarro)
print("Já executou a função vendaCarro")