# 03/05/2025


placaCaminhao = input("Digite a placa do caminhão: ")
kmInicial = int(input("Digite o Km inicial da viagem: "))
kmFinal = int(input("Digite o km final da viagem: "))
valorCombustivel = float(input("Digite o valor do combustível: "))
qtdCombustivel = float(input("Digite a quantidade de combustível gasto na viagem: "))

def viagem(placaCaminhao,kmInicial,kmFinal,valorCombustivel,qtdCombustivel):
    kmPercorrido = kmFinal - kmInicial
    valorTotal = qtdCombustivel * valorCombustivel
    media = kmPercorrido / qtdCombustivel
    print(f"Placa do caminhão: {placaCaminhao} rodou {kmPercorrido}KM, fazendo uma média de {media}KM/L ,e gastando R${valorTotal} com combustivel")
viagem(placaCaminhao,kmInicial,kmFinal,valorCombustivel,qtdCombustivel)