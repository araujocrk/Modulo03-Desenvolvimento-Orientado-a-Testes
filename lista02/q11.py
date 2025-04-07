def cadastrarNome(lista):
    nome = input('Digite o nome que você deseja adicionar: ')
    lista.append(nome)

def pesquisarNome(lista):
    nome = input('Digite o nome que você deseja pesquisar: ')
    if nome in lista:
        return 'Este nome está na lista.'
    else:
        return 'Este nome não está na lista.'
    
def listarNomes(lista):
    for nome in lista:
        print(nome)

def main():
# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0) Sair do programa
# ——————–
# Digite sua escolha:_
    nomes = []
    contador = 0
    while True:
        try:
            qtdLista = int(input('Quantos nomes você deseja na lista: '))
            break
        except:
            print('Quantidade inválida. Tente novamente!')

    while contador < qtdLista:
        try:
            escolha = int(input('''
    1)Cadastar nome
    2)Pesquisar nome
    3)Listar todos os nome
    0) Sair do programa
    ——————–
    Digite sua escolha:_'''))
            if escolha == 1:
                cadastrarNome(nomes)
                contador += 1
            elif escolha == 2:
                print(pesquisarNome(nomes))
            elif escolha == 3:
                listarNomes(nomes)
            elif escolha == 0:
                break
            else:
                print('Escolha inválida. Tente novamente!')
        except:
            print('Escolha inválida. Tente novamente!')
    print(listarNomes(nomes))
if __name__ == '__main__':
    main()