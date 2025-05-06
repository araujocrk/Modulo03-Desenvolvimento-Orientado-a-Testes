from q7 import calcularFatorial
from q14 import calcularS

def test_calcularS():
    assert calcularS(1) == 1.00
    assert calcularS(2) == 1.5
    assert calcularS(3) == 1.67
    assert calcularS(0) == Exception
    assert calcularS("a") == Exception
    print("Todos os testes para q14 passaram com sucesso!")
