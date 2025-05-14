def area(r):
    if isinstance(r, str) or r <= 0:
        return Exception
    PI = 3.14
    return round(PI * (r ** 2), 2)

def perimetro(r):
    if isinstance(r, str) or r <= 0:
        return Exception
    PI = 3.14
    return round(PI * 2 * r, 2)

def main():
    
    assert area(1) == 3.14 # Testando valor limítrofe.
    assert area(2.5) == 19.62 # Testando float.
    assert area('a') == Exception # Testando valores inválidos ou improváveis.
    assert area(0) == Exception # Testando valores inválidos ou improváveis.
    assert area(-1) == Exception # Testando valores inválidos ou improváveis.
    print('Testes passados com sucesso!')
    
    assert perimetro(1) == 6.28 # Testando valor limítrofe.
    assert perimetro(2.5) == 15.70 # Testando float.
    assert perimetro('a') == Exception # Testando valores inválidos ou improváveis.
    assert perimetro(0) == Exception # Testando valores inválidos ou improváveis.
    assert perimetro(-1) == Exception # Testando valores inválidos ou improváveis.
    print('Testes passados com sucesso!')
         
if __name__ == '__main__':
    main()