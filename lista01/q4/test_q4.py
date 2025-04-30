import pytest
from q4 import passou_De_Ano

def test_passou_De_Ano():
    assert passou_De_Ano(0, 0) == 0 # Testando valor limítrofe.
    assert passou_De_Ano(6, 6) == 6.0 # Testando valor limítrofe.
    assert passou_De_Ano(6.5, 7.5) == 7.0 # Testando valor limítrofe.
    assert passou_De_Ano('a', 7) == Exception # Testando classe inválida.
    assert passou_De_Ano(7, 'b') == Exception # Testando classe inválida.
    assert passou_De_Ano(-1, 7) == Exception # Testando classe inválida.
    assert passou_De_Ano(7, -1) == Exception # Testando classe inválida.
    assert passou_De_Ano(11, 7) == Exception # Testando classe inválida.
    assert passou_De_Ano(7, 11) == Exception # Testando classe inválida.
    print('Testes passados com sucesso!')