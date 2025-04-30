import pytest
from q1 import par_impar

def test_q1():
    assert par_impar(1) == False # Testando classe valor limítrofe.
    assert par_impar(2) == True # Testando classe par.
    assert par_impar(-3) == False # Testando classe impar.
    assert par_impar(3.5) == Exception # Testando valores inválidos ou improváveis.
    assert par_impar('a') == Exception # Testando valores inválidos ou improváveis.
    print('Testes passados com sucesso!')