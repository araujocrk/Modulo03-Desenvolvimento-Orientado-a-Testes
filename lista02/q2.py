def qtdNegativos(l10):
    qtd = 0
    for n in l10:
        if n < 0:
            qtd += 1
    return qtd

def somaPositivos(l10):
    soma = 0
    for n in l10:
        if n > 0:
            soma += n
    return soma
def main():
# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.
    l10 = []
    for n in range(10):
        l10.append(float(input(f'Digite o {n+1} número: ')))
    print(f'Quantidade de números negativos: {qtdNegativos(l10)}\nSoma dos números positivos: {somaPositivos(l10)}')
    
if __name__ == '__main__':
    main()