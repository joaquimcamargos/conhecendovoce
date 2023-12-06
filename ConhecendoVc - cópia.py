Nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {Nome}')
Nasce = input('Que mês você nasceu? ')
Cor = input('\033[7;34mQuais são suas cores favoritas (escreva duas cores)? \033[m ')
print('As cores {} são as melhores cores do mundo! Tamo junto {}'.format(Cor, Nome))
idade_input = input("Qual é a sua idade? ")
print(f'Vamos aprender a tabuada {Nome}')
num = int(input('Digite um número para a sua tabuada '))
print('\033[1;34m-=-\033[m'*5)
print(f'{num} x {1} = {num*1}')
print(f'{num} x {2} = {num*2}')
print(f'{num} x {3} = {num*3}')
print(f'{num} x {4} = {num*4}')
print(f'{num} x {5} = {num*5}')
print(f'{num} x {6} = {num*6}')
print(f'{num} x {7} = {num*7}')
print(f'{num} x {8} = {num*8}')
print(f'{num} x {9} = {num*9}')
print(f'{num} x {10} = {num*10}')
print('\033[1;34m-=-\033[m'*5)
Peso = input('Qual é seu peso aproximado? ')
Comida = input('Qual é a sua comida favorita? ')
print('Comer {} é muito bom {}'.format(Comida, Nome))
Gosta = input('O que você mais gosta de fazer? ')
print('Que legal! Eu também gosto de {} {}!'.format(Gosta, Nome))
Estação = input('Qual é a sua estação do ano preferida? ')
print('O(a) {} é muito bom {}'.format(Estação, Nome))
Dia = input('Qual é seu dia da semana preferido? ')
print('Eu também gosto muito dos dias de {} {}'.format(Dia, Nome))
print('Hora dos jogos!')
print('Par ou Ímpar')
print('\033[1;31m-=-\033[m'*13)
from random import randint

v = 0
while True:
        jogador = int(input('Digite um valor'))
        computador = randint(0, 11)
        total = jogador + computador
        tipo = '  '
        while tipo not in 'PI':
            tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total {total}')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você venceu!')
                v += 1
                break
            else:
                print('Você perdeu!')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você venceu!')
                v += 1
                break
            else:
                print('Você perdeu!')
                break
print('\033[1;31m-=-\033[m'*13)
print('Jogo da adivinhação')
computador1 = randint(0, 5)
print('Vou pensar entre um número entre 0 e 5')
jogador = int(input('Em que número eu pensei? '))
if jogador == computador1:
    print('PARABÉNS você conseguiu me vencer!')
else:
    print('Você não conseguiu né? Vamos diminuir a dificuldade 0 até 4')
    número = randint(0, 4)
    jogador1 = int(input('Eu vou repetir... Em que número eu pensei {} '.format(Nome)))
    if jogador1 == número:
        print('Parabéns! Você acertou!')
    else:
        print('Você não conseguiu né? Vamos diminuir a dificuldade 0 até 3')
        número1 = randint(0, 3)
        jogador2 = int(input('Eu vou repetir pela 2 vez... Em que número eu pensei {} '.format(Nome)))
        if jogador2 == número1:
            print('Parabéns! Você acertou!')
        else:
            print('Você não conseguiu né? Vamos diminuir a dificuldade 0 até 2')
            número2 = randint(0, 2)
            jogador3 = int(input('Eu vou repetir pela 3 vez... Em que número eu pensei {} '.format(Nome)))
            if jogador3 == número2:
                print('Parabéns! Você acertou!')
            else:
                print('Você não conseguiu né? Vamos diminuir a dificuldade 0 ou 1')
                número3 = randint(0, 1)
                jogador4 = int(input('Eu vou repetir pela 4 e última vez... Em que número eu pensei {} '.format(Nome)))
                if jogador4 == número3:
                    print('Parabéns! Você acertou!')
                else:
                    print('Melhore suas adivinhações {}, você não foi bem... Pensei no número {} não no número {}'.format(Nome, número3, jogador4))
print(f'Legal {Nome}, agora vamos saber se você é esperto')
print('\033[1;31m-=-\033[m'*13)
print('Hora de digirir')
velocidade = float(input('Digite um velocidade de carro'))
if velocidade > 80:
    print('Você foi MULTADO! o limite era de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print(f'Dirija com segurança {Nome}')
print('Vamos ver se você sabe fazer contas')
v = 0
print('Mais (+)')
computador = randint(1, 10)
com = randint(1, 10)
pergunta = int(input(f'Quanto é {computador} + {com}? '))
total = computador + com
if pergunta == total:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {total}')
computador1 = randint(1, 10)
com1 = randint(1, 10)
pergunta1 = int(input(f'Quanto é {computador1} + {com1}? '))
total1 = computador1 + com1
if pergunta1 == total1:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {total1}')
computador2 = randint(1, 10)
com2 = randint(1, 10)
pergunta2 = int(input(f'Quanto é {computador2} + {com2}? '))
total2 = computador2 + com2
if pergunta2 == total2:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {total2}')
computador3 = randint(1, 10)
com3 = randint(1, 10)
pergunta3 = int(input(f'Quanto é {computador3} + {com3}? '))
total3 = computador3 + com3
if pergunta3 == total3:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {total3}')
print(f'Até aqui, você acertou {v} vezes')
print('Menos (-)')
note = randint(5, 10)
no = randint(1, 4)
per = int(input(f'Quanto é {note} - {no}? '))
tote = note - no
if per == tote:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {tote}')
note1 = randint(5, 10)
no1 = randint(1, 4)
per1 = int(input(f'Quanto é {note1} - {no1}? '))
tote1 = note1 - no1
if per1 == tote1:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {tote1}')
note2 = randint(5, 10)
no2 = randint(1, 4)
per2 = int(input(f'Quanto é {note2} - {no2}? '))
tote2 = note2 - no2
if per2 == tote2:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {tote2}')
note3 = randint(5, 10)
no3 = randint(1, 4)
per3 = int(input(f'Quanto é {note3} - {no3}? '))
tote3 = note3 - no3
if per3 == tote3:
    print('Acertou!')
    v += 1
else:
    print(f'Errou! A resposta é {tote3}')
print(f'PARABÉNS! Você acertou {v} vezes')
print('\033[1;31m-=-\033[m'*13)
Animal = input('Qual é seu animal favorito {}? '.format(Nome))
print('Eu também gosto muito de {} {}'.format(Animal, Nome))
Mês = input('Qual é seu mês favorito {}? '.format(Nome))
print('Eu também gosto muito do mês de {}'.format(Mês))
print('Aqui estão os seus resultados')
print(f'Seu nome é {Nome}')
print(f'Você nasceu no mês de {Nasce}')
print('Suas cores favoritas são {}'.format(Cor))
if idade_input.endswith("anos"):
    idade = idade_input[:-4]
else:
    idade = idade_input
print(f'Você tem {idade} anos')
print('Seu peso é {} Kg'.format(Peso))
print(f'Sua comida favorita é {Comida}')
print('Você gosta muito de {}'.format(Gosta))
print(f'Sua estação do ano preferida é {Estação}')
print('Seu dia da semana preferido é {}'.format(Dia))
print(f'Seu animal preferido é o(a) {Animal}')
print('Seu mês favorito é o mês de {}'.format(Mês))
Responde = str(input('Esse é você? Sim ou Não? ')).strip().lower()
if Responde == 'sim' or 's':
    print('\033[7;40mMuito obrigado {} por ter te conhecido\033[m'.format(Nome))
else:
    print('Tente novamente {}'.format(Nome))
resposta2 = input('Quer conhecer sobre o programador?').strip().lower()
if resposta2 == 'sim' or 's':
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
#Instalar a biblioteca
    driver = webdriver.Chrome(ChromeDriverManager().install())
#Rodando o site
    driver.get('file:///Users/Joaquim/Downloads/Meu%20primeiro%20site/Joaquim.html')
#Tempo para fechar o site
    time.sleep(120000000)
