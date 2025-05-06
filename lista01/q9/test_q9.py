from q9 import somaIntervalo

def test_somaIntervalo():
    assert somaIntervalo(1, 5) == 15
    assert somaIntervalo(0, 0) == 0
    assert somaIntervalo(3, 3) == 3
    assert somaIntervalo(5, 1) == Exception
    assert somaIntervalo("a", 5) == Exception
    print("Todos os testes para q9 passaram com sucesso!")
