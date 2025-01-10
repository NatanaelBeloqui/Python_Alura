class Carro:
    def __init__(self, ano,modelo, cor):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor

    def __str__(self):
        return f'Ano: {self.ano} | Modelo: {self.modelo} | Cor: {self.cor}'

carro = Carro(2022, 'Gol', 'Preto')

class Restaurante:
    def __init__(self, nome, categoria, avaliacao, endereco):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.avaliacao = avaliacao
        self.endereco = endereco

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Avaliacao: {self.avaliacao} | Endereco: {self.endereco}'


restaurante_praca = Restaurante('Praça', 'Gourmet', 5, 'Av. Brasil, 1000')

print(restaurante_praca)

class Cliente:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f'Nome: {self.nome} | Endereco: {self.endereco} | Telefone: {self.telefone} | Email: {self.email}'


cliente_01 = Cliente('Natanael', 'Rua José Gomes de Freitas, 106', '47 9 9926-1533', 'natanael.beloqui@gmail.com')

cliente_02 = Cliente('BRKsEDU', 'Rua Visconde de Taunay, 730', '47 3026-6666', 'eduardo.neumann@gmail.com')

cliente_03 = Cliente('Livia', 'Rua dos Bobos, 0', '47 9 9999-9999', 'livia.beloqui@gmail.com')
