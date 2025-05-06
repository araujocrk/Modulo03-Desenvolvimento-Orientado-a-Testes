from q12 import somatorio

def test_somatorio():
    assert somatorio(1) == 1
    assert somatorio(5) == 15
    assert somatorio(10) == 55
    assert somatorio(0) == Exception
    assert somatorio("a") == Exception
    print("Todos os testes para q12 passaram com sucesso!")
