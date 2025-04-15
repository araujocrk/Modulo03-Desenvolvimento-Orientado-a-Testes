import random
import string

def preencherListaStr(qtd, lista):
    for i in range(qtd):
        lista.append(random.choice(string.ascii_letters))
    print('Lista preenchida com sucesso!')

def qtdDeA(lista):
    contador = 0
    for l in lista:
        if l == 'A':
            contador += 1
    return contador

def main():
# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.
    lista = []
    while True:
        try:
            qtd = int(input('Digite a quantidade de letras que deseja: '))
            break
        except:
            print('Quantidade de letras inválida')
    preencherListaStr(qtd, lista)
    lista.append('A')
    print(f'Lista: {lista}')
    print(f'Quantidade de A: {qtdDeA(lista)}')
                    
if __name__ == '__main__':
    main()