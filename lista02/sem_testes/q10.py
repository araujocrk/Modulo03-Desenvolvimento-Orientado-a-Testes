import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def maiorElementoESuaPosicao(lista):
    maior = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i + 1
    return maior, posicao

def menorElementoESuaPosicao(lista):
    menor = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicao = i + 1
    return menor, posicao

def main():
# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.
    lista15 = []
    preencherListaInt(15, lista15)
    # contador = 1
    # while contador <= 15:
    #     try:
    #         n = int(input(f'Digite o {contador} número de 15: '))
    #         lista15.append(n)
    #         contador += 1
    #     except:
    #         print(f'Número {contador} inválido. Tente novamente')
    print(f'O maior elemento é {maiorElementoESuaPosicao(lista15)[0]} e sua posição é {maiorElementoESuaPosicao(lista15)[1]}') 
    print(f'O menor elemento é {menorElementoESuaPosicao(lista15)[0]} e sua posição é {menorElementoESuaPosicao(lista15)[1]}')
                    
if __name__ == '__main__':
    main()