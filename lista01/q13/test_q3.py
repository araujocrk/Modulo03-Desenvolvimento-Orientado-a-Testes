from q13 import calcularS

def test_calcularS():
    assert calcularS(1) == 1.00
    assert calcularS(2) == 1.5
    assert calcularS(3) == 1.83
    assert calcularS(0) == Exception
    assert calcularS("a") == Exception
    print("Todos os testes para q13 passaram com sucesso!")
