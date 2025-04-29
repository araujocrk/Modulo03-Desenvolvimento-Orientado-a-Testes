import random

def preencherListaInt(qtd):
    lista = []
    for i in range(qtd):
        lista.append(random.randint(-10, 10))
    return lista

def contaOcorrencias(lista):
    ocorrencias = {}
    for num in lista:
        if num in ocorrencias:
            ocorrencias[num] += 1
        else:
            ocorrencias[num] = 1
    return ocorrencias
def main():
    # 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
    # o número de vezes que cada número ocorre na sequência.
    
    assert contaOcorrencias([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert contaOcorrencias([1, 1, 2, 3, 4]) == {1: 2, 2: 1, 3: 1, 4: 1}
    assert contaOcorrencias([1, 1, 1, 2, 2]) == {1: 3, 2: 2}
    assert contaOcorrencias([1, 1, 1, 1, 2]) == {1: 4, 2: 1}
    assert contaOcorrencias([1, 1, 1, 1, 1]) == {1: 5}
    assert contaOcorrencias([]) == {}

    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()