def divisores(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    numDivisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            numDivisores += 1
    return numDivisores

def main():

    assert divisores(1) == 1
    assert divisores(6) == 4
    assert divisores(10) == 4
    assert divisores(-1) == Exception
    assert divisores("a") == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()