import random
def calcularFaturamento(qtd, preco):
    faturamento = []
    for i in range(len(qtd)):
        faturamento.append(round(qtd[i] * preco[i], 2))
    return faturamento

def calcularFaturamentoTotal(qtd, preco):
    faturamentoTotal = 0
    faturamento = calcularFaturamento(qtd, preco)
    for i in faturamento:
        faturamentoTotal += i
    return faturamentoTotal

def calcularMediaFaturamento(qtd, preco):
    faturamentoTotal = calcularFaturamentoTotal(qtd, preco)
    return faturamentoTotal / len(qtd)

def abaixoDaMedia(qtd, preco):
    qtdAbaixo = 0
    media = calcularMediaFaturamento(qtd, preco)
    faturamento = calcularFaturamento(qtd, preco)
    for i in faturamento:
        if i < media:
            qtdAbaixo += 1
    return qtdAbaixo

def main():
# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.
    # qtd = [10, 5, 3, 8, 12, 7, 20, 15, 9, 4, 6, 18, 10, 14, 11, 13, 16, 19, 2, 17]
    # preco = [15.99, 25.50, 7.30, 10.00, 45.75, 30.40, 12.99, 8.50, 22.00, 5.99, 17.25, 13.60, 9.99, 19.99, 8.75, 18.40, 23.60, 11.10, 14.50, 27.30]
    qtd, preco = [], []
    for i in range(20):
        qtd.append(random.randint(1, 20))
        preco.append(round(random.uniform(5.00, 50.00), 2))
    
    print(calcularFaturamento(qtd, preco))
    print(calcularFaturamentoTotal(qtd, preco))
    print(calcularMediaFaturamento(qtd, preco))
    print(abaixoDaMedia(qtd, preco))
                    
if __name__ == '__main__':
    main()