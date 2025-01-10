# biblioteca.py
from livro import Livro

# Criando um livro
livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)

# Emprestando o livro
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

# Verificando disponibilidade de livros por ano
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}:")
for livro in livros_disponiveis_ano:
    print(livro)