import random

def preencherListaInt(qtd, lista):
    if not isinstance(qtd, int) or all(isinstance(i, int) for i in lista):
        return Exception
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    return lista

def qtdPares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    qtd = 0
    for i in lista:
        if i % 2 == 0:
            qtd += 1
    return qtd

def listaPares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

def qtdImpares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    qtd = 0
    for i in lista:
        if i % 2 != 0:
            qtd += 1
    return qtd

def listaImpares(lista):
    if not all(isinstance(i, int) for i in lista):
        return Exception
    impares = []
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
    return impares

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
