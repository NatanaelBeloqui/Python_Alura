def exercicio(numero):
    print()
    print(numero)
    print()

exercicio('Exercício 1')
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nomes = ('Arthur', 'Eduardo', 'Ísis', 'João')
anos = (2005, 2024)

exercicio('Exercício 2')
for numero in numeros:
    print(numero)

exercicio('Exercício 3')
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

exercicio('Exercício 4')
for i in range(10, 0, -1):
    print(i)

# No range(10, 0, -1), o número 0 é o limite final da sequência, mas ele não será incluído no loop. Aqui está o significado de cada argumento:
# 10: Esse é o ponto inicial da sequência, ou seja, o loop começa em 10.
# 0: Esse é o ponto final exclusivo; o loop para antes de chegar a esse valor. Ou seja, ele vai de 10 até 1, mas sem incluir o 0.
# -1: Esse é o passo do range, indicando que estamos diminuindo de 1 em cada iteração (movendo-se para trás).
# Assim, range(10, 0, -1) gera os números 10, 9, 8, 7, ..., 1.

exercicio('Exercício 5')
numero = int(input('Digite um número: '))
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')

exercicio('Exercício 6')
soma = 0
try:
    for i in numeros:
        soma += i
    print(f'Soma dos elementos: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

exercicio('Exercício 7')
soma = 0
try:
    for numero in numeros:
        soma += numero
    media = soma/len(numeros) # O len retorna o tamanho da lista, ou seja, o número de elementos que ela tem.
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")