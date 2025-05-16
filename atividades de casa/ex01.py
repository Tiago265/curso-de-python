# 1) Crie um programa que peça os dados de um cliente: Nome, idade, nacionalidade,
# endereço. Após digitados os dados, mostrar na tela a seguinte mensagem &quot;Cliente [Nome],
# com [idade] anos, [nacionalidade], reside no endereço [endereço]&quot;. Exemplo: Cliente Lucas,
# com 29 anos, brasileiro, reside no endereço Rua Victor Meirelles, 281, Centro,
# Florianópolis.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nacionalidade = input("Digite a sua nacionalidade: ")
endereco = input("Digite seu endereço: ")

print(f"Cliente {nome}, com {idade} anos, {nacionalidade}, reside no endereço {endereco}.")
