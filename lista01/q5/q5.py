def pesoIdeal(altura, sexo):
    if isinstance(altura, str) or altura < 0.30 or altura > 2.80:
        return Exception
    if sexo == 1:
        return round((62.1 * altura) - 44.7, 2)
    elif sexo == 2:
        return round((72.7 * altura) - 58, 2)
    else:
        return Exception

def main():
    
    while True:
        try:
            h = float(input('Digite a sua altura em m: '))
            if h >= 0.30 and h <= 2.80:
                break
            else:
                print('Altura deve estar entre 0.30 e 2.80 metros. Tente novamente!')
        except:
            print('Altura inválida. Tente novamente!')
    while True:
        try:
            s = int(input('Digite o seu sexo (1-feminino, 2-masculino): '))
            if s == 1 or s == 2:
                print(f'O seu peso ideal é : {pesoIdeal(h, s):.2f} kg.')
                break
            else:
                print('Sexo deve ser 1 para feminino ou 2 para masculino. Tente novamente!')
        except:
            print('Sexo inválido. Tente novamente!')
            
if __name__ == '__main__':
    main()