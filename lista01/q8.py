def lerCaractere():
    while True:
        caractere = input('Deseja escolher outro número? (S ou N): ').strip().upper()
        if caractere[0] == 'S' or caractere[0] == 'N':
            print(caractere[0])
            return caractere[0]
        else:
            print('Caractere inválido. Digite novamente')
            lerCaractere()
    
def elevarAoCubo(n):
    return n ** 3

def main():
# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
    while True:
        try:
            numero = float(input('Digite um número para ser elevado ao cubo: '))
            print(f'{elevarAoCubo(numero):.2f}')
            resposta = lerCaractere()
            if resposta == 'N':
                print('Finalizando...')
                break
        except:
            print('Número inválido. Tente novamente.')
            
if __name__ == '__main__':
    main()