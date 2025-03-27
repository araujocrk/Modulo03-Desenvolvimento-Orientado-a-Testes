def passou_De_Ano(n1, n2):
    media = (n1 + n2) / 2
    if media >= 6:
        return f'Média: {media}\nPARABÉNS! Você foi aprovado!'
    else:
        return f'Média: {media}\nVocê foi reprovado!'

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