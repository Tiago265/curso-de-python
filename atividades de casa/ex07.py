# 7) Crie uma função chamada calcular_area_circulo que receba o raio de um círculo como
# parâmetro e retorne a área do círculo (use a fórmula A = π * r², onde π pode ser
# aproximadamente 3.14). Exiba o resultado fora da função.



r = int(input("Digite o valor do raio: "))
pi = 3.14

def calcular_area_circulo(r,pi):
    a = pi * r*r
    print(f"O valor da area é {a}")

calcular_area_circulo(r)