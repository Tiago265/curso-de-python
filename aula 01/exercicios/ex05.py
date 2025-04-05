# 05/04/2025

nomeDoFuncionario = input("Digite o nome do funcionário: ")
DiasTrabalhados = int(input("Digite os dias que ele trabalhou: "))
horasTrabalhadas = int(input("Digite quantas horas ele Trabalhou: "))
minutostrabalhados = int(input("Digite quantos minutos ele trabalhou: "))
segundosTrabalhados = int(input("Digite qauntos segndos ele trabalhou: "))

total = (DiasTrabalhados * 86400) + (horasTrabalhadas * 3600) + (minutostrabalhados * 60) + segundosTrabalhados

print("O nome digitado foi: ")
print("O total de segundos é: ",total)

