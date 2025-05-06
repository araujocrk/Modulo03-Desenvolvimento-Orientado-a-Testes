from q2 import qtdNegativos, somaPositivos

def test_qtdNegativos():
    assert qtdNegativos([]) == 0
    assert qtdNegativos([1, 2]) == 0
    assert qtdNegativos([1, 2, 3, 4, 5, 6]) == 0
    assert qtdNegativos([-1]) == 1
    assert qtdNegativos([-1, -2, -3,- 4, -5, -6]) == 6
    assert qtdNegativos([1.5, 2, 2.5]) == 0
    assert qtdNegativos([-1.5, -1, -0.5, 0, 0.5, 1]) == 3
    assert qtdNegativos(['a', 2, 'c']) == Exception

def test_somaPositivos():
    assert somaPositivos([]) == 0
    assert somaPositivos([1, 2]) == 3
    assert somaPositivos([1, 2, 3, 4, 5, 6]) == 21
    assert somaPositivos([-1]) == 0
    assert somaPositivos([-1, -2, -3,- 4, -5, -6]) == 0
    assert somaPositivos([1.5, 2, 2.5]) == 6
    assert somaPositivos([-1.5, -1, -0.5, 0, 0.5, 1]) == 1.5
    assert somaPositivos(['a', 2, 'c']) == Exception