# 10/05/2025

# Clase Livro

class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

    def informacoes(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nAno de Publicação: {self.ano_publicado}\n'
    
# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self,livro):
        self.livros.append(livro)

    def exibir_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            for livro in self.livros:
                print(livro.informacoes())

    def buscar_livro(self,titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                print(livro.informacoes())
                return
        print("Livro não encontrado.")
    
# Testandoas classes
livro1 = Livro("O senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("Dom Casmurro", "Machado de Assis", 1899)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

print("Livros na biblioteca: ")
biblioteca.exibir_livros()