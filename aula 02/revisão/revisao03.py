# 12/04/2025
# Atividade de revisão de if, else e elif
a = float(input("primeiro Lado: "))
b = float(input("segundo Lado: "))
c = float(input("terceiro Lado: "))

if(a + b > c and a + c > b and b + c > a):
    if a == b == c:
        print("Triângulo Equilatero")
    elif a == b or a == c or b == c:
        print("Triângulo Isoóceles")
    else: 
        print("Triângulo Escaleno")
else:
    print("Não é triângulo")