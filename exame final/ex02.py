# Realize a confecção de um sistema que solicite ao usuário nome e idade, informando posteriormente
# nome digitado e se o usuário pode ter carteira nacional de habilitação ou se ainda é menor de idade.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome} é maior de idade, portanto pode ter cnh.")
else:
    print(f"{nome} é menor de idade, portanto não pode ter cnh.")

# +1 ponto
