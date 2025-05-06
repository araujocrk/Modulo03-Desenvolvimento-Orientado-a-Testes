import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')
    
def inverterLista(lista):
    y = []
    for i in lista:
        y.insert(0, i)
    return y

def main():
# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

    x = []
    preencherListaFloat(5, x)
    print(inverterLista(x))

if __name__ == '__main__':
    main()