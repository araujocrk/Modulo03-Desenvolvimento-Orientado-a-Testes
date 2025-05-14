import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def qtdNegativos(lista):
    if not all(isinstance(i, (float, int)) for i in lista):
        return Exception
    qtd = 0
    for n in lista:
        if n < 0:
            qtd += 1
    return qtd

def somaPositivos(lista):
    if not all(isinstance(i, (float, int)) for i in lista):
        return Exception
    soma = 0
    for n in lista:
        if n > 0:
            soma += n
    return round(soma, 2)
def main():

    assert qtdNegativos([]) == 0
    assert qtdNegativos([1, 2]) == 0
    assert qtdNegativos([1, 2, 3, 4, 5, 6]) == 0
    assert qtdNegativos([-1]) == 1
    assert qtdNegativos([-1, -2, -3,- 4, -5, -6]) == 6
    assert qtdNegativos([1.5, 2, 2.5]) == 0
    assert qtdNegativos([-1.5, -1, -0.5, 0, 0.5, 1]) == 3
    assert qtdNegativos(['a', 2, 'c']) == Exception
    
    assert somaPositivos([]) == 0
    assert somaPositivos([1, 2]) == 3
    assert somaPositivos([1, 2, 3, 4, 5, 6]) == 21
    assert somaPositivos([-1]) == 0
    assert somaPositivos([-1, -2, -3,- 4, -5, -6]) == 0
    assert somaPositivos([1.5, 2, 2.5]) == 6
    assert somaPositivos([-1.5, -1, -0.5, 0, 0.5, 1]) == 1.5
    assert somaPositivos(['a', 2, 'c']) == Exception
    print('Testes passados com sucesso!')

if __name__ == '__main__':
    main()
