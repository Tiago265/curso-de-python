# 3) Você é um amante da natureza e adora fazer trilhas. Criar um programa que calcule a
# velocidade média das trilhas que você realiza. Para isso, devem ser digitados os dados de
# distância percorrida (quilômetros) e tempo que a trilha durou (horas). Fazer então o cálculo
# da velocidade média e mostrar na tela a mensagem &quot;Sua média de velocidade durante essa
# trilha foi de X km/h&quot;, sendo X a velocidade.

distanciaPercorridaKM = int(input("Digite quantos quilômetros: "))
tempoTrilha = int(input("Digite quantas horas você trilhou: "))

# velocidade média = distância total / tempo total
velocidadeMedia = distanciaPercorridaKM / tempoTrilha

print(f"Sua média de velocidade durante essa trilha foi de {velocidadeMedia} km/hrs")