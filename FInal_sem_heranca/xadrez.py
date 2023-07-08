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
    def qual_movimento_fazer(peca_do_teclado, posicao_do_teclado, lista_pecas, index_peca_a_mover):
        tipo_da_peca = peca_do_teclado[:2]
        indice_fez_movimento = 0
        if(tipo_da_peca == "Pp"):
            #print("{}  {}").format(lista_pecas[index_peca_a_mover], posicao_do_teclado)
            #tabuleiro = objeto_tabuleiro.movimento_peao_preto(lista_pecas[index_peca_a_mover], posicao_do_teclado, tabuleiro)
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_peao_preto(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
            #print("ta vindo aqui?")
            #return tabuleiro
        elif(tipo_da_peca == "Pb"): 
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_peao_branco(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
            #return tabuleiro
        
        elif(tipo_da_peca == "Tp"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_torre_preto(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(tipo_da_peca == "Tb"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_torre_branco(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(tipo_da_peca == "Cp"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_cavalo_preto(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(tipo_da_peca == "Cb"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_cavalo_branco(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(tipo_da_peca == "Bp"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_bispo_preto(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(tipo_da_peca == "Bb"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_bispo_branco(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(peca_do_teclado == "Qp"):
            #print("{}  {}".format(lista_pecas[index_peca_a_mover], posicao_do_teclado))
            #print(lista_pecas[index_peca_a_mover].get_nome())
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_rainha_preto(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
            #return tabuleiro
        
        elif(peca_do_teclado == "Qb"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_rainha_branco(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
            #print("ta vindo aqui?")
            #return tabuleiro
        elif(peca_do_teclado == "Rp"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_rei_preto(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
        elif(peca_do_teclado == "Rb"):
            pos_antiga = lista_pecas[index_peca_a_mover].get_posicao()
            objeto_tabuleiro.movimento_rei_branco(posicao_do_teclado, lista_pecas[index_peca_a_mover])
            if(lista_pecas[index_peca_a_mover].get_posicao() == pos_antiga): #se a posicao nova = antiga
                indice_fez_movimento = 0
            else: indice_fez_movimento = 1
            return indice_fez_movimento
        
#=> eu preciso ler a string da peça e converter em uma posição da lista
#eu preciso definir qual método será chamado a partir da peça selecionada
#preciso de alguma coisa que permita que o usuário cancele a seleção da peça e a selecione novamente
#Eu acho que preciso de um método "move_peça" genérico, aqui no Xadrez, que realiza leituras
#Tabuleiro.movimento_peao_preto(lista_pecas[4], "24", tabuleiro)

Xadrez.mensagem_de_inicio()
jogo_acontecendo = True
#objeto_tabuleiro = Tabuleiro()
#Tabuleiro.cria_tabuleiro_normal()
matriz = Tabuleiro.cria_tabuleiro_normal()
objeto_tabuleiro = Tabuleiro(matriz)
lista_pecas = Peca.cria_pecas()
lista_pecas_string = Peca.cria_lista_pecas_string(lista_pecas)
objeto_tabuleiro.inicializa_tabuleiro(lista_pecas)
objeto_tabuleiro.imprime_matriz()
dicionario_tabuleiro = objeto_tabuleiro.cria_hash_de_posicoes()

rodada = -1
ultimo_que_jogou = "b"
posicao_do_teclado = "reset"
peca_a_mover = "reset"

#print(teste)
#fazer tratamento de erro se Peça ou Posicao digitadas erradas

while(jogo_acontecendo == True):
    rodada = rodada + 1
    while(peca_a_mover.strip() not in lista_pecas_string):
        peca_a_mover = input("Qual peça você gostaria de mover?")
        if(rodada == 0):
            if(peca_a_mover.strip() in lista_pecas_string and peca_a_mover[1] == "b"):
                break
            else:
                peca_a_mover = "reset"
                print("Peça digitada incorretamente. Lembre-se que as BRANCAS começam o jogo. Tente de novo: ")
    
        elif(ultimo_que_jogou == "b"):
            if(peca_a_mover.strip() in lista_pecas_string and peca_a_mover[1] == "p"):
                ultimo_que_jogou = "p"
                break
        
            else: 
                peca_a_mover = "reset"
                print("Peça digitada incorretamente. Lembre-se que quem jogou por último foram as brancas! Tente de novo: ")
                continue

        elif(ultimo_que_jogou == "p"):
            if(peca_a_mover.strip() in lista_pecas_string and peca_a_mover[1] == "b"):
                ultimo_que_jogou = "b"
                break
        
            else: 
                peca_a_mover = "reset"
                print("Peça digitada incorretamente. Lembre-se que quem jogou por último foram as brancas! Tente de novo: ")
                continue
            
    index_peca_a_mover = lista_pecas_string.index(peca_a_mover.strip())
    
    
    #se a posicao digitada está em dicionario, OK, se não, fica pedindo
    while(posicao_do_teclado not in dicionario_tabuleiro):
        posicao_do_teclado = input("Para qual posição você gostaria de mover essa peça?")
        if(posicao_do_teclado not in dicionario_tabuleiro):
            print("Posição digitada inexistente, tente de novo: ")
            continue
        else:
            posicao_a_mover = dicionario_tabuleiro[posicao_do_teclado] #recebe a posicao que a chave aponta
            

    deu_boa_movimento = Xadrez.qual_movimento_fazer(peca_a_mover.strip(), posicao_a_mover, lista_pecas, index_peca_a_mover)
    if(deu_boa_movimento == 0):
        if(ultimo_que_jogou == "b"):
            ultimo_que_jogou = "p"
        elif(ultimo_que_jogou == "p"):
            ultimo_que_jogou = "b"
    #print("{}            {}".format(lista_pecas, lista_pecas_string))
    #print("depois do agora é pra cá que eu venho {}".format(lista_pecas[28].get_posicao()))
    #print("{}    {}".format(tabuleiro[2][3], tabuleiro[1][3]))
    #print(deu_boa_movimento)
    objeto_tabuleiro.imprime_matriz()
    posicao_do_teclado = "reset"
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


