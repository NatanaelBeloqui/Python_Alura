x = float(input('Insira o valor de X: '))
y = float(input('Insira o valor de Y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('O ponto está localizado no eixo ou origem.')