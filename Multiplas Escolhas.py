print('''
Q1 - No python, como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variável
c - uma caixa de sapatos
''')
resposta = input().lower()

if resposta == 'a':
    print('Não - texto é um tipo de dado :(')
elif resposta=='b':
    print('correto!! :)')
elif resposta=='c':
    print('Não seja bobinho!:(')
else:
    print('Você não escolheu a, b ou c :(')
