'''
AULA 40 - FOR - ELSE
'''

variavel = ['Luiz Otavio', 'Joaozinho', 'Maria']        # lista com strings

for valor in variavel:
    if valor.startswith('J'):  # starswith - testa se a variavel começa com 'J'
        print('Começa com J',valor)
    else:
        print('Não começa com J', valor)

# break - para a execução da linhas
# continue - pula a execução do laço  e vai para o proximo bloco

