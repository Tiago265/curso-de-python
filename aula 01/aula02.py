# 05/04/2025

# Operadores lógicos

# >= Maior igual que
# <= Menor igual que
# != diferente que
# < menor que
# > maior que
# == igual

nomeAluno = input("Digite seu nome: ")
idadeAluno = int(input("Digite sua idade: "))
if idadeAluno >= 18:
    print("O aluno(a)",nomeAluno,"é maior de idade e pode fazer CNH.")
    print("carteira de motorista custa R$5000,00")
else:
    print("O aluno(a)",nomeAluno,"é menor de idade e não pode fazer CNH.")