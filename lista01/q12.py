def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma
def main():
# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
    while True:
        try:
            n = int(input('Digite um número inteiro e positivo: '))
            if n > 0:
                print(f'O somatório de {n} é {somatorio(n)}')
                break
            else:
                print('Número inválido. O número deve ser maior que 0!')
        except:
            print('Número inválido. Tente novamente!')
    
if __name__ == '__main__':
    main()