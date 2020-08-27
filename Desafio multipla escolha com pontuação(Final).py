score = 0
print('''
Q1 - De quem é a famosa frase "penso, logo existo"?
a - Platão
b - Galileu Galilei
c - Descartes
d - Sócrates''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :(')
elif resposta=='b':
    print('Errado :(')
elif resposta=='c':
    print('Correto!! :)')
    score = score + 1
elif resposta=='d':
    print('errado :(')
else:
    print('Você não escolheu a, b, c ou d :(')

print('''
Q2 - De onde é a invenção do chuveiro elétrico?
a - França
b - Brasil
c - Inglaterra
d - Itália''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :(')
elif resposta=='b':
    print('Correto!! :)')
    score = score + 1
elif resposta=='c':
    print('Errado :(')
elif resposta=='d':
    print('errado :(')
else:
    print('Você não escolheu a, b, c ou d :(')

print('''
Q3 - Qual o menor e o maior país do mundo?
a - Vaticano e Rússia
b - Nauru e China
c - Mônaco e Canadá
d - São Marino e Índia''')
resposta = input().lower()

if resposta == 'a':
    print('Correto!! :)')
    score = score + 1
elif resposta=='b':
    print('Errado :(')
elif resposta=='c':
    print('Errado :(')
elif resposta=='d':
    print('Errado :(')
else:
    print('Você não escolheu a, b, c ou d :(')

print('''
Q4 - Qual o nome do presidente do Brasil que ficou conhecido como Jango?
a - Jânio Quadros
b - Getúlio Vargas
c - João Figueiredo
d - João Goulart''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :(')
elif resposta=='b':
    print('Errado :(')
elif resposta=='c':
    print('Errado :(')
elif resposta=='d':
    print('Correto!! :)')
    score = score + 1
else:
    print('Você não escolheu a, b, c ou d :(')

print('''
Q5 - Quantos graus são necessários para que dois ângulos sejam complementares?
a - 45°
b - 60°
c - 90°
d - 360°''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :(')
elif resposta=='b':
    print('Errado :(')
elif resposta=='c':
    print('Correto!! :)')
    score = score + 1
elif resposta=='d':
    print('Errado :(')
else:
    print('Você não escolheu a, b, c ou d :(')

print(f'Você marcou {score} pontos, tente novamente :(')
