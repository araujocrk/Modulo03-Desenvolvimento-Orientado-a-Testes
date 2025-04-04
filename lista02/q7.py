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
    l10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while True:
        try:
            valor = int(input('Digite o número inteiro para verificação: '))
            print(verificarValorEmLista(l10, valor))
            print(verificarValorEmLista2(l10, valor))
            break
        except:
            print('Número inválido. Tente novamente.')
           
if __name__ == '__main__':
    main()