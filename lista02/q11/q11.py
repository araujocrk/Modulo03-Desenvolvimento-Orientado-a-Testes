def cadastrarNome(lista, nome):
    if not all(isinstance(i, str) for i in lista) or not isinstance(nome, str):
        return Exception
    lista.append(nome)
    return lista

def pesquisarNome(lista, nome):
    if not all(isinstance(i, str) for i in lista) or not isinstance(nome, str):
        return Exception
    if nome in lista:
        return True
    else:
        return False
    
def listarNomes(lista):
    if not all(isinstance(i, str) for i in lista):
        return Exception
    return lista

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