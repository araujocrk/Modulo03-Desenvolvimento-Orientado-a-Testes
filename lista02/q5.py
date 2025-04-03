def main():
# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
# elementos deste em uma outra lista de 20 elementos.
    l1 = []
    l2 = []
    l3 = []
    contador = 1
    while contador <= 10:
        try:
            n = int(input(f'Digite o {contador} número da primeira lista: '))
            l1.append(n)
            contador += 1
        except:
            print(f'Número {contador} inválido. Tente novamente')
            
    contador = 1
    while contador <= 10:
        try:
            n = int(input(f'Digite o {contador} número da segunda lista: '))
            l2.append(n)
            contador += 1
        except:
            print(f' número {contador} inválido. Tente novamente')
            
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    print(l3)
                    
if __name__ == '__main__':
    main()