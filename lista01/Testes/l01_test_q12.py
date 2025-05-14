def somatorio(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma
def main():

    assert somatorio(1) == 1
    assert somatorio(5) == 15
    assert somatorio(10) == 55
    assert somatorio(0) == Exception
    assert somatorio("a") == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()