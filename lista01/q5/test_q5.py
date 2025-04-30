import pytest
from q5 import pesoIdeal

def test_pesoIdeal():
    assert pesoIdeal(0.30, 1) == -26.07 # Testanto valor limítrofe.
    assert pesoIdeal(0.30, 2) == -36.19 # Testanto valor limítrofe.
    assert pesoIdeal(2.80, 1) == 129.18 # Testeando classe válida
    assert pesoIdeal(2.80, 2) == 145.56 # Testeando classe válida
    assert pesoIdeal('a', 1) == Exception # Testando classe inválida.
    assert pesoIdeal(2.80, 'b') == Exception # Testando classe inválida.
    assert pesoIdeal(-1, 1) == Exception # Testando classe inválida.
    assert pesoIdeal(2.80, -1) == Exception # Testando classe inválida.
    print('Testes passados com sucesso!')