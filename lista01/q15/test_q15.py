from q15 import calcularS

def test_calcularS():
    assert calcularS(1) == 0.5
    assert calcularS(2) == 1.5
    assert calcularS(3) == 3.17
    assert calcularS(0) == Exception
    assert calcularS("a") == Exception
    print("Todos os testes para q15 passaram com sucesso!")
