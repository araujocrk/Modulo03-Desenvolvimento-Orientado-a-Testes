import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def qtdPares(lista):
    qtd = 0
    for i in lista:
        if i % 2 == 0:
            qtd += 1
    return f'Quantidade de números pares: {qtd}'

def listaPares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    print(f'Lista de números pares: {pares}')

def qtdImpares(lista):
    qtd = 0
    for i in lista:
        if i % 2 != 0:
            qtd += 1
    return f'Quantidade de números ímpares: {qtd}'

def listaImpares(lista):
    impares = []
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
    print(f'Lista de números ímpares: {impares}')

def main():
# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.

    qtd = 100
    lista = []
    preencherListaInt(qtd, lista)
    print(qtdPares(lista))
    listaPares(lista)
    print(qtdImpares(lista))
    listaImpares(lista)
    
if __name__ == '__main__':
    main()
