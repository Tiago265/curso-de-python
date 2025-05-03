# 03/05/2025

def somaOuMultiplicacao(num1, num2, num3, sinal):
    if sinal == "+":
        soma = num1 + num2 + num3
        print(soma)
    elif sinal == "*":
        multiplicacao = num1 * num2 * num3
        print(multiplicacao)
    else:
        print("Digite um sinal valido na próxima vez.")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

d = input("Digite o sinal + ou *: ")

somaOuMultiplicacao(a, b, c, d)





  
