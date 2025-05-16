# 5) Uma pousada cobra R$280 reais a diária por quarto e R$15 reais o café por pessoa por
# dia. Você pretende passar um tempo com alguns amigos nessa pousada, sendo que todos
# ficarão no mesmo quarto. Informar a quantidade de pessoas, o número de diárias e quantas
# pessoas do grupo vão querer café diário. Mostrar na tela o total a pagar.

diaria = 280
cafe = 15

amigos = int(input("Digite o número de amigos que você deseja hospedar no quarto: "))

torpedoCafe = input("Você gostaria de um café? ")

if torpedoCafe == "sim" or torpedoCafe == "Sim":
    cafeConfirmado = int(input("Digite quantos cafés você gostaria: "))
    totalCafe = cafeConfirmado * 15
    totalAhPagar = (cafeConfirmado * 15) + (diaria * amigos)
    print(f"O total deu {totalAhPagar}")
elif torpedoCafe == "não" or torpedoCafe == "Não":
    print(f"O total deu {diaria * amigos}")