# 03/05/2025

def calcular(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

cont = int(input("Quantos alunos querem fazer a análise de notas? "))
for i in range(cont):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = calcular(n1,n2)
    n3 = float(input("Digite o ponto extra: "))
    mediaFinal = media + n3
print(f"Média final do aluno {i+1} é {mediaFinal}")