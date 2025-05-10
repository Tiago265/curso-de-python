# 10/05/2025

# Criando a classe Animal - Super-classe

class Animal:

    def __init__ (self,nome, especie):
        self.nome = nome
        self.especie = especie
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")

    def emitir_som(self):
        pass

# Criando a classe cachorro - Sub-classe

class Cachorro(Animal):

    def __ini__(self,nome, especie, raca):
        super().__init__(nome, especie)
        self.raca = raca
        print("Cachirro foi criado.")
        # Animal.__init__(self)

    def emitir_som(self):
        print("AU AU!")

cachorro1 = Cachorro('Paçoca', 'Pit Bull')
cachorro1.emitir_som()

