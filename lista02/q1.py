def qtdParesImpares(l100):
    pares = []
    impares = []
    for i in l100:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return len(pares), pares, len(impares), impares
def main():
# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.
    l100 = list(range(100))
    print(f'Quantidade de números pares: {qtdParesImpares(l100)[0]}\nNúmeros pares: {qtdParesImpares(l100)[1]}\nQuantidade de números ímpares: {qtdParesImpares(l100)[2]}\nNúmeros ímpares: {qtdParesImpares(l100)[3]}')
    
if __name__ == '__main__':
    main()