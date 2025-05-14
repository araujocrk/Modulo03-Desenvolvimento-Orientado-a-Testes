def poligonoRegular(nl, ml):
    if isinstance(nl, str) or isinstance(ml, str) or nl < 3 or nl > 5 or ml <= 0:
        return Exception
    if nl == 3:
        return f'TRIÂNGULO; Perímetro: {ml * nl} cm'
    elif nl == 4:
        return f'QUADRADO; Área: {ml * ml} cm²'
    else:
        return 'PENTÁGONO'
    
def main():
    
    assert poligonoRegular(3, 10) == 'TRIÂNGULO; Perímetro: 30 cm' # Testando classe válida
    assert poligonoRegular(4, 10) == 'QUADRADO; Área: 100 cm²' # Testando classe válida
    assert poligonoRegular(5, 10) == 'PENTÁGONO' # Testando classe válida
    assert poligonoRegular(2, 10) == Exception # Testando classe inválida
    assert poligonoRegular(3, 'a') == Exception # Testando classe inválida
    assert poligonoRegular('b', 10) == Exception # Testando classe inválida
    assert poligonoRegular(-1, 10) == Exception # Testando classe inválida
    assert poligonoRegular(10, -1) == Exception # Testando classe inválida
    print('Testes passados com sucesso!')
            
if __name__ == '__main__':
    main()