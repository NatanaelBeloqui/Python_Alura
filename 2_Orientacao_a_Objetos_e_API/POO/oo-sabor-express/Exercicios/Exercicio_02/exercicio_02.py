class musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
musica1 = musica('Vai Vai', 'Jota', 180)
musica2 = musica('Pão de ló', 'Pepe', 60)
musica3 = musica('Fazendinha', 'BRKsEDU', 300)