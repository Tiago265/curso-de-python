# Realize a confecção de um sistema que solicite ao usuário apontar quanto números quer digitar.
# Após solicite que digite números na quantidade de valor informado anteriormente e após digitação dos 
# números pelo usuário informar qual maior e qual menor.
numerosX = []

numeros = int(input("Digite quantos números você quer no for: "))
maior = 0

for i in range(numeros):
    numeros = int(input("Digite numeros: "))
    if numeros > maior:
        numerosX.append(numeros)
print(max(numerosX))

# +1 ponto