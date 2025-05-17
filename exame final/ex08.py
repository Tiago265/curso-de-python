# Realize a confecção de um sistema onde tenha uma função (def) que receba como parâmetro 3 
# números e um sinal(+ ou – ou *) retorne o resultado matemático dos 3 números



def somaOuMultiplicacao(num1, num2, num3, sinal):
    if sinal == "+":
        resultado = num1 + num2 + num3
    elif sinal == "*":
        resultado = num1 * num2 * num3
    elif sinal == "-":
        resultado = num1 - num2 - num3
    return resultado


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

d = input("Digite o sinal +, * ou -: ")

print(somaOuMultiplicacao(a, b, c, d))

# +1 ponto