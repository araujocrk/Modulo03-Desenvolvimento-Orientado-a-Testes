import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(1, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def preencherListaY(x, y):
    if not all(isinstance(i, int) for i in x) or len(x) == 0 or len(y) > 0:
        return Exception
    if not all(i > 0 for i in x):
        return Exception
    for i in range(len(x)):
        if i % 2 == 0:
            y.append(x[i] / 2)
        else:
            y.append(x[i] * 3)
    return y
def main():

    assert preencherListaY([1], []) == [0.5]
    assert preencherListaY([1, 2], []) == [0.5, 6]
    assert preencherListaY([1, 2, 3], []) == [0.5, 6, 1.5]
    assert preencherListaY([], []) == Exception
    assert preencherListaY([1], [1]) == Exception
    assert preencherListaY([1, -2], []) == Exception
    assert preencherListaY([1.5, 2.5], []) == Exception
    assert preencherListaY([1, 2, 'c'], []) == Exception
    print('Testes passados com sucesso!')
    
    
if __name__ == '__main__':
    main()