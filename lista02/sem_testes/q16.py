import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(1, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def preencherListaY(x, y):
    for i in range(len(x)):
        if i % 2 == 0:
            y.append(x[i] / 2)
        else:
            y.append(x[i] * 3)
    return y
def main():
# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# Escrever as listas X e Y.
    x = []
    y = []
    preencherListaInt(10, x)
    print(f'Lista Y: {preencherListaY(x, y)}')
    
if __name__ == '__main__':
    main()