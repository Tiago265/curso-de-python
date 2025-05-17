# Leia uma senha do usuário. Enquanto a senha estiver incorreta fique repetindo a solicitação. 
# Utilize o While.

senhaUsuario = int(input("Digite sua senha: "))

while senhaUsuario != "1234":
    senhaUsuario = input("Digite a senha: ")
    if senhaUsuario != "1234":
        print("Acesso negado! tente novamente")
print("Acesso liberado!")

# +1 ponto