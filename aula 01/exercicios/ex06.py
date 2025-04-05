# 05/04/2025

nome = input("Digite seu nome: ")
qtdDiasCarroAlugado = int(input("Digite quantos dias o carro foi alugado: "))
qtdKmRodado = float(input("Digite quantos kilo mêtros foram rodados: "))

total = (qtdDiasCarroAlugado * 60) + (qtdKmRodado * 0.15)

print("O nome digitado foi: ",nome)
print("A quantidade de dias alugados foi: ",qtdDiasCarroAlugado)
print("A quantidade de kilo mêtros rodados foi: ",qtdKmRodado)
print(total)