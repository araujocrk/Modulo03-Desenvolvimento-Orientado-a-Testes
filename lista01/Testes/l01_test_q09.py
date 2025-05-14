def somaIntervalo(n1, n2):
    if not all(isinstance(x, int) for x in [n1, n2]) or n1 > n2:
        return Exception
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma
        
def main():

    assert somaIntervalo(1, 5) == 15
    assert somaIntervalo(0, 0) == 0
    assert somaIntervalo(3, 3) == 3
    assert somaIntervalo(5, 1) == Exception
    assert somaIntervalo("a", 5) == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()