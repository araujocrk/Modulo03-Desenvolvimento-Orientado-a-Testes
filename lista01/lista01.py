# Questão 01
def par_impar(n):
    
    return n % 2 == 0


# Questão 02
def area(r):
    PI = 3.14
    return PI * (r ** 2)


def perimetro(r):
    PI = 3.14
    return PI * 2 * r


# Questão 03
def fahrenheit_To_Celsius(f):
    return ((f-32)/9)*5


# Questão 04
def passou_De_Ano(n1, n2):
    media = (n1 + n2) / 2
    if media >= 6:
        return f'Média: {media}\nPARABÉNS! Você foi aprovado!'
    else:
        return f'Média: {media}\nVocê foi reprovado!'
    


# Questão 05
# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:

def pesoIdeal(altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    elif sexo == 2:
        return (72.7 * altura) - 58
    
# Questão 6
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
# Questão 01
# Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except:
            print('Número inválido. Tente Novamete!')
        if par_impar(num) == True:
            print('Este número é par!')
        else:
            print('Este número é impar!')
        break

# Questão 02
# Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
# do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;
    while True:
        try:
            raio = float(input('Digite o raio do círculo: '))
            print(area(raio))
            print(perimetro(raio))
            break
        except:
            print('Número inválido. Tente novamente!')

# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5
    while True:
        try:
            fah = float(input('Digite a temperatura em fahrenheit: '))
            print(f'{fahrenheit_To_Celsius(fah):.2f}')
            break
        except:
            print('Temperatura inválida. Tente Novamente!')

# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação).
    while True:
        try:
            n1 = float(input('Digite sua primeira nota: '))
            n2 = float(input('Digite sua segunda nota: '))
            print(passou_De_Ano(n1, n2))
            break
        except:
            print('Nota inválida. Tente novamente!')

# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
    while True:
        try:
            h = float(input('Digite a sua altura em m: '))
            if h >= 0.30 and h <= 2.80:
                pass
            else:
                raise Exception
        except:
            print('Altura inválida. Tente novamente!')
        try:
            s = float(input('Digite o seu sexo: '))
            if s == 1 or s == 2:
                print(pesoIdeal(h, s))
                break
            else:
                raise Exception
        except:
            print('Sexo inválido. Tente novamente!')

# Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.
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