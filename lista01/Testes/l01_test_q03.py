# Questão 03
def fahrenheit_To_Celsius(f):
    if isinstance(f, str):
        return Exception
    return round(((f-32)/9)*5)

def main():
    
    assert fahrenheit_To_Celsius(1) == -17
    assert fahrenheit_To_Celsius(-1) == -18
    assert fahrenheit_To_Celsius(80) == 27
    assert fahrenheit_To_Celsius(50.5) == 10
    assert fahrenheit_To_Celsius('a') == Exception
    print('Testes passados com sucesso!')
            
if __name__ == '__main__':
    main()