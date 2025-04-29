import random

def preencherListaInt(qtd):
    if isinstance(qtd, (float, str)) or qtd == 0:
        return Exception
    lista = []
    for i in range(qtd):
        lista.append(random.randint(-10, 10))
    return lista

def contaOcorrencias(lista):
    if len(lista) == 0:
        return Exception
    ocorrencias = {}
    for num in lista:
        if isinstance(num, (float, str)):
            return Exception
        if num in ocorrencias:
            ocorrencias[num] += 1
        else:
            ocorrencias[num] = 1
    return ocorrencias
def main():
    # 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
    # o número de vezes que cada número ocorre na sequência.
    
    assert len(preencherListaInt(5)) == 5 # Testanto se a lista é criada no tamanho correto.
    assert preencherListaInt(5.5) == Exception # Testando classe float.
    assert preencherListaInt('B') == Exception # Testando classe str.
    assert all(-10 <= i <= 10 for i in preencherListaInt(100)) # Testando se os valores da lista estão no intervalo de -10 a 10.

    assert contaOcorrencias([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1} # Testando classe int
    assert contaOcorrencias([1, 1, 2, 3, 4]) == {1: 2, 2: 1, 3: 1, 4: 1} # Testando classe int
    assert contaOcorrencias([1, 1, 1, 2, 2]) == {1: 3, 2: 2} # Testando classe int
    assert contaOcorrencias([1, 1, 1, 1, 2]) == {1: 4, 2: 1} # Testando classe int
    assert contaOcorrencias([1, 1, 1, 1, 1]) == {1: 5} # Testando classe int
    assert contaOcorrencias([]) == Exception # Testando lista vazia
    assert contaOcorrencias([1.5, 2.5, 3.5, 4.5, 5.5]) == Exception # Testando classe float
    assert contaOcorrencias(['a', 'b', 'c', 'd', 'e']) == Exception # Testando classe str
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()
