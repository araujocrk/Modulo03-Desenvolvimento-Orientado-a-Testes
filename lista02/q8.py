import random
import string

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
    # lista = random.choices(string.ascii_letters, k=20)
    # lista += ['A', 'A', 'A']
    # random.shuffle(lista)
    lista = []
    contador = 1
    letras = list(string.ascii_letters + 'ç' + 'Ç')
    while contador <= 10:
        try:
            letra = input(f'Digite a {contador}ª letra para adicionar na lista: ')
            if letra in letras:
                lista.append(letra)
                contador += 1
            else:
                print('Você não digitou uma letra. Tente novamente!')
        except:
            print('Erro. Tente novamente!')
    print(f'Lista: {lista}')
    print(f'Quantidade de A: {qtdDeA(lista)}')
                    
if __name__ == '__main__':
    main()