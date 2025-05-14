import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def maiorElementoESuaPosicao(lista):
    if not all(isinstance(i, (int, float)) for i in lista) or len(lista) == 0:
        return Exception
    maior = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i
    return maior, posicao

def menorElementoESuaPosicao(lista):
    if not all(isinstance(i, (int, float)) for i in lista) or len(lista) == 0:
        return Exception
    menor = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicao = i
    return menor, posicao

def main():

    assert maiorElementoESuaPosicao([1]) == (1, 0)
    assert maiorElementoESuaPosicao([1, 2, 3, 4]) == (4, 3)
    assert maiorElementoESuaPosicao([1, 4, 3, 2]) == (4, 1)
    assert maiorElementoESuaPosicao([1, 1.5, 2.5, 0.5]) == (2.5, 2)
    assert maiorElementoESuaPosicao([]) == Exception
    assert maiorElementoESuaPosicao(['a', 2, 'c']) == Exception
    
    assert menorElementoESuaPosicao([1]) == (1, 0)
    assert menorElementoESuaPosicao([1, 2, 3, 4]) == (1, 0)
    assert menorElementoESuaPosicao([4, 1, 3, 2]) == (1, 1)
    assert menorElementoESuaPosicao([-1, 1.5, 2.5, 0.5]) == (-1, 0)
    assert menorElementoESuaPosicao([]) == Exception
    assert menorElementoESuaPosicao(['a', 2, 'c']) == Exception
    print('Testes passados com sucesso!')
                    
if __name__ == '__main__':
    main()