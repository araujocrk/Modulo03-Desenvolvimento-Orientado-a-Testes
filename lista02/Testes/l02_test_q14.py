import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')
    
def trocarNegativosPorZero(c):
    if not all(isinstance(i, int) for i in c) or len(c) == 0:
        return Exception
    for i in range(len(c)):
        if c[i] < 0:
            c[i] = 0
    return c
def main():
    
    assert trocarNegativosPorZero([-1, 2, -3, 4, -5]) == [0, 2, 0, 4, 0]
    assert trocarNegativosPorZero([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert trocarNegativosPorZero([-1, -2, -3, -4, -5]) == [0, 0, 0, 0, 0]
    assert trocarNegativosPorZero([]) == Exception
    assert trocarNegativosPorZero(['a', 'b', 'c', 'd', 'e']) == Exception
    assert trocarNegativosPorZero([1.5, 2.5, 3.5, 4.5, 5.5]) == Exception
    
if __name__ == '__main__':
    main()