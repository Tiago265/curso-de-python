# Peça 10 números e diga quantos são pares e quantos são ímpares. Utilize For, if e também 
# (%) para pegar o resto que deve ser = a zero quando par.



for numero in range(10):
    numero = int(input("Digite qualquer número: "))
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

# +1 ponto
    