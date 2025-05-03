# 03/05/2025

a = input("Digite o nome do aluno 1: ")
b = input("Digite o nome do aluno 2: ")
c = input("Digite o nome do aluno 3: ")

notaa1 = float(input("Digite a nota 1 do aluno 1: "))
notaa2 = float(input("Digite a nota 2 do aluno 1: "))
notab1 = float(input("Digite a nota 1 do aluno 2: "))
notab2 = float(input("Digite a nota 2 do aluno 2: "))
notac1 = float(input("Digite a nota 1 do aluno 3: "))
notac2 = float(input("Digite a nota 2 do aluno 3: "))

def media(a,b,c,notaa1,notaa2,notab1,notab2,notac1,notac2):

    mediaa = (notaa1 + notaa2) / 2
    mediab = (notab1 + notab2) / 2
    mediac = (notac1 + notac2) / 2

    if mediaa > mediab and mediaa > mediac:
        print(f"{a} é o aluno com maior média {mediaa}")
    elif mediab > mediaa and mediab > mediac:
        print(f"{b} é o aluno com maior média {mediab}")
    else:
        print(f"{c} é o aluno com maior média {mediac}")
media(a,b,c,notaa1,notaa2,notab1,notab2,notac1,notac2)

