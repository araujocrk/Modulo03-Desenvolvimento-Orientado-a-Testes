import random

def preencherListaInt(qtd, lista):
    if not isinstance(qtd, int) or all(isinstance(i, int) for i in lista):
        return Exception
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    return lista

def qtdPares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    qtd = 0
    for i in lista:
        if i % 2 == 0:
            qtd += 1
    return qtd

def listaPares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

def qtdImpares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    qtd = 0
    for i in lista:
        if i % 2 != 0:
            qtd += 1
    return qtd

def listaImpares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    impares = []
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
    return impares

def main():

    assert qtdPares([]) == 0
    assert qtdPares([1, 2]) == 1
    assert qtdPares([1, 2, 3, 4, 5, 6]) == 3
    assert qtdPares([-1, -2, -3, -4, -5, -6]) == 3
    assert qtdPares(['a', 2, 'c']) == Exception
    assert qtdPares([0.5, 1, 1.5, 2]) == Exception
    
    assert listaPares([]) == []
    assert listaPares([1, 2]) == [2]
    assert listaPares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert listaPares([-1, -2, -3, -4, -5, -6]) == [-2, -4, -6]
    assert listaPares(['a', 2, 'c']) == Exception
    assert listaPares([0.5, 1, 1.5, 2]) == Exception
    
    assert qtdImpares([]) == 0
    assert qtdImpares([1, 2]) == 1
    assert qtdImpares([1, 2, 3, 4, 5, 6]) == 3
    assert qtdImpares([-1, -2, -3, -4, -5, -6]) == 3
    assert qtdImpares(['a', 2, 'c']) == Exception
    assert qtdImpares([0.5, 1, 1.5, 2]) == Exception
    
    assert listaImpares([]) == []
    assert listaImpares([1, 2]) == [1]
    assert listaImpares([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert listaImpares([-1, -2, -3, -4, -5, -6]) == [-1, -3, -5]
    assert listaImpares(['a', 2, 'c']) == Exception
    assert listaImpares([0.5, 1, 1.5, 2]) == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()
