# 05/04/2025

nome = input("Digite seu nome: ")

qtdDiasAlugado = int(input("Digite quantos dias você alugou o carro: "))
qtdKmRodados = float(input("Digite quantos km foram Rodados: "))

valorQtdDiasAlugado = float(input("Digite o valor que deve ser da diaria de locação: "))
valorQtdkmRodados = float(input("Digite o valor que deve ser por km rodado: "))

valorTotal = (qtdDiasAlugado * valorQtdDiasAlugado) + (qtdKmRodados * valorQtdkmRodados)

print("O nome digitado foi: ",nome)
print("O total a pagar é : R$",valorTotal)