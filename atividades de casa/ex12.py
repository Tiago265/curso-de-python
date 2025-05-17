# 12) Um cliente comprou 4 produtos no mercado. Peça o preço de cada produto e calcule o
# total da compra.
lista_de_compras = []
soma = 0

for i in range(4):
    produtos = input("Digite um produto que queira comprar: ")
    preco = int(input("Digiteo preço do produto: "))
    lista_de_compras.append(preco)

for i in range(4):
    soma =  soma + lista_de_compras[i]
print(f"O total deu R${soma:.2f}")