def Max(n1, n2, n3, n4):
    maior = 0
    if n1 >= n2 and n1 >= n3 and n1 >= n4:
        maior = n1
    elif n2 >= n1 and n2 >= n3 and n2 >= n4:
        maior = n2 
    elif n3 >= n1 and n3 >= n2 and n3 >= n4:
        maior = n3
    else:
        maior = n4
    return maior

def main():
# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada 4  números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b, c, d Para cada série lida imprime o maior dos quatro números usando a função
# Max.
    for i in range(4):
        for i in range(4):
            while True:
                try:
                    n1 = int(input('Digite o primeiro número inteiro: '))
                    break
                except:
                    print('Número inválido para n1. Tente novamente!')
                
            while True:
                try:
                    n2 = int(input('Digite o segundo número inteiro: '))
                    break
                except:
                    print('Número inválido para n2. Tente novamente!')
                
            while True:
                try:
                    n3 = int(input('Digite o terceiro número inteiro: '))
                    break
                except:
                    print('Número inválido para n3. Tente novamente!')
                
            while True:
                try:
                    n4 = int(input('Digite o quarto número inteiro: '))
                    break
                except:
                    print('Número inválido para n4. Tente novamente!')
                
            print(f'O maior número é {Max(n1, n2, n3, n4)}')
            break
    
if __name__ == '__main__':
    main()