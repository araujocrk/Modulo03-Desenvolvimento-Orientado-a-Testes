def maiorSomaDeDoisSegmentos(lista):
    if len(lista) == 0:
        return Exception
    maior = lista[0] + lista[1]
    sequencia = 2
    while sequencia <= len(lista):
        for i in range((len(lista) - sequencia) + 1):
            soma = 0
            for j in range(i, i+sequencia):
                soma = soma + lista[j]
                if soma > maior:
                    maior = soma
        sequencia += 1
        return maior

def main():
# 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
# -6, 4, 1] = 34
    assert func(5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1) == 34

    assert func([]) == Exception
if __name__ == '__main__':
    main()