# 03/05/2025
# Aula de POO = Programação Orientada Objeto

# Criando uma classe
# self = construtor
# __init__ = colocar todos os atributos

class vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "Bateu a meta")
        else:
            print(self.nome,"Não bateu a meta")

vendedor1 = vendedor("Lira")
vendedor1.vendeu(int(input("Digite quantas vendas o Lira fez: ")))
# vendedor1.bateu_meta(int(input("Digite a meta de vendas do Lira: ")))
# vendedor1.vendeu(1000)
# vendedor1.bateu_meta(600)

class vendedor2():
    def __init__(self, nome, produto):
        self.nome = nome
        self.vendas = 0
        self.produto = produto

    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f"{self.nome} bateu a meta")
        else:
            print(f"{self.nome} não bateu a meta")

vendedor2 = vendedor2("Tiago", "Paçoca")
vendedor2.vendeu(int(input("Digite quantas Paçocas o Tiago vendeu: ")))
# vendedor2.bateu_meta(int(input("Digite a meta de vendas do Tiago: ")))
# vendedor2.vendeu(120)
# vendedor2.bateu_meta(150)

class vendedor3():
    def __init__(self, nome, produto, local, cpf):
        self.nome = nome
        self.vendas = 0
        self.produto = produto
        self.local = local
        self.cpf = cpf
    
    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f"{self.nome} bateu a meta")
        else:
            print(f"{self.nome} não bateu a meta")

vendedor3 = vendedor3("Lucas", "carros", "Florianópolis", "106-421-869-52")
vendedor3.vendeu(int(input("Digite quantos carros o Lucas vendeu:  ")))
# vendedor3.bateu_meta(int(input("Digite a meta de venda: ")))
# vendedor3.vendeu(150)
# vendedor3.bateu_meta(4000)

def maior():
    if vendedor1.vendas > vendedor2.vendas and vendedor1.vendas > vendedor3.vendas:
        print(f"O {vendedor1.nome} vendeu mais produtos.")
    elif vendedor2.vendas > vendedor1.vendas and vendedor2.vendas > vendedor3.vendas:
        print(f"O {vendedor2.nome} vendeu mais produtos.")
    elif vendedor3.vendas > vendedor2.vendas and vendedor3.vendas > vendedor1.vendas:
        print(f"O {vendedor2.nome} vendeu mais produtos.")
maior()