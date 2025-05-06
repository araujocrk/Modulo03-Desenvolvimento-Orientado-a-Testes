def calcularS(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return round(s, 2)

def main():
# 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.
    while True:
        try:
            n = int(input('Digite um número inteiro e positivo: '))
            if n > 0:
                print(f'O resultado da expressão S é {calcularS(n):.2f}')
                break
            else:
                print(' número inválido. O número deve ser maior que 0!')
        except:
            print(' número inválido. Tente novamente!')
    
if __name__ == '__main__':
    main()