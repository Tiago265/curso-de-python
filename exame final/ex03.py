# Escreva um programa que leia a 5 nota de um aluno e classifique como "Aprovado", "Recuperação" ou 
# "Reprovado"
# Média Maior ou igual 7 aprovado
# Média entre 5.0 e 6.9 recuperações
# Média abaixo de 5.0 reprovado

# A soma das 5 divido por 5



nota1 = int(input("Digite quantos de nota você tem: "))
nota2 = int(input("Digite quantos de nota você tem: "))
nota3 = int(input("Digite quantos de nota você tem: "))
nota4 = int(input("Digite quantos de nota você tem: "))
nota5 = int(input("Digite quantos de nota você tem: "))

notaTotal = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if notaTotal >= 7:
    print("Aprovado")
elif notaTotal >= 5.0 and notaTotal <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")

# +1 ponto
