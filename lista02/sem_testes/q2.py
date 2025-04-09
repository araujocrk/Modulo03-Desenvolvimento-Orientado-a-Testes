import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def qtdNegativos(lista):
    qtd = 0
    for n in lista:
        if n < 0:
            qtd += 1
    return qtd

def somaPositivos(lista):
    soma = 0
    for n in lista:
        if n > 0:
            soma += n
    return f'{soma:.2f}'
def main():
# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.
    qtd = 10
    lista = []
    preencherListaFloat(qtd, lista)
    print(qtdNegativos(lista))
    print(somaPositivos(lista))

if __name__ == '__main__':
    main()
