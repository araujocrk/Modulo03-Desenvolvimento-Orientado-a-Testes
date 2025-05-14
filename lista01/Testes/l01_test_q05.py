def pesoIdeal(altura, sexo):
    if isinstance(altura, str) or altura < 0.30 or altura > 2.80:
        return Exception
    if sexo == 1:
        return round((62.1 * altura) - 44.7, 2)
    elif sexo == 2:
        return round((72.7 * altura) - 58, 2)
    else:
        return Exception

def main():
    
    assert pesoIdeal(0.30, 1) == -26.07 # Testanto valor limítrofe.
    assert pesoIdeal(0.30, 2) == -36.19 # Testanto valor limítrofe.
    assert pesoIdeal(2.80, 1) == 129.18 # Testeando classe válida
    assert pesoIdeal(2.80, 2) == 145.56 # Testeando classe válida
    assert pesoIdeal('a', 1) == Exception # Testando classe inválida.
    assert pesoIdeal(2.80, 'b') == Exception # Testando classe inválida.
    assert pesoIdeal(-1, 1) == Exception # Testando classe inválida.
    assert pesoIdeal(2.80, -1) == Exception # Testando classe inválida.
    print('Testes passados com sucesso!')
            
if __name__ == '__main__':
    main()