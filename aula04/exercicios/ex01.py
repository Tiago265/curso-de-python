# 10/05/2025

# Classe
class carro:
    def __init__(self,modelo, marca, ano,cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano 
        self.cor = cor

    def dados(self):
        print(f'o modelo do carro é {self.modelo}, a marcar é {self.marca}, o ano é {self.ano}, a cor é {self.cor}. ')

carro1 = carro('Huracán','Lamborgini', '1908', 'Amarelo', )  

carro1.dados()