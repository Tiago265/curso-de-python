# 03/05/2025

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
x = int(input("Digite número para calcular fatorial: "))
print(fatorial(x))