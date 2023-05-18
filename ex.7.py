nota = float(input('Informe a sua media:'))

if 9 <= nota <= 10:
    print('A classificação do aluno é Superior:')
elif 7 <= nota <= 8.9:
    print('A classificação do aluno é Médio Superior:')
elif 5 <= nota <= 6.9:
    print('A classificação do aluno é Médio:')
elif 3 <= nota <= 4.9:
    print('A classificação do aluno é Médio inferior:')
elif 1 <= nota <= 2.9:
    print('A classificação do aluno é Inferior:')
else:
    print('Sem Rendimento:')