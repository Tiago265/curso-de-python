# 05/04/2025

nomeDaPessoa = input("Digite seu nome: ")
nomeDoCarro = input("Digite o nome do carro: ")
valorDoCarro = float(input("Digite o valor do carro: "))
percentualDeDesconto = float(input("Digite quantos '%' de desconto você quer: "))

porcentagem = (valorDoCarro) * ((percentualDeDesconto) / 100)
valorFinal = (valorDoCarro) - (porcentagem)

print("O nome da pessoa digitado foi: ",nomeDaPessoa)
print("O nome do carro digitado foi: ",nomeDoCarro)
print("O valor do carro digitado foi: ",valorDoCarro)
print("A porcentagem de desconto foi: ",percentualDeDesconto,"%")
print("Subtotal: ",valorFinal)