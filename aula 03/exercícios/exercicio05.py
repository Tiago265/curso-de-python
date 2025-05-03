# 03/05/2025


placaCaminhao = input("Digite a placa do caminhão: ")
kmInicial = float(input("Digite o Km inicial da viagem: "))
kmFinal = float(input("Digite o km final da viagem: "))
valorCombustivel = float(input("Digite o valor do combustível: "))
litrosAbasecidos = int(input("Digite quantos litros foram abastecidos: "))
kmTotal = kmInicial + kmFinal

def consumo(placaCaminhao, kmInicial, kmFinal, kmTotal, valorCombustivel, litrosAbastecidos):
    print(f"Caminhão placa {placaCaminhao} rodou {kmTotal}KM fazendo uma média de {litrosAbastecidos}KM/litro, gastando R${valorCombustivel}")


consumo(placaCaminhao, kmInicial, kmFinal, kmTotal, valorCombustivel, litrosAbasecidos)