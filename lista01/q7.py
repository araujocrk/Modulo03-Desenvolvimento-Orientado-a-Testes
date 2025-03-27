def calcularFatorial(fatorial):
    resultado = 1
    if fatorial == 0 or fatorial == 1:
        return 1
    else:
        for i in range(1, fatorial + 1):
            resultado *= i
        return resultado

def main():
# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro. 
    while True:
        try:
            fatorial = int(input('Digite um número inteiro para calcular o fatorial: '))
            if fatorial >= 0:
                print(f'O fatorial de {fatorial} é {calcularFatorial(fatorial)}')
                break
            else:
                print('O número deve ser maior ou igual a 0 e inteiro. Tente novamente!')
        except:
            print('Número inválido. Tente novamente!')
            
if __name__ == '__main__':
    main()