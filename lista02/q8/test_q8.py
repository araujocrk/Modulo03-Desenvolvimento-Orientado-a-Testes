from q8 import qtdDeA

def test_qtdDeA():
    assert qtdDeA([]) == 0
    assert qtdDeA(['a', 'b', 'c']) == 0
    assert qtdDeA(['A']) == 1
    assert qtdDeA(['a', 'b', 'c', 'A', 'B', 'A', 'c']) == 2
    assert qtdDeA([1, 2, 'A']) == Exception
    assert qtdDeA([1.5, 2.5, 'c', 'A']) == Exception
    