import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def intercalarListas(l1, l2):
    if not all(isinstance(i, (int, float)) for i in l1) or not all(isinstance(ii, (int, float)) for ii in l2) or len(l1) == 0 or len(l2) == 0 or len(l1) < len(l2):
        return Exception
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    return l3

def main():
# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
# elementos deste em uma outra lista de 20 elementos.
    l1 = []
    l2 = []
    l3 = []
    preencherListaFloat(10, l1)
    preencherListaFloat(10, l2)
    intercalarListas(l1, l2, l3)
       
if __name__ == '__main__':
    main()
