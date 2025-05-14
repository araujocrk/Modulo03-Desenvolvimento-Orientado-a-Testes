import random
import string

def preencherListaStr(qtd, lista):
    for i in range(qtd):
        lista.append(random.choice(string.ascii_letters))
    print('Lista preenchida com sucesso!')

def qtdDeA(lista):
    if not all(isinstance (i, str) for i in lista):
        return Exception
    contador = 0
    for l in lista:
        if l == 'A':
            contador += 1
    return contador

def main():

    assert qtdDeA([]) == 0
    assert qtdDeA(['a', 'b', 'c']) == 0
    assert qtdDeA(['A']) == 1
    assert qtdDeA(['a', 'b', 'c', 'A', 'B', 'A', 'c']) == 2
    assert qtdDeA([1, 2, 'A']) == Exception
    assert qtdDeA([1.5, 2.5, 'c', 'A']) == Exception
    print('Testes passados com sucesso!')
                    
if __name__ == '__main__':
    main()