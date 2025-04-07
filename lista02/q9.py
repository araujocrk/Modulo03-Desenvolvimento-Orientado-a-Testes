def inverterLista(lista):
    y = []
    for i in lista:
        y.insert(0, i)
    return y

def main():
# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
    contador = 1
    x = []
    while contador <= 5:
        try:
            n = float(input(f'Digite o {contador}º número da lista: '))
            contador += 1
            x.append(n)
        except:
            print('Número inválido. Tente novamente!')
    print(inverterLista(x))

if __name__ == '__main__':
    main()