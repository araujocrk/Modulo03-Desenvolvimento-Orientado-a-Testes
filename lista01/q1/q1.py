# Questão 01
def par_impar(n):
    if isinstance(n, (float, str)):
        return Exception
    return n % 2 == 0

def main():
# Questão 01
# Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            if par_impar(num) == True:
                print('Este número é par!')
            else:
                print('Este número é impar!')
            break
        except:
            print('Número inválido. Tente Novamete!')

if __name__ == '__main__':
    main()