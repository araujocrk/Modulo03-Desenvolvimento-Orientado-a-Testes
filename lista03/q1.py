import random

def preencherListaInt(qtd):
    lista = []
    for i in range(qtd):
        lista.append(random.randint(-10, 10))
    return lista
    
def eliminarRepeticoes(lista):
    listaSemRepeticao = []
    for i in lista:
        if i not in listaSemRepeticao:
            listaSemRepeticao.append(i)
    return listaSemRepeticao

def main():
# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

    assert len(preencherListaInt(5)) == 5
    lista = preencherListaInt(100)
    assert all(-10 <= i <= 10 for i in lista)
    assert eliminarRepeticoes([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]
    assert eliminarRepeticoes([]) == []
    assert eliminarRepeticoes([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    print('Testes passados com sucesso!')
if __name__ == '__main__':
    main()