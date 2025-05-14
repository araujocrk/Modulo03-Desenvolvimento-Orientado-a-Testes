import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    return lista
    
def inverterLista(lista):
    if not all(isinstance(i, (int, float)) for i in lista):
        return Exception
    listaInvertida = []
    for i in lista:
        listaInvertida.insert(0, i)
    return listaInvertida

def main():

    assert inverterLista([]) == []
    assert inverterLista([1]) == [1]
    assert inverterLista([1.5, 2.5, 3.5]) == [3.5, 2.5, 1.5]
    assert inverterLista([1, 2, 3]) == [3, 2, 1]
    assert inverterLista([-1, 2, 3]) == [3, 2, -1]
    assert inverterLista(['a', 2, 'c']) == Exception
    assert inverterLista([1, 1.5, 'c']) == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()