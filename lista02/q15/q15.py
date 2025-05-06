import random

def preencherListaInt(qtd, lista):
    for i in range(qtd):
        lista.append(random.randint(-100, 100))
    print('Lista preenchida com sucesso!')
    return lista
    
def inverterLista(lista):
    listaInvertida = []
    for i in lista:
        listaInvertida.insert(0, i)
    return f'Lista invertida: {listaInvertida}'

def main():
# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
# por diante. Escrever todo a lista D e todo a lista E.
    d = []
    preencherListaInt(10, d)
    print(d)
    print(inverterLista(d))
    
if __name__ == '__main__':
    main()