import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def inverterLista(lista):
    listaInvertida = []
    for i in lista:
        listaInvertida.insert(0, i)
    return f'Lista invertida: {listaInvertida}'

def main():
# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
# leitura.
    lista = []
    while True:
        try:
            qtd = int(input('Digite a quantidade números que deseja: '))
            break
            # IA
            # print(listaN[::-1])
        except:
            print('Quantidade de números inválida')
    preencherListaFloat(qtd, lista)
    print(inverterLista(lista))

if __name__ == '__main__':
    main()
