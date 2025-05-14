import random
def calcularFaturamento(qtd, preco):
    if not all(isinstance(i, (int, float)) for i in qtd) or not all(isinstance(i, (int, float)) for i in preco) or len(qtd) == 0 or len(preco) == 0 or len(qtd) != len(preco):
        return Exception
    faturamento = []
    for i in range(len(qtd)):
        faturamento.append(round(qtd[i] * preco[i], 2))
    return faturamento

def calcularFaturamentoTotal(qtd, preco):
    if not all(isinstance(i, (int, float)) for i in qtd) or not all(isinstance(i, (int, float)) for i in preco) or len(qtd) == 0 or len(preco) == 0 or len(qtd) != len(preco):
        return Exception
    faturamentoTotal = 0
    faturamento = calcularFaturamento(qtd, preco)
    for i in faturamento:
        faturamentoTotal += i
    return round(faturamentoTotal, 2)

def calcularMediaFaturamento(qtd, preco):
    if not all(isinstance(i, (int, float)) for i in qtd) or not all(isinstance(i, (int, float)) for i in preco) or len(qtd) == 0 or len(preco) == 0 or len(qtd) != len(preco):
        return Exception
    faturamentoTotal = calcularFaturamentoTotal(qtd, preco)
    return round(faturamentoTotal / len(qtd), 2)

def abaixoDaMedia(qtd, preco):
    if not all(isinstance(i, (int, float)) for i in qtd) or not all(isinstance(i, (int, float)) for i in preco) or len(qtd) == 0 or len(preco) == 0 or len(qtd) != len(preco):
        return Exception
    qtdAbaixo = 0
    media = calcularMediaFaturamento(qtd, preco)
    faturamento = calcularFaturamento(qtd, preco)
    for i in faturamento:
        if i < media:
            qtdAbaixo += 1
    return qtdAbaixo

def main():

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
    print('Testes passados com sucesso!')
                    
if __name__ == '__main__':
    main()
