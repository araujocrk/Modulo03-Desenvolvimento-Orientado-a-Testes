def calcularS(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    s = 0
    for t in range(1, n + 1):
        s += (((t**2) + 1) / (t + 3))
    return round(s, 2)

def main():
# 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
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