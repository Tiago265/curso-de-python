# 11) Peça o nome de 5 alunos usando for, armazene em uma lista e depois mostre todos os
# nomes.

lista_nomes = []

for i in range(5):
    nome = input("Digite alguns nomes: ")
    lista_nomes.append(nome)
print(lista_nomes)