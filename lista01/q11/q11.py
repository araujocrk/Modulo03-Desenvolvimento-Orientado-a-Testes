def divisores(n):
    if not isinstance(n, int) or n <= 0:
        return Exception
    numDivisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            numDivisores += 1
    return numDivisores

def main():
# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
    while True:
        try:
            n = int(input('Digite um número inteiro e positivo: '))
            if n > 0:
                print(f'O número de divisores de {n} é {divisores(n)}')
                break
            else:
                print('Número inválido. O número deve ser maior que 0!')
        except:
            print('Número inválido. Tente novamente!')
    
if __name__ == '__main__':
    main()