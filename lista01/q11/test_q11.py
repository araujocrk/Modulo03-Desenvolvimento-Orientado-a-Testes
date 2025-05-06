from q11 import divisores

def test_divisores():
    assert divisores(1) == 1
    assert divisores(6) == 4
    assert divisores(10) == 4
    assert divisores(-1) == Exception
    assert divisores("a") == Exception
    print("Todos os testes para q11 passaram com sucesso!")
