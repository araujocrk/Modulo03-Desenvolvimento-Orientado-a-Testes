def inverterLista(lista):
    listaInvertida = []
    for i in lista:
        listaInvertida.insert(0, i)
    return listaInvertida

def main():
# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
# leitura.
    while True:
        try:
            qtdN = int(input('Digite a quantidade de números de uma sequência: '))
            listaN = list(range(qtdN))
            print(inverterLista(listaN))
            break
            # IA
            # print(listaN[::-1])
        except:
            print('Quantidade de números inválida')
    
if __name__ == '__main__':
    main()