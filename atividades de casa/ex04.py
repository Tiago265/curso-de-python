# 4) Uma cidade pretende apurar os votos de sua eleição. Faça um programa para ler o
# número total de eleitores. Em seguida o número de votos do candidato X, o número de votos
# do candidato Y, total de votos brancos e total de votos nulos (a soma desses quatro, deve
# ser igual ao total de eleitores). Calcular e escrever o percentual que cada um representa
# em relação ao total de eleitores.


xVotos = int(input("Digite o número de votos do candidato x: "))
yVotos = int(input("Digite o número de votos do candidato y: "))

totalVotosBrancos = int(input("Digite o números de votos em branco: "))
totalVotosNulos = int(input("Digite o número total de votos nulos: "))

nTotalEleitores =  (xVotos + yVotos + totalVotosNulos + totalVotosBrancos) / 100

print(f"{nTotalEleitores}%")
