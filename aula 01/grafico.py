import matplotlib.pyplot as plt
nome1 = input("Nome 01: ")
nome2 = input("Nome 02: ")
nome3 = input("Nome 03: ")

venda1 = float(input("Digite valor 01: "))
venda2 = float(input("Digite valor 02: "))
venda3 = float(input("Digite valor 03: "))

x = [venda1,venda2,venda3]
y = [nome1,nome2,nome3]

#  plt.scatter: Gráfico de pontos

plt.bar(y,x)
plt.show

# pip install matplotlib: comando para instalar a biblioteca

# Colab.google para rodar o gráfico