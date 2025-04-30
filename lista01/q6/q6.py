def poligonoRegular(nl, ml):
    if isinstance(nl, str) or isinstance(ml, str) or nl < 3 or nl > 5 or ml <= 0:
        return Exception
    if nl == 3:
        return f'TRIÂNGULO; Perímetro: {ml * nl} cm'
    elif nl == 4:
        return f'QUADRADO; Área: {ml * ml} cm²'
    else:
        return 'PENTÁGONO'
    
def main():
    while True:
        try:
            n = int(input('Insira o número de lados: '))
            if n >= 3 and n <= 5:
                break
            else:
                print('Digite o número de lados entre 3 e 5. Tente novamente!')
        except:
            print('Número de lados inválido. Tente novamente!')
    
    while True:
        try:
            m = float(input('Insira a medida dos lados em cm: '))
            print(poligonoRegular(n, m))
            break
        except:
            print('Medida dos lados inválida. Tente novamente!')
            
if __name__ == '__main__':
    main()