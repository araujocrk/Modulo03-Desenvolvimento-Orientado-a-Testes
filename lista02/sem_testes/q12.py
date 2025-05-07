def main():
# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas. 
    gabarito = []
    print(len(gabarito))
    contador = 1
    while len(gabarito) < 30:
        try:
            respostaGabarito = input(f'Digite a resposta da {contador}ª questão de 30 (A-E): ').upper()
            if respostaGabarito in 'ABCDE':
                contador += 1
                gabarito.append(respostaGabarito)
            else:
                raise Exception()
        except Exception:
            print('Resposta da questão inválida, tente novamente.')
    
    while True:
        try:
            qtdAlunos = int(input('Digite o número de alunos: '))
            break
        except:
            print('Quantidade de alunos inválida. Tente novamente.')
            
    for i in range(qtdAlunos):
        respostasAluno = []
        nome = input('Nome do aluno: ')
        while len(respostasAluno) < 30:
            try:
                respostaAluno = input(f'Digite a resposta do aluno {nome}, questão {i+1}ª de 30 (A-E): ').upper()
                if respostaAluno in 'ABCDE':
                    respostasAluno.append(respostaAluno)
                else:
                    raise Exception()
            except Exception:
                print('Resposta da questão inválida, tente novamente.')
                
        for 
        
            
if __name__ == '__main__':
    main()