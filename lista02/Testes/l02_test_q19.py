import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    return lista

def preencherListaX(r, s):
    x = []
    if len(r) != 5 or len(s) != 10:
        return Exception
    x = r + s
    return x
def main():

    assert preencherListaX([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert preencherListaX([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == Exception
    assert preencherListaX([6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 2, 3, 4]) == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()