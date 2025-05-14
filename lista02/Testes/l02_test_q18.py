import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista X: {lista}')
    
def preencherListaR(x):
    r = []
    for i in range(len(x)):
        if x[i] < 0:
            r.append(x[i])
    return r

def main():

    assert preencherListaR([1, -1, 2, -2, 3]) == [-1, -2]
    assert preencherListaR([1, 2, 3]) == []
    assert preencherListaR([-1, -2, -3]) == [-1, -2, -3]
    assert preencherListaR([]) == []
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()