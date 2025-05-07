from q4 import maiorElementoESuaPosicao, menorElementoESuaPosicao

def test_maiorElementoESuaPosicao():
    assert maiorElementoESuaPosicao([1]) == (1, 0)
    assert maiorElementoESuaPosicao([1, 2, 3, 4]) == (4, 3)
    assert maiorElementoESuaPosicao([1, 4, 3, 2]) == (4, 1)
    assert maiorElementoESuaPosicao([1, 1.5, 2.5, 0.5]) == (2.5, 2)
    assert maiorElementoESuaPosicao([]) == Exception
    assert maiorElementoESuaPosicao(['a', 2, 'c']) == Exception

def test_menorElementoESuaPosicao():
    assert menorElementoESuaPosicao([1]) == (1, 0)
    assert menorElementoESuaPosicao([1, 2, 3, 4]) == (1, 0)
    assert menorElementoESuaPosicao([4, 1, 3, 2]) == (1, 1)
    assert menorElementoESuaPosicao([1, -1.5, 2.5, 0.5]) == (-1.5, 1)
    assert menorElementoESuaPosicao([]) == Exception
    assert menorElementoESuaPosicao(['a', 2, 'c']) == Exception