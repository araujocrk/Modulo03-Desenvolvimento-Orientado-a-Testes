import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def intercalarListas(l1, l2):
    if not all(isinstance(i, (int, float)) for i in l1) or not all(isinstance(ii, (int, float)) for ii in l2) or len(l1) == 0 or len(l2) == 0 or len(l1) < len(l2):
        return Exception
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    return l3

def main():

    assert intercalarListas([1], [2]) == [1, 2]
    assert intercalarListas([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert intercalarListas([1.5, 2.5, 3.5], [2, 3, 4]) == [1.5, 2, 2.5, 3, 3.5, 4]
    assert intercalarListas([], []) == Exception
    assert intercalarListas([], [1, 2, 3]) == Exception
    assert intercalarListas([1, 2, 3], []) == Exception 
    assert intercalarListas(['a', 2, 'c'], [1, 2, 3]) == Exception
    assert intercalarListas([1, 2, 3], ['a', 2, 'c']) == Exception
    assert intercalarListas([1, 2], [3, 4, 5]) == Exception
    print('Testes passados com sucesso!')
       
if __name__ == '__main__':
    main()
