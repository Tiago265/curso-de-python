# 10/05/2025

pilha = [4, 4, 5]
pilha.append(6)
pilha.append(7)
print(pilha)
pilha.pop()
print(pilha)
print(f"Temos essa quantidade de vezes o número 4: {pilha.count(4)}")
x = pilha.index(6) # vai te dizer em qual posição está 
print(x)
tamanho = len(pilha) # vai te dizer o tamanho todo do arry
print(tamanho)
pilha2 = [4,4,5]
pilha.extend(pilha2) # pega duas listas(array) e junta em um só
print(pilha)