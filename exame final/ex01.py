# Realize a confecção de um sistema que solicite ao usuário nome, e-mail, idade, salário de janeiro, salário de fevereiro e salário de março. 
# Ao final deve mostrar nome do cliente, e-mail do cliente, idade do cliente e soma dos 3 meses de salário.

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
idade = input("Digite sua idade: ")
salario_janeiro = float(input("Digite o seu salário de janeiro: "))
salario_fevereiro = float(input("Digite o seu salário de fevereiro: "))
salario_marco = float(input("Digite o seu salário de março: "))

salarioTotal = salario_fevereiro + salario_janeiro + salario_marco

print(f"nome do cliente é {nome}, o e-mail do cliente é {email}, a idade do cliente é {idade} e o salário total do cliente é {salarioTotal:2}.")

# +1 ponto