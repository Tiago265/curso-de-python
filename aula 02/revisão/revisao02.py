# 12/04/2025
# Atividade de revisão de if e else
n1 = float(input("Digite a sua primeira nota:"))
n2 = float(input("Digite a sua segunda nota:"))

media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")