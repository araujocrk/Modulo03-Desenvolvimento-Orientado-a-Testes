def calculaPoligono(lados, medida):
    if lados == 3:
        perimetro = medida * lados
        return f'TRIÃNGULO; Perímetro: {perimetro}'
    elif lados == 4: 
        area = lados * lados
        return f'QUADRADO; Área: {area}' 
    else:
        return 'PENTÁGONO'

def main():
    while True:
        try:   
            numeroLados = int(input('Insira o numero de lados: '))
        except:
            raise ValueError('Digite o numero de lados entre 3 e 5')
        try:
            medida = int(input('Insira a medida dos lados em cm: '))
        except: 
            raise TypeError('Entrada inválida')
        resultadoPoligono = calculaPoligono(numeroLados, medida)
        print(resultadoPoligono)
if __name__ == '__main__':
    main()