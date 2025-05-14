import random
def lancarDado(qtdLancamentos, resultados):
    for i in range(qtdLancamentos):
        x = random.randint(1, 6)
        print('Lançando o dado...')
        print(f'Lançamento {i + 1}: {x}')
        resultados.append(x)

def verificarFace(resultados):
    contagem = {i: 0 for i in range(1, 7)}
    for x in resultados:
        if x in contagem:
            contagem[x] += 1
    return contagem
    
def main():

    assert verificarFace([1, 2, 3, 4, 5, 6]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
    assert verificarFace([1, 1, 1, 1]) == {1: 4, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    assert verificarFace([]) == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    assert verificarFace([6, 6, 6, 3, 2, 2]) == {1: 0, 2: 2, 3: 1, 4: 0, 5: 0, 6: 3}
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()
