def calcularS(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    s = 0
    for t in range(1, n + 1):
        s += (((t**2) + 1) / (t + 3))
    return round(s, 2)

def main():

    assert calcularS(1) == 0.5
    assert calcularS(2) == 1.5
    assert calcularS(3) == 3.17
    assert calcularS(0) == Exception
    assert calcularS("a") == Exception
    print("Todos os testes para q15 passaram com sucesso!")
    
if __name__ == '__main__':
    main()