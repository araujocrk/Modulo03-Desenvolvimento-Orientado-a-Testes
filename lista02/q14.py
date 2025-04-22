import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')
    
def trocarNegativosPorZero(c):
    for i in range(len(c)):
        if c[i] < 0:
            c[i] = 0
    return f'Lista modificada: {c}'
def main():
# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.
    c = []
    preencherListaInt(10, c)
    print(trocarNegativosPorZero(c))
    
if __name__ == '__main__':
    main()