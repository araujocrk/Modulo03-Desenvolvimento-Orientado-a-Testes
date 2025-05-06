from q1 import qtdPares, listaPares, qtdImpares, listaImpares

def test_qtdPares():
    assert qtdPares([]) == 0
    assert qtdPares([1, 2]) == 1
    assert qtdPares([1, 2, 3, 4, 5, 6]) == 3
    assert qtdPares([-1, -2, -3, -4, -5, -6]) == 3
    assert qtdPares(['a', 2, 'c']) == Exception
    assert qtdPares([0.5, 1, 1.5, 2]) == Exception

def test_listaPares():
    assert listaPares([]) == []
    assert listaPares([1, 2]) == [2]
    assert listaPares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert listaPares([-1, -2, -3, -4, -5, -6]) == [-2, -4, -6]
    assert listaPares(['a', 2, 'c']) == Exception
    assert listaPares([0.5, 1, 1.5, 2]) == Exception

def test_qtdImpares():
    assert qtdImpares([]) == 0
    assert qtdImpares([1, 2]) == 1
    assert qtdImpares([1, 2, 3, 4, 5, 6]) == 3
    assert qtdImpares([-1, -2, -3, -4, -5, -6]) == 3
    assert qtdImpares(['a', 2, 'c']) == Exception
    assert qtdImpares([0.5, 1, 1.5, 2]) == Exception

def test_listaImpares():
    assert listaImpares([]) == []
    assert listaImpares([1, 2]) == [1]
    assert listaImpares([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert listaImpares([-1, -2, -3, -4, -5, -6]) == [-1, -3, -5]
    assert listaImpares(['a', 2, 'c']) == Exception
    assert listaImpares([0.5, 1, 1.5, 2]) == Exception