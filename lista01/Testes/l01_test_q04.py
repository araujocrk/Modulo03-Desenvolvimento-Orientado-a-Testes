def passou_De_Ano(n1, n2):
    if isinstance(n1, str) or isinstance(n2, str) or n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
        return Exception
    media = (n1 + n2) / 2
    if media >= 6:
        return round(media, 1)
    else:
        return round(media, 1)

def main():
    
    while True:
        try:
            n1 = float(input('Digite sua primeira nota: '))
            break
        except:
            print('Primeira nota inválida. Tente novamente!')
    
    while True:
        try:
            n2 = float(input('Digite sua segunda nota: '))
            print(passou_De_Ano(n1, n2))
            break
        except:
            print('Segunda nota inválida. Tente novamente!')
            
if __name__ == '__main__':
    main()