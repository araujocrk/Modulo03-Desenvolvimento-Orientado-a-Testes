from q11 import cadastrarNome, pesquisarNome, listarNomes

def test_cadastrarNome():
    assert cadastrarNome(['Carlos', 'Henrique'], 'Lucas') == ['Carlos', 'Henrique', 'Lucas']
    assert cadastrarNome([1, 'Carlos', 3], 'Wanderson') == Exception
    assert cadastrarNome([1.5, 'Bruno'], 'Caio') == Exception
    assert cadastrarNome(['Ryan'], 2) == Exception
    
def test_pesquisarNome():
    assert pesquisarNome(['Carlos', 'Henrique'], 'Carlos') == True
    assert pesquisarNome(['Carlos', 'Henrique'], 'Lucas') == False
    assert pesquisarNome([1, 'Carlos', 3], 'Carlos') == Exception
    assert pesquisarNome([1.5, 'Bruno'], 'Bruno') == Exception
    assert pesquisarNome(['Ryan'], 2) == Exception
    
def test_listarNomes():
    assert listarNomes(['Carlos', 'Henrique']) == ['Carlos', 'Henrique']
    assert listarNomes(['Wanderson', 'Lucas', 'Carlos', 'Beatriz', 'Isadora']) == ['Wanderson', 'Lucas', 'Carlos', 'Beatriz', 'Isadora']
    assert listarNomes(['Carlos', 3]) == Exception
    assert listarNomes([1.5, 'Ryan']) == Exception
    