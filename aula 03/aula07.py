#  03/05/2025

class pessoa:
    # Método construtor: inicializa cada nova instância da classe pessoa
    def __init__(self, nome, idade):
        self.nome = nome # Atributo para armazenar o nome
        self.idade = idade # Atributo para armazenar a idade

    # Método de instância: exibe uma mensagem de apresentação
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criação de uma instância da classe pessoa
pessoa1 = pessoa("João", 25)

# Chamada ao método que apresenta a pessoa
pessoa1.apresentar()