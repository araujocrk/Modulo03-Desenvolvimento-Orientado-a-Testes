# Questão 02
def area(r):
    if isinstance(r, str) or r <= 0:
        return Exception
    PI = 3.14
    return round(PI * (r ** 2), 2)

def perimetro(r):
    if isinstance(r, str) or r <= 0:
        return Exception
    PI = 3.14
    return round(PI * 2 * r, 2)

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