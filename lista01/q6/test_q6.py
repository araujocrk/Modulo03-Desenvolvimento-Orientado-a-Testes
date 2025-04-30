import pytest
from q6 import poligonoRegular

def test_poligonoRegular():
    assert poligonoRegular(3, 10) == 'TRIÂNGULO; Perímetro: 30 cm' # Testando classe válida
    assert poligonoRegular(4, 10) == 'QUADRADO; Área: 100 cm²' # Testando classe válida
    assert poligonoRegular(5, 10) == 'PENTÁGONO' # Testando classe válida
    assert poligonoRegular(2, 10) == Exception # Testando classe inválida
    assert poligonoRegular(3, 'a') == Exception # Testando classe inválida
    assert poligonoRegular('b', 10) == Exception # Testando classe inválida
    assert poligonoRegular(-1, 10) == Exception # Testando classe inválida
    assert poligonoRegular(10, -1) == Exception # Testando classe inválida
    print('Testes passados com sucesso!')