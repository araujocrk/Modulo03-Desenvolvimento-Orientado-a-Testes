def calcularFatorial(fatorial):
    if isinstance(fatorial, (str, float)) or fatorial < 0:
        return Exception
    resultado = 1

    for i in range(1, fatorial + 1):
        resultado *= i
    return resultado

def main():

    assert calcularFatorial(0) == 1  # valor limítrofe
    assert calcularFatorial(1) == 1
    assert calcularFatorial(5) == 120
    assert calcularFatorial(-1) == Exception  # valor inválido
    assert calcularFatorial(3.5) == Exception  # tipo inválido
    assert calcularFatorial("a") == Exception  # tipo inválido
    print('Testes passados com sucesso!')
            
if __name__ == '__main__':
    main()