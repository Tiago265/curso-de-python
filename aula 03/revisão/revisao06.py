# 03/05/2025

lista1 = [1,16,24,39,47]
lista2 = [32,89,47,76,12]

# Loop externo
for elemento_lista1 in lista1:

    # Loop interno
    for elemento_lista2 in lista2:

        # condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:

            print("O número 47 encontrado nas duas listas!")