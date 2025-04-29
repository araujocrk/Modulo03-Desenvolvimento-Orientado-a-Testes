def maiorSomaDeDoisSegmentos(lista):
    if len(lista) == 0:
        return Exception
    maior = lista[0] + lista[1]
    for i in range(1, len(lista)):
        if lista[i] + lista[i-1] >= maior:
            maior = lista[i] + lista[i-1]
    return maior

def main():
# 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# 4, 1] = 25
    assert maiorSomaDeDoisSegmentos([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 25
    assert maiorSomaDeDoisSegmentos([8, -3, 7, 10, 8, 2, -10, 5]) == 18
    assert maiorSomaDeDoisSegmentos([-10, -5, -1, -4, -7, -9]) == -5
    assert maiorSomaDeDoisSegmentos([]) == Exception
    print('Testes realizados com sucesso!')
if __name__ == '__main__':
    main()