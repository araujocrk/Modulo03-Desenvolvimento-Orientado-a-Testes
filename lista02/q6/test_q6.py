from q6 import calcularFaturamento, calcularFaturamentoTotal, calcularMediaFaturamento, abaixoDaMedia

def test_calcularFaturamento():
    assert calcularFaturamento([15, 19, 18, 3], [31.33, 32.98, 36.63, 14.58]) == [469.95, 626.62, 659.34, 43.74]
    assert calcularFaturamento([0, 0, 0, 0], [0, 0, 0, 0]) == [0, 0, 0, 0]
    assert calcularFaturamento([1.5], [3]) == [4.5]
    assert calcularFaturamento([1], [3.5]) == [3.5]
    assert calcularFaturamento([1], [3.5, 4.5]) == Exception
    assert calcularFaturamento([1, 2], [1]) == Exception
    assert calcularFaturamento([], []) == Exception
    assert calcularFaturamento([], [1, 2, 3]) == Exception
    assert calcularFaturamento([1, 2, 3], []) == Exception
    assert calcularFaturamento(['a', 2, 'c'], [1, 2, 3]) == Exception
    assert calcularFaturamento([1, 2, 3], ['a', 2, 'c']) == Exception
    
def test_calcularFaturamentoTotal():
    assert calcularFaturamentoTotal([15, 19, 18, 3], [31.33, 32.98, 36.63, 14.58]) == 1799.65
    assert calcularFaturamentoTotal([0, 0, 0, 0], [0, 0, 0, 0]) == 0
    assert calcularFaturamentoTotal([1.5], [3]) == 4.5
    assert calcularFaturamentoTotal([1], [3.5]) == 3.5
    assert calcularFaturamentoTotal([1], [3.5, 4.5]) == Exception
    assert calcularFaturamentoTotal([1, 2], [1]) == Exception
    assert calcularFaturamentoTotal([], []) == Exception
    assert calcularFaturamentoTotal([], [1, 2, 3]) == Exception
    assert calcularFaturamentoTotal([1, 2, 3], []) == Exception
    assert calcularFaturamentoTotal(['a', 2, 'c'], [1, 2, 3]) == Exception
    
def test_calcularMediaFaturamento():
    assert calcularMediaFaturamento([15, 19, 18, 3], [31.33, 32.98, 36.63, 14.58]) == 449.91
    assert calcularMediaFaturamento([0, 0, 0, 0], [0, 0, 0, 0]) == 0
    assert calcularMediaFaturamento([1.5], [3]) == 4.5
    assert calcularMediaFaturamento([1], [3.5]) == 3.5
    assert calcularMediaFaturamento([1], [3.5, 4.5]) == Exception
    assert calcularMediaFaturamento([1, 2], [1]) == Exception
    assert calcularMediaFaturamento([], []) == Exception
    assert calcularMediaFaturamento([], [1, 2, 3]) == Exception
    assert calcularMediaFaturamento([1, 2, 3], []) == Exception
    assert calcularMediaFaturamento(['a', 2, 'c'], [1, 2, 3]) == Exception
    
def test_abaixoDaMedia():
    assert abaixoDaMedia([15, 19, 18, 3], [31.33, 32.98, 36.63, 14.58]) == 1
    assert abaixoDaMedia([0, 0, 0, 0], [0, 0, 0, 0]) == 0
    assert abaixoDaMedia([1.5], [3]) == 0
    assert abaixoDaMedia([1], [3.5]) == 0
    assert abaixoDaMedia([1], [3.5, 4.5]) == Exception
    assert abaixoDaMedia([1, 2], [1]) == Exception
    assert abaixoDaMedia([], []) == Exception
    assert abaixoDaMedia([], [1, 2, 3]) == Exception
    assert abaixoDaMedia([1, 2, 3], []) == Exception
    assert abaixoDaMedia(['a', 2, 'c'], [1, 2, 3]) == Exception