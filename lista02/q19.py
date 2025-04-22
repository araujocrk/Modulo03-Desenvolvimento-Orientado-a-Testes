import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    return lista

def preencherListaX(r, s, x):
    x = r + s
    return x
def main():
# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
# de S. Escrever a lista X.
    r = []
    s = []
    x = []
    print(f'Lista R: {preencherListaInt(5, r)}')
    print(f'Lista S: {preencherListaInt(10, s)}')
    print(f'Lista X: {preencherListaX(r, s, x)}')
    
if __name__ == '__main__':
    main()