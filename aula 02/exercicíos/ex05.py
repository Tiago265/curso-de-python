# 12/04/2025

numero = float(input("Digite um número: "))
total = 0

while (numero > 0):
    print("Passou da primeira linha do while")
    total = total + numero
    numero = float(input("Digite um número: "))
    print("Última linha do while")

print("Foi digitado um número negativo, ecerrado o programa.")
print("Total acumalado: ",total)