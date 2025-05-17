# 8) Escreva uma função chamada converter_temperatura que receba uma temperatura em
# graus Celsius como parâmetro e retorne a temperatura convertida para Fahrenheit. Use a
# fórmula F=C×95+32F = C \times \frac{9}{5} + 32F=C×59 +32. Exiba o resultado fora da
# função.
grauCelcius = int(input("Digite quantos graus está: "))

def converter_temperatura(grauCelcius):
    f = grauCelcius * 1.8 + 32
    print(f)
    
converter_temperatura(grauCelcius)

