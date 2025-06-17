# 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos anteriores da lista original. Ex: [1,2,3] =
# [1,3,6]

def listaCumulativa(listaOri):
    listaCumulativa = []
    for i in range(1, len(listaOri) + 1):
        soma = 0
        for j in range(0, i):
            soma += listaOri[j]
        listaCumulativa.append(soma)
    return listaCumulativa

def main():
    assert listaCumulativa([3, 5, 7, 4]) == [3, 8, 15, 19]
    print('Testes passados com sucesso!')

if __name__ == '__main__':
    main()