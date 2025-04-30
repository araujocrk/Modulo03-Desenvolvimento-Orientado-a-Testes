import pytest
from q3 import fahrenheit_To_Celsius

def test_fahrenheit_To_Celsius():
    assert fahrenheit_To_Celsius(1) == -17
    assert fahrenheit_To_Celsius(-1) == -18
    assert fahrenheit_To_Celsius(80) == 27
    assert fahrenheit_To_Celsius(50.5) == 10
    assert fahrenheit_To_Celsius('a') == Exception
    print('Testes passados com sucesso!')