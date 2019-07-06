from random import randint
import os

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

player = 0
bender = 0
x = 'X'
o = 'O'
matriz = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    passo = 0
    limpar()
    print('+-=+=-=+=-=+=-=+=-+')
    print('|  Jogo da velha  |')
    print('+-=+=-=+=-=+=-=+=-+\n')

    print(f'+--+--+--+--+')
    print(f'| {matriz[0]} | {matriz[1]} | {matriz[2]} |\t  Placar')
    print(f'| = + = + = |')
    print(f'| {matriz[3]} | {matriz[4]} | {matriz[5]} |\t Player: {player}')
    print(f'| = + = + = |')
    print(f'| {matriz[6]} | {matriz[7]} | {matriz[8]} |\t Bender: {bender}')
    print(f'+--+--+--+--+')

    esc = int(input('\nEscolha sua posição de escolha: '))

    if matriz[esc - 1] == x or matriz[esc - 1] == o:    #Jogada Inválida
        passo = 0

    else:
        matriz[matriz.index(esc)] = x   #Ponto do jogador
        passo = 1

    if passo == 1:
        tent = 0
        while passo == 1:       #Sistema do computador
            tent += 1
            comp = randint(0, 8)

            if matriz[comp] != x and matriz[comp] != o:     #Jogada do computador
                print(2)
                matriz[comp] = o
                passo = 0

            if tent == 9:   #Sistema da velha
                passo = 3
                break

    if passo == 3:
        print('Deu velha')
        break

# Jogador
    if matriz[0] == x and matriz[1] == x and matriz[2] == x:
        passo = 5

    elif matriz[3] == x and matriz[4] == x and matriz[5] == x:
        passo = 5

    elif matriz[6] == x and matriz[7] == x and matriz[8] == x:
        passo = 5

    elif matriz[0] == x and matriz[3] == x and matriz[6] == x:
        passo = 5

    elif matriz[1] == x and matriz[4] == x and matriz[7] == x:
        passo = 5

    elif matriz[2] == x and matriz[5] == x and matriz[8] == x:
        passo = 5

    elif matriz[0] == x and matriz[4] == x and matriz[8] == x:
        passo = 5

    elif matriz[2] == x and matriz[4] == x and matriz[6] == x:
        passo = 5

# Computador
    if matriz[0] == o and matriz[1] == o and matriz[2] == o:
        passo = 6

    elif matriz[3] == o and matriz[4] == o and matriz[5] == o:
        passo = 6

    elif matriz[6] == o and matriz[7] == o and matriz[8] == o:
        passo = 6

    elif matriz[0] == o and matriz[3] == o and matriz[6] == o:
        passo = 6

    elif matriz[1] == o and matriz[4] == o and matriz[7] == o:
        passo = 6

    elif matriz[2] == o and matriz[5] == o and matriz[8] == o:
        passo = 6

    elif matriz[0] == o and matriz[4] == o and matriz[8] == o:
        passo = 6

    elif matriz[2] == o and matriz[4] == o and matriz[6] == o:
        passo = 6


    if passo == 5 or passo == 6:
        break

limpar()
if passo == 5:
    print('Parabéns, Você Ganhou!!!')

elif passo == 6:
    print('Que pena, você perdeu!!!')
    
#Instruçoes de variáveis
# Tent    = Tentativas do computador a jogar
# Passo   = Acesso global a instrução do jogo
# Passo 0 = False
# Passo 1 = True
# Passo 2 = Velha
# Passo 5 = Jogador Ganhou
# Passo 6 = Computador Ganhou
# Player  = Pontos do jogador
# Bender  = Pontos do computador