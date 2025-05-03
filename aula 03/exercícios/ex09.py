# 03/05/2025

# Não pode chamar a função antes de criar ela
# return = é tudo que pode ser retornado
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
# o def cria uma função com ou sem recebimento de parametro
def maior(n1,n2,n3): 
    if n1 > n2 and n1 > n3:
       return n1
    elif n2 > n1 and n2 > n3:
       return n2
    elif n3 > n1 and n3 > n2:
       return n3


resultado = maior(a,b,c)
print("resultado foi" , resultado)
