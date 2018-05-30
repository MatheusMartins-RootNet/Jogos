import os
from random import *

pontos = 0
tentativas = 1
escolha = 1

def limpar():
    so = os.name
    if so == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpar()
print("Deseja qual dificuldade? \n[01] Facil \t 2 Numeros \n[02] Normal \t 5 Numeros \n[03] Dificil \t 10 Numeros\n[04] Insano \t 10 Numeros e 5 chances")


tipo = int(input())
if tipo == 1:
    lista = (1, 2)

elif tipo == 2:
    lista = (1, 5, 2, 3 , 4)

elif tipo == 3:
    lista = (1, 10, 2, 3, 4, 5, 6, 7, 8, 9)

else:
    lista = (1, 10, 2, 3, 4, 5, 6, 7, 8, 9)
    chances = 5

numeros = sorted(lista)

if tipo != 4:
    while True:
        num = randint(lista[0], lista[1])
        limpar()
        print("Digite um numero entre",lista[0], "e", sorted(lista, reverse=True)[0])
        print("")
        print("Pontos", pontos, "\t Tentativa", tentativas)

        tent = int(input("R."))

        if tent > 10:
            limpar()
            print("Seu numero não esta dentro da lista de permitidos!!!")
            print("Por favor, escreva somente numeros listados!")
            input("Digite algo para continuar ")

        elif tent == num:
            limpar()
            print("Parabéns voce acertou! =)")
            pontos += 1
            tentativas += 1
            input(print("Digite algo para continuar"))
        
        else:
            limpar()    
            print("Que pena, voce errou! =(")
            print("O numero correto era", num)
            tentativas += 1
            input("Digite qualquer coisa para continuar.")
    
    limpar()
    print("Obrigado por jogar \nFeito por: Matheus Martins")

if tipo == 4:
    while chances > 0:
        limpar()
        num = randint(lista[0], lista[1])
        print("Seja bem vindo ao modo Insano \n")
        print("Voce tem", chances, "chances ainda")
        print("Sempre que acertar, ira ganhar duas chances \nE se perder, ira perder uma chance")
        print("\n\tBoa Sorte")
        print("\nNumeros Permitidos\n", sorted(lista))
        tent = int(input("R."))

        if tent > 10:
            limpar()
            print("Seu numero não esta dentro da lista de permitidos!!!")
            print("Por favor, escreva somente numeros listados!")
            input("Digite algo para continuar ")

        elif tent == num:
            limpar()
            print("Parabéns voce acertou! =)")
            chances += 2
            input(print("Digite algo para continuar"))
        
        else:
            limpar()    
            print("Que pena, voce errou! =(")
            print("O numero correto era", num)
            chances -= 1
            input("Digite qualquer coisa para continuar.")
    limpar()
    print("Que pena, voce perdeu\nTente novamente sempre que quiser")
    print("\nObrigado por jogar \nFeito por: Matheus Martins")
