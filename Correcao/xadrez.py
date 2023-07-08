import random
import numpy as np 
from Piece import Peca 
from Board import Tabuleiro
import sys

class Xadrez:
    def __init__(self):
        pass

    
    @staticmethod
    def mensagem_de_inicio():
        print("****************************")
        print("bem vindo ao jogo de Xadrez!")
        print("****************************\n\n\n")
        print("O tabuleiro tem a dimensão 8 linhas x 8 colunas")
        print("A primeira linha e a primeira coluna têm o índice '0'. A última linha e a última coluna têm o índice '7'")
        print("O primeiro espaço ('00') é o espaço de cima à esquerda")
        print("O último espaço ('77') é o espaço de baixo à direita")
        print("Bom jogo!")

#recebo do teclado: peça + posicao.
#jogo realiza o movimento e pede um novo input
#o jogo é só isso. 
    @staticmethod
    def qual_movimento_fazer(peca_do_teclado, posicao_do_teclado, tabuleiro, lista_pecas, index_peca_a_mover):
        tipo_da_peca = peca_do_teclado[:2]
        if(tipo_da_peca == "Pp"):
            #print("{}  {}").format(lista_pecas[index_peca_a_mover], posicao_do_teclado)
            #tabuleiro = objeto_tabuleiro.movimento_peao_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
            tabuleiro = Tabuleiro.movimento_peao_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
            #print("ta vindo aqui?")
            #return tabuleiro
        elif(tipo_da_peca == "Pb"): 
            Tabuleiro.movimento_peao_branco(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
            #return tabuleiro
        
        elif(tipo_da_peca == "Tp"):
            Tabuleiro.movimento_torre_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)

        elif(tipo_da_peca == "Tb"):
            Tabuleiro.movimento_torre_branco(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)

        elif(tipo_da_peca == "Cp"):
            Tabuleiro.movimento_cavalo_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)

        elif(tipo_da_peca == "Cb"):
            Tabuleiro.movimento_cavalo_branco(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
        
        elif(tipo_da_peca == "Bp"):
            Tabuleiro.movimento_bispo_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)

        elif(tipo_da_peca == "Bb"):
            Tabuleiro.movimento_bispo_branco(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
        
        elif(peca_do_teclado == "Qp"):
            #print("{}  {}".format(lista_pecas[index_peca_a_mover], posicao_do_teclado))
            #print(lista_pecas[index_peca_a_mover].get_nome())
            tabuleiro = Tabuleiro.movimento_rainha_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
            #return tabuleiro
        
        elif(peca_do_teclado == "Qb"):
            Tabuleiro.movimento_rainha_branco(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
            #print("ta vindo aqui?")
            #return tabuleiro
        elif(peca_do_teclado == "Rp"):
            Tabuleiro.movimento_rei_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
        
        elif(peca_do_teclado == "Rb"):
            Tabuleiro.movimento_rei_branco(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
#=> eu preciso ler a string da peça e converter em uma posição da lista
#eu preciso definir qual método será chamado a partir da peça selecionada
#preciso de alguma coisa que permita que o usuário cancele a seleção da peça e a selecione novamente
#Eu acho que preciso de um método "move_peça" genérico, aqui no Xadrez, que realiza leituras
#Tabuleiro.movimento_peao_preto(lista_pecas[4], "24", tabuleiro)
#objeto_tabuleiro = Tabuleiro()
Xadrez.mensagem_de_inicio()
jogo_acontecendo = True
#objeto_tabuleiro = Tabuleiro()
tabuleiro = Tabuleiro.cria_tabuleiro_normal()
lista_pecas = Peca.cria_pecas()
lista_pecas_string = Peca.cria_lista_pecas_string(lista_pecas)
Tabuleiro.inicializa_tabuleiro(tabuleiro, lista_pecas)
Tabuleiro.imprime_matriz(tabuleiro)

rodada = -1
ultimo_que_jogou = "b"
posicao_a_mover = "88"
peca_a_mover = "reset"

#print(teste)
#fazer tratamento de erro se Peça ou Posicao digitadas erradas

while(jogo_acontecendo == True):
    rodada = rodada + 1
    while(peca_a_mover not in lista_pecas_string):
        peca_a_mover = input("Qual peça você gostaria de mover?")
        if(rodada == 0):
            if(peca_a_mover in lista_pecas_string and peca_a_mover[1] == "b"):
                break
            else:
                print("Peça digitada incorretamente. Lembre-se que as BRANCAS começam o jogo. Tente de novo: ")
    
        elif(ultimo_que_jogou == "b"):
            if(peca_a_mover in lista_pecas_string and peca_a_mover[1] == "p"):
                ultimo_que_jogou = "p"
                break
        
            else: 
                print("Peça digitada incorretamente. Lembre-se que quem jogou por último foram as brancas! Tente de novo: ")
    
        elif(ultimo_que_jogou == "p"):
            if(peca_a_mover in lista_pecas_string and peca_a_mover[1] == ""):
                ultimo_que_jogou = "b"
                break
        
            else: 
                print("Peça digitada incorretamente. Lembre-se que quem jogou por último foram as brancas! Tente de novo: ")
    
    index_peca_a_mover = lista_pecas_string.index(peca_a_mover)
    
    
    while(int(posicao_a_mover[0]) < 0 or int(posicao_a_mover[0]) > 7 or int(posicao_a_mover[1]) < 0 or int(posicao_a_mover[1]) > 7 or len(posicao_a_mover) > 2):
        posicao_a_mover = input("Para qual posição você gostaria de mover essa peça?")
        if(posicao_a_mover.isdigit() == False):
            print("aqui?")
            posicao_a_mover = "88"
            continue
        if(int(posicao_a_mover[0]) < 0 or int(posicao_a_mover[0]) > 7 or int(posicao_a_mover[1]) < 0 or int(posicao_a_mover[1]) > 7 or len(posicao_a_mover) > 2):
            print("Posição digitada inexistente, tente de novo: ")


    Xadrez.qual_movimento_fazer(peca_a_mover, posicao_a_mover, tabuleiro, lista_pecas, index_peca_a_mover)
    
    #print("{}            {}".format(lista_pecas, lista_pecas_string))
    #print("depois do agora é pra cá que eu venho {}".format(lista_pecas[28].get_posicao()))
    #print("{}    {}".format(tabuleiro[2][3], tabuleiro[1][3]))
    Tabuleiro.imprime_matriz(tabuleiro)
    posicao_a_mover = "99"
    peca_a_mover = "reset"
    #se peça do tipo contrário comer o rei inimigo, gg
    for i in range(len(lista_pecas)):
        peca_tipo = lista_pecas[i].get_tipo()
        if(peca_tipo == "branco"):
            if(lista_pecas[i].get_posicao() == lista_pecas[30].get_posicao()):
                print("O REI PRETO CAIU!!!! O lado das peças brancas venceu!")
                jogo_acontecendo = False
                break
        
        elif(peca_tipo == "preto"):
            if(lista_pecas[i].get_posicao() == lista_pecas[31].get_posicao()):
                print("O REI BRANCO CAIU!!!! O lado das peças pretas venceu!")
                jogo_acontecendo = False
                break


