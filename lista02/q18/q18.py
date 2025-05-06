import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    print(f'Lista X: {lista}')
    
def preencherListaR(x, r):
    for i in range(len(x)):
        if x[i] < 0:
            r.append(x[i])
    return r

def main():
# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
    x = []
    r = []
    preencherListaInt(10, x)
    print(f'Lista R: {preencherListaR(x, r)}')
    
if __name__ == '__main__':
    main()