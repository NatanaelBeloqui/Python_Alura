from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # Aqui diz que a classe prato herda da classe ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)