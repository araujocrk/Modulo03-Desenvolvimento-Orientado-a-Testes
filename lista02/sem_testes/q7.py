import random

def preencherListaFloat(qtd, lista):
    for i in range(qtd):
        lista.append(round(random.uniform(-100, 100), 2))
    print('Lista preenchida com sucesso!')
    print(f'Lista: {lista}')

def verificarValorEmLista(lista, valor):
    if valor in lista:
        return 'Valor já está dentro da lista'
    else:
        return 'Valor ainda não está dentro da lista.'
    
def verificarValorEmLista2(lista, valor):
    resultado = 'Valor ainda não está dentro da lista.'
    for i in lista:
        if valor == i:
            resultado = 'Valor já está dentro da lista'
    return resultado
        
def main():
# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.
    l = []
    qtd = 10
    preencherListaFloat(qtd, l)
    
    while True:
        try:
            valor = float(input('Digite o número para verificação: '))
            print(verificarValorEmLista(l, valor))
            print(verificarValorEmLista2(l, valor))
            break
        except:
            print('Número inválido. Tente novamente.')
           
if __name__ == '__main__':
    main()