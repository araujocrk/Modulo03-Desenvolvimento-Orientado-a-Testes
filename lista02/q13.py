import random
def lancarDado(qtdLancamentos, resultados):
    for i in range(qtdLancamentos):
        x = random.randint(1, 6)
        print('Lançando o dado...')
        print(f'Lançamento {i + 1}: {x}')
        resultados.append(x)

def verificarFace(resultados):
    n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0
    for x in resultados:
        if x == 1:
            n1 += 1
        elif x == 2:
            n2 += 1
        elif x == 3:
            n3 += 1
        elif x == 4:
            n4 += 1
        elif x == 5:
            n5 += 1
        elif x == 6:
            n6 += 1
    return f'Faces: 1 - {n1} vezes; 2 - {n2} vezes; 3 - {n3} vezes; 4 - {n4} vezes; 5 - {n5} vezes; 6 - {n6} vezes;'
    

def main():
# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
# cada face. 
    resultados = []
    while True:
        try:
            n = int(input('Digite o número de lancamentos: '))
            if n > 0:
                break
            else:
                print('O número de lancamentos deve ser maior que 0! Tente novamente!') 
        except:
            print('O número de lancamentos deve ser um número inteiro! Tente novamente!')
    
    lancarDado(n, resultados)
    print(verificarFace(resultados))
    
if __name__ == '__main__':
    main()
