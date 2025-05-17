# 9) Crie um programa que solicita ao usuário uma nota (de 0 a 10) e exibe a mensagem
# correspondente: &quot;Aprovado&quot; se a nota for 7 ou maior. &quot;Em recuperação&quot; se a nota estiver
# entre 4 e 6. &quot;Reprovado&quot; se a nota for menor que 4.]

nota1 = int(input("Digite sua primeira nota do trimestre: "))
nota2 = int(input("Digite sua segunda nota do trimestre: "))
nota3 = int(input("Digite sua terceira nota do trimestre: "))

media = nota1 + nota2 + nota3 / 3

if media >= 7:
    print("Aprovado!")
elif media >= 4 and media <= 6:
    print("Em recuperação")
elif media < 4:
    print("Reprovado") 