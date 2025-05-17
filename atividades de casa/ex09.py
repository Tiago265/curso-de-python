# 10) Escreva um programa que gera um número aleatório entre 1 e 100 e permite que o
# usuário tente adivinhá-lo. O programa deve informar se o palpite é maior ou menor que o
# número gerado. Use um loop while para permitir que o usuário faça múltiplos palpites. Dica:
# Utilize a variável numero_secreto = random.randint(1, 100) para gerar o número aleatório.
import random

numero_secreto = random.randint(1,100)
acerto = int(input("Digite o número aleatório: "))
while 1 <= 100:
    if acerto == numero_secreto:
        print("Você acertou!")
    else:
        print("Errou!")
