nomeDaPessoa = input("Digite seu nome: ")
nomeDoCarro = input("Digite o nome do carro: ")
valorDoCarro = float(input("Digite o valor do carro: "))
percentualDeDesconto = float(input("Digite quantos '%' de desconto você quer: "))
porcentagem = (valorDoCarro) * (percentualDeDesconto) - 100
valorFinal = (valorDoCarro) - (percentualDeDesconto)

print(valorFinal)

