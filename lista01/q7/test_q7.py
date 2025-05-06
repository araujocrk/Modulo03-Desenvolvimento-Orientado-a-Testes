from q7 import calcularFatorial

def test_calcularFatorial():
    assert calcularFatorial(0) == 1  # valor limítrofe
    assert calcularFatorial(1) == 1
    assert calcularFatorial(5) == 120
    assert calcularFatorial(-1) == Exception  # valor inválido
    assert calcularFatorial(3.5) == Exception  # tipo inválido
    assert calcularFatorial("a") == Exception  # tipo inválido
    print("Todos os testes para q7 passaram com sucesso!")
