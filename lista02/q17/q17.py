import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')
    
def quantidadeOcorrencias(w, v):
    qtd = 0
    for i in range(len(w)):
        if w[i] == v:
            qtd += 1
    if qtd == 0:
        return 'não aparece na lista'
    return f'aparece {qtd} vezes na lista'

def posicoesOcorrencias(w, v):
    posicoes = []
    for i in range(len(w)):
        if w[i] == v:
            posicoes.append(i)
    if len(posicoes) >= 1:
        return f'e suas posições são {posicoes}' 
    return ''

def main():
# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
# aparece.
# Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.
    w = []
    preencherListaInt(10, w)
    while True:
        try:
            v = int(input('Digite o número para verificação: '))
            break
        except:
            print('Valor inválido. Tente novamente!')
    print(f'O número {v} {quantidadeOcorrencias(w, v)} {posicoesOcorrencias(w, v)}')
    
if __name__ == '__main__':
    main()