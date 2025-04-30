# Questão 03
def fahrenheit_To_Celsius(f):
    if isinstance(f, str):
        return Exception
    return round(((f-32)/9)*5)

def main():
    
    while True:
        try:
            fah = float(input('Digite a temperatura em fahrenheit: '))
            print(f'{fahrenheit_To_Celsius(fah):.2f}')
            break
        except:
            print('Temperatura inválida. Tente Novamente!')
            
if __name__ == '__main__':
    main()