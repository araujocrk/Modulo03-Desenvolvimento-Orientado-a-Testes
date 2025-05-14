import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')
    
def quantidadeOcorrencias(w, v):
    qtd = 0
    for i in range(len(w)):
        if w[i] == v:
            qtd += 1
    if qtd == 0:
        return False
    return qtd

def posicoesOcorrencias(w, v):
    posicoes = []
    for i in range(len(w)):
        if w[i] == v:
            posicoes.append(i)
    if len(posicoes) >= 1:
        return posicoes 
    return False

def main():

    assert quantidadeOcorrencias([1, 2, 3, 2, 4, 2], 2) == 3 
    assert quantidadeOcorrencias([5, 6, 7], 6) == 1
    assert quantidadeOcorrencias([8, 9, 10], 11) == False
    assert quantidadeOcorrencias([], 0) == False
    
    assert posicoesOcorrencias([1, 2, 3, 2, 4, 2], 2) == [1, 3, 5]
    assert posicoesOcorrencias([5, 6, 7], 6) == [1]
    assert posicoesOcorrencias([8, 9, 10], 11) == False
    assert posicoesOcorrencias([], 0) == False
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()