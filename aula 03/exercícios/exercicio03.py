# 03/05/2025

a = int(input("Digite um número: "))
b = int(input("Digite o número de quantas vezes vai ser múltiplicado: "))
def taboada(x, y):
    for i in range(y + 1):
        print(x," X ",i," = ", x*i)
taboada(a, b)