from veiculo import Carro

carro_01 = Carro('Honda', 'Civic', 'Preto')
carro_02 = Carro('Fiat', 'Uno', 'Branco')
carro_03 = Carro('Ford', 'Mustang', 'Vermelho')

print(carro_01.marca, carro_01.modelo, carro_01.cor)
print(carro_02.marca, carro_02.modelo, carro_02.cor)
print(carro_03.marca, carro_03.modelo, carro_03.cor)

carro_01.ligar()
carro_02.ligar()
carro_03.ligar()