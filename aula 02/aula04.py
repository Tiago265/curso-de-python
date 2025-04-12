# 12/04/2025
# aula de for

# for i in range(1,10,2):start,stop,step
#     print(i)

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
passo = int(input("Digite o passo: "))

for i in range(inicio, fim + 1, passo):
    print(i)

print("Acabou")

