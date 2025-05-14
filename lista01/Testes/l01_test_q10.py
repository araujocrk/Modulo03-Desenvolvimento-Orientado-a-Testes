def Max(n1, n2, n3, n4):
    if not all(isinstance(x, int) for x in [n1, n2, n3, n4]):
        return Exception
    maior = 0
    if n1 >= n2 and n1 >= n3 and n1 >= n4:
        maior = n1
    elif n2 >= n1 and n2 >= n3 and n2 >= n4:
        maior = n2 
    elif n3 >= n1 and n3 >= n2 and n3 >= n4:
        maior = n3
    else:
        maior = n4
    return maior

def main():
    
    assert Max(1, 2, 3, 4) == 4
    assert Max(10, 5, 5, 5) == 10
    assert Max(-1, -2, -3, -4) == -1
    assert Max(5, 5, 5, 5) == 5
    assert Max(1, "a", 3, 4) == Exception
    print('Testes passados com sucesso!')

if __name__ == '__main__':
    main()
