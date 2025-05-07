from q7 import verificarValorEmLista, verificarValorEmLista2

def test_verificarValorEmLista():
    assert verificarValorEmLista([1], 1) == True
    assert verificarValorEmLista([1, 2, 3, 4], 1) == True
    assert verificarValorEmLista([1.5, 2, 3.5, 4], 3.5) == True
    assert verificarValorEmLista([], 1) == Exception
    assert verificarValorEmLista(['a', 2, 'c'], 'c') == Exception
    