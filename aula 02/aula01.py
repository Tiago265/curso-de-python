# 12/04/2025
#aula de matche e case
diasdaSemana = str(input("Digite o dia da semana: "))

match diasdaSemana:
        case "segunda":
            print("Fazer relatório.")
        case "terça":
            print("Reunião")
        case "quinta":
            print("Visitar cliente")
        case other:
          print("Pode ir para praia")