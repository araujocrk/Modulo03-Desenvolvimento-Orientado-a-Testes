import pytest 
from q2 import area, perimetro

def test_area():
    assert area(1) == 3.14 # Testando valor limítrofe.
    assert area(2.5) == 19.62 # Testando float.
    assert area('a') == Exception # Testando valores inválidos ou improváveis.
    assert area(0) == Exception # Testando valores inválidos ou improváveis.
    assert area(-1) == Exception # Testando valores inválidos ou improváveis.
    print('Testes passados com sucesso!')
    
def test_perimetro():
    assert perimetro(1) == 6.28 # Testando valor limítrofe.
    assert perimetro(2.5) == 15.70 # Testando float.
    assert perimetro('a') == Exception # Testando valores inválidos ou improváveis.
    assert perimetro(0) == Exception # Testando valores inválidos ou improváveis.
    assert perimetro(-1) == Exception # Testando valores inválidos ou improváveis.
    print('Testes passados com sucesso!')