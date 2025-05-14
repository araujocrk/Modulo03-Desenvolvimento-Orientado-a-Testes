def calcularS(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return round(s, 2)

def main():

    assert calcularS(1) == 1.00
    assert calcularS(2) == 1.5
    assert calcularS(3) == 1.83
    assert calcularS(0) == Exception
    assert calcularS("a") == Exception
    print('Testes passados com sucesso!')
    
if __name__ == '__main__':
    main()