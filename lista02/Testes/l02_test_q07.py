import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def verificarValorEmLista(lista, valor):
    if not all(isinstance(i, (int, float)) for i in lista) or not isinstance(valor, (int, float)) or len(lista) <= 0:
        return Exception
    if valor in lista:
        return True
    else:
        return False
    
def verificarValorEmLista2(lista, valor):
    resultado = 'Valor ainda não está dentro da lista.'
    for i in lista:
        if valor == i:
            resultado = 'Valor já está dentro da lista'
    return resultado
        
def main():

    assert verificarValorEmLista([1], 1) == True
    assert verificarValorEmLista([1, 2, 3, 4], 1) == True
    assert verificarValorEmLista([1.5, 2, 3.5, 4], 3.5) == True
    assert verificarValorEmLista([], 1) == Exception
    assert verificarValorEmLista(['a', 2, 'c'], 'c') == Exception
    print('Testes passados com sucesso!')
           
if __name__ == '__main__':
    main()