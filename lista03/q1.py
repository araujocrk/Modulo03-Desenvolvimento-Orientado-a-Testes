import random

def preencherListaInt(qtd):
    if isinstance(qtd, (float, str)) or qtd == 0:
        return Exception
    lista = []
    for i in range(qtd):
        lista.append(random.randint(-10, 10))
    return lista
    
def eliminarRepeticoes(lista):
    if len(lista) == 0:
        return Exception
    listaSemRepeticao = []
    for i in lista:
        if isinstance(i, (float, str)):
            return Exception
        if i not in listaSemRepeticao:
            listaSemRepeticao.append(i)
    return listaSemRepeticao

def main():
# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

    assert len(preencherListaInt(5)) == 5 # Testanto se a lista é criada no tamanho correto.
    assert preencherListaInt(5.5) == Exception # Testando classe float.
    assert preencherListaInt('B') == Exception # Testando classe str.
    assert all(-10 <= i <= 10 for i in preencherListaInt(100)) # Testando se os valores da lista estão no intervalo de -10 a 10.
    assert eliminarRepeticoes([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3] # Testando classe int.
    assert eliminarRepeticoes([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5] # Testando classe int sem repetidos.
    assert eliminarRepeticoes([1.5, 2.5, 3, 4.5, 5]) == Exception # Testando classe float.
    assert eliminarRepeticoes([0, 'a', '2', 'c', '4']) == Exception # Testando classe str.
    assert eliminarRepeticoes([]) == Exception # Testando uma lista vazia
    print('Testes passados com sucesso!')
if __name__ == '__main__':
    main()
