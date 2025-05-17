# 6) Criar um programa que calcule o IMC, no qual o usuário deve digitar o seu peso e altura,
# realizar o cálculo (peso / altura * altura) e mostrar o resultado na tela, com 3 casas depois
# da vírgula

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imcTotal = peso / (altura * altura) 

if imcTotal < 18.5:
    print("Você está abaixo do peso")
elif imcTotal > 18.5 and imcTotal < 24.9:
    print("Você está no peso ideal")
elif imcTotal >=  25 and imcTotal <= 29.9:
    print("Você está sobrepeso")
elif imcTotal >= 30 and imcTotal <= 34.9:
    print("Você esta na obesidade no grau I")
elif imcTotal >= 35 and imcTotal <= 39.9:
    print("Você está na obesidade no grau II")
elif imcTotal >= 40:
    print("(Obesidade mórbida) você está com obesidade grau III")