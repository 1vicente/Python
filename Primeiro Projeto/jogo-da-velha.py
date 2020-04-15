# -*- Coding: UTF-8 -*-
#coding: utf-8
lista = [[''], ['0', '1', '1', '1'], ['0', '2', '2', '2'], ['0', '3', '3', '3']]

#teste


# Função que define o tabuleiro
def tabuleiro():
    print("""
         1       2       3
    1    %s   |   %s   |   %s   \n
        -------------------\n
    2    %s   |   %s   |   %s   \n
        -------------------\n
    3    %s   |   %s   |   %s   \n
          """ % (lista[1][1], lista[1][2], lista[1][3], lista[2][1], lista[2][2], lista[2][3], lista[3][1], lista[3][2], lista[3][3]))


# Função que define as condições de vitória por linha horizontal, vertical ou diagonal
def vitoria():
    if len(set(lista[1])) == 2:
        print('O jogador %s ganhou.' % (lista[1][1]))
    elif lista[1][1] == lista[2][1] == lista[3][1]:
        print('O jogador %s ganhou.' % (lista[1][1]))
    elif lista[1][2] == lista[2][2] == lista[3][2]:
        print('O jogador %s ganhou.' % (lista[1][2]))
    elif lista[1][3] == lista[2][3] == lista[3][3]:
        print('O jogador %s ganhou.' % (lista[1][3]))
    elif lista[1][1] == lista[2][2] == lista[3][3]:
        print('O jogador %s ganhou.' % (lista[1][1]))
    elif lista[3][1] == lista[2][2] == lista[1][3]:
        print('O jogador %s ganhou.' % (lista[3][1]))


# Função que decide de quem é a vez de jogar
def jogada():
    count = 1
    while count <= 9:
        if count % 2 == 0:
            print('~~~ Vez do X jogar ~~~')
            i = int(input('Digite o numero da linha desejada: '))
            j = int(input('Digite o numero da coluna desejada: '))
            lista[i][j] = 'X'
            tabuleiro()
            vitoria()
            count += 1
        else:
            print('~~~ Vez do O jogar ~~~')
            i = int(input('Digite o numero da linha desejada: '))
            j = int(input('Digite o numero da coluna desejada: '))
            lista[i][j] = 'O'
            tabuleiro()
            vitoria()
            count += 1


# Início do cógido onde as funções são chamadas
again = 'yes'
while again == 'yes':
    tabuleiro()
    jogada()
    again = input("""Deseja jogar novamente?:\n""")
    lista = [[''], ['0', '1', '1', '1'], ['0', '2', '2', '2'], ['0', '3', '3', '3']]
