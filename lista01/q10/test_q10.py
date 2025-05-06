from q10 import Max

def test_Max():
    assert Max(1, 2, 3, 4) == 4
    assert Max(10, 5, 5, 5) == 10
    assert Max(-1, -2, -3, -4) == -1
    assert Max(5, 5, 5, 5) == 5
    assert Max(1, "a", 3, 4) == Exception
    print("Todos os testes para q10 passaram com sucesso!")
