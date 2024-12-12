# livro.py

class Livro:
    livros = []  # Lista para armazenar todos os livros criados

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)  # Adiciona o livro criado à lista global de livros

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

    def emprestar(self):
        """Marca o livro como indisponível."""
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        """Retorna uma lista de livros disponíveis publicados em um ano específico."""
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]