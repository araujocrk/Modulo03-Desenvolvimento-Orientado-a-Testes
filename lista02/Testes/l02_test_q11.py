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

    assert cadastrarNome(['Carlos', 'Henrique'], 'Lucas') == ['Carlos', 'Henrique', 'Lucas']
    assert cadastrarNome([1, 'Carlos', 3], 'Wanderson') == Exception
    assert cadastrarNome([1.5, 'Bruno'], 'Caio') == Exception
    assert cadastrarNome(['Ryan'], 2) == Exception
    
    assert pesquisarNome(['Carlos', 'Henrique'], 'Carlos') == True
    assert pesquisarNome(['Carlos', 'Henrique'], 'Lucas') == False
    assert pesquisarNome([1, 'Carlos', 3], 'Carlos') == Exception
    assert pesquisarNome([1.5, 'Bruno'], 'Bruno') == Exception
    assert pesquisarNome(['Ryan'], 2) == Exception
    
    assert listarNomes(['Carlos', 'Henrique']) == ['Carlos', 'Henrique']
    assert listarNomes(['Wanderson', 'Lucas', 'Carlos', 'Beatriz', 'Isadora']) == ['Wanderson', 'Lucas', 'Carlos', 'Beatriz', 'Isadora']
    assert listarNomes(['Carlos', 3]) == Exception
    assert listarNomes([1.5, 'Ryan']) == Exception
    print('Testes passados com sucesso!')

if __name__ == '__main__':
    main()