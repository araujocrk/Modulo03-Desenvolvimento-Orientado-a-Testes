import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def maiorElementoESuaPosicao(lista):
    maior = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i + 1
    return f'Maior número: {maior}\nPosição: {posicao}'

def menorElementoESuaPosicao(lista):
    menor = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicao = i + 1
    return f'Menor número: {menor}\nPosição: {posicao}'

def main():
# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.
    qtd = 15
    lista15 = []
    preencherListaFloat(qtd, lista15)
    print(maiorElementoESuaPosicao(lista15))
    print(menorElementoESuaPosicao(lista15))
                    
if __name__ == '__main__':
    main()
