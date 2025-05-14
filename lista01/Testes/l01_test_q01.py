def par_impar(n):
    if isinstance(n, (float, str)):
        return Exception
    return n % 2 == 0

def main():
    assert par_impar(1) == False # Testando classe valor limítrofe.
    assert par_impar(2) == True # Testando classe par.
    assert par_impar(-3) == False # Testando classe impar.
    assert par_impar(3.5) == Exception # Testando valores inválidos ou improváveis.
    assert par_impar('a') == Exception # Testando valores inválidos ou improváveis.
    print('Testes passados com sucesso!')

if __name__ == '__main__':
    main()