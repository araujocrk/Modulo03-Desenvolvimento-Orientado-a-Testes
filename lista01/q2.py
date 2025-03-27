# Questão 02
def area(r):
    PI = 3.14
    return PI * (r ** 2)


def perimetro(r):
    PI = 3.14
    return PI * 2 * r

def main():
    while True:
        try:
            raio = float(input('Digite o raio do círculo: '))
            print(area(raio))
            print(perimetro(raio))
            break
        except:
            print('Número inválido. Tente novamente!')
            
if __name__ == '__main__':
    main()