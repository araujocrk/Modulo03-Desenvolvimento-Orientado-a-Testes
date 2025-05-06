from q5 import intercalarListas

def test_intercalarListas():
    assert intercalarListas([1], [2]) == [1, 2]
    assert intercalarListas([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert intercalarListas([1.5, 2.5, 3.5], [2, 3, 4]) == [1.5, 2, 2.5, 3, 3.5, 4]
    assert intercalarListas([], []) == Exception
    assert intercalarListas([], [1, 2, 3]) == Exception
    assert intercalarListas([1, 2, 3], []) == Exception 
    assert intercalarListas(['a', 2, 'c'], [1, 2, 3]) == Exception
    assert intercalarListas([1, 2, 3], ['a', 2, 'c']) == Exception
    assert intercalarListas([1, 2], [3, 4, 5]) == Exception