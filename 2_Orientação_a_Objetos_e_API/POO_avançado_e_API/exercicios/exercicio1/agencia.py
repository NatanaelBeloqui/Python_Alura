from exercicio1.banco import Banco

class Agencia(Banco):
    def _init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return f'{self._nome} | {self._endereco} | {self._numero}'

agencia1 = Agencia('Bradesco', 'Av. Paulista', 1234)
print(agencia1)

# Importante: A herança em programação orientada a objetos proporciona a reutilização eficiente de código ao permitir que uma classe herde características e comportamentos de uma classe pai. Isso promove abstração, simplificando a representação hierárquica do domínio do problema.