def somaIntervalo(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma
        
def main():
# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma. 
    while True:
        try:
            n1 = int(input('Digite o primeiro número inteiro: '))
            break
        except:
            print('Primeiro número inválido. Tente novamente.')
    
    while True:
        try:
            n2 = int(input('Digite o segundo número inteiro: '))
            if n2 > n1:
                print(f'A soma do intervalo de [{n1},{n2}] é {somaIntervalo(n1, n2)}')
                break
            else:
                print('Erro! O segundo número deve ser maior que o primeiro.')
        except:
            print('Segundo número inválido. Tente novamente.')
    
if __name__ == '__main__':
    main()