from q3 import inverterLista

def test_inverterLista():
    assert inverterLista([]) == []
    assert inverterLista([1]) == [1]
    assert inverterLista([1.5, 2.5, 3.5]) == [3.5, 2.5, 1.5]
    assert inverterLista([1, 2, 3]) == [3, 2, 1]
    assert inverterLista([-1, 2, 3]) == [3, 2, -1]
    assert inverterLista(['a', 2, 'c']) == Exception
    assert inverterLista([1, 1.5, 'c']) == Exception