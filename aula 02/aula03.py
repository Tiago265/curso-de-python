# 12/04/2025

senha = input("Digite sua senha: ")

while senha != "1234":
    senha = input("Digite a senha: ")
    if senha != "1234":
        print("Acesso negado! tente novamente")
print("Acesso liberado!")