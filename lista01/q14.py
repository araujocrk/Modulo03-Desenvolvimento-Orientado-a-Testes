from q7 import calcularFatorial
def calcularS(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / calcularFatorial(i)
    return s
def main():
# 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + ½! + 1/3! + 1 /N!
    while True:
        try:
            n = int(input('Digite um número inteiro e positivo: '))
            if n > 0:
                print(f'O resultado da expressão S é {calcularS(n):.2f}')
                break
            else:
                print('Número inválido. O número deve ser maior que 0!')
        except:
            print('Número inválido. Tente novamente!')
    
if __name__ == '__main__':
    main()