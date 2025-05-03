# 03/05/2025

x = float(input("Digite o lado: "))
y = float(input("Digite o outro lado: "))

def area(x,y):
    return x*y

def perimetro(x,y):
    return (x+y) * 2 

areaRetangulo = area(x,y)
perimetroRetangulo = perimetro(x,y)
print(f"Área do retângulo é {areaRetangulo} e o perimetro é {perimetroRetangulo}.")
