import random
import numpy as np 
from Piece import Peca 
import sys

#falta: movimento do bispo branco. Rainha e Rei de ambas as cores.

#Depois, fazer a main e rodar o jogo

#Depois, mudanças e ajustes finais de todo tipo

class Tabuleiro:
    def __init__(self):
    #matriz como atributo
        pass#self.__matriz = self.cria_tabuleiro_normal()
    
    #get matriz
    #set matriz {método altera_matriz}
       
    

   
    def cria_tabuleiro_normal(): #cria a matriz na mão
        tabuleiro = [] #inicializa tabuleiro como lista vazia
        for i in range(8): #laço que criará os elementos do tabuleiro (cada linha = uma lista)
            linha = []
            for j in range(8): #esse for preenche cada uma das linhas com o numero de elementos (8, pq xadrez)
                linha.append("___") #o 0 é o valor default de preenchimento
                #print(linha)
            tabuleiro.append(linha) #a linha preenchida de zeros é adicionada ao tabuleiro como um elemento
        #Tabuleiro.imprime_matriz(tabuleiro) #chama o método que imprime a matriz tabuleiro de maneira adequada
        return tabuleiro        
            #a = len(tabuleiro)
            #print(linha)
            #print(a)
        #Tabuleiro.imprime_matriz(tabuleiro)
        #print(tabuleiro)
        
   #     for x in range(len(linha)):
    #        print(linha)
        #print(tabuleiro)

    @staticmethod
    def cria_tabuleiro_biblioteca(): #metodo para criar matriz usando import "numpy"
        tabuleiro = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        )
        #print(tabuleiro)
        #Tabuleiro.imprime_matriz(tabuleiro)
        return tabuleiro

#print(matriz)

    
    @staticmethod
    def imprime_matriz(matriz): #parâmetro é a matriz tabuleiro
        linha = [] #cria uma lista para receber as linhas do tabuleiro
        for x in range(len(matriz)): #o laço vai iterar até o tamanho da matriz (8 = 8 **linhas**, que sao os elementos)
            linha = matriz[x] #a minha lista recebe a linha (X) do tabuleiro
            print(linha) #printo a linha
            #print(tabuleiro)
    
    @staticmethod
    def altera_matriz(pos_antiga, peca, matriz): #recebe uma peca que mudou de posicao e altera o valor no tabuleiro
        #peca = Peca.get_posicao()
        #posicao é uma string pq recebe do teclado. "Valor_tipo" = tipo da peça que vai sobrescrever
        #posicao_str = input("Diga a posicao a ser movida a peça, de 00 ate 77")
        #print("to colando?")
        matriz[int(pos_antiga[0])][(int(pos_antiga[1]))] = "___"
        posicao = peca.get_posicao()
        valor_nome = peca.get_nome()
        #print("{}   {}".format(posicao, valor_nome))
        matriz[int(posicao[0])][int(posicao[1])] = valor_nome 
        #print(matriz[1][3])
        return matriz
        #Tabuleiro.imprime_matriz(matriz)
        #o valor que vai ser recebido é a legenda da peça ou *

    
    @staticmethod    
    def inicializa_tabuleiro(tabuleiro, lista_pecas):
        
        for i in range(32):
            tabuleiro = Tabuleiro.altera_matriz("44", lista_pecas[i], tabuleiro)
        return tabuleiro
    
    @staticmethod
    def inicializa_dicionario(self):
        dicionario = self.dicionario_posicoes_inciais_peoes(lista_pecas)
        return dicionario

    @staticmethod
    #o self aqui nesses métodos é na verdade uma lista_pecas
    def movimento_peao_preto(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        #print("to aqui mano?")
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        lista_duplicada = Peca.lista_pecas_inicial_duplicata()
        dicionario = self.dicionario_posicoes_iniciais_peoes(lista_duplicada)
        #print(dicionario)
        #my_dict = {"a": 1, "b": 2}

        if(posicao_antiga == dicionario[self.get_nome()]): #se peao na posicao inicial
            print(dicionario[self.get_nome()])
            if(posicao_coluna_antiga == int(nova_posicao[1]) and ((posicao_linha_antiga == int(nova_posicao[0]) - 1) or (posicao_linha_antiga == int(nova_posicao[0]) - 2))): #se uma ou duas para frente
                #print("aqui nao?")
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                return pos_antiga
            else:
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
        
        if(posicao_tabuleiro != "___"):
            #print("nao to aqui")
            if(posicao_tabuleiro[1] == "p"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
            #se peça for preta, movimento nao permitido
            elif(int(nova_posicao[0]) - 1 == posicao_linha_antiga and ((int(nova_posicao[1]) - 1 == posicao_coluna_antiga) or (int(nova_posicao[1]) + 1 == posicao_coluna_antiga))):
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                return pos_antiga
            else: 
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
        
        elif(int(nova_posicao[0]) - 1 == posicao_linha_antiga and int(nova_posicao[1]) == posicao_coluna_antiga):
            #print("to aqui mano?")
            pos_antiga = self.altera_posicao(self, nova_posicao)
            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
            return pos_antiga
        else: 
            #print("obvio que to aqui")
            #a = self.get_posicao()
            print("movimento não é permitido")
            #print(a)
            #print(posicao_antiga)
            return posicao_antiga
    
    @staticmethod
    def movimento_torre_preto(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        posicao_antiga = self.get_posicao()
        #print(posicao_antiga)
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "p"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
            #se peça for preta, movimento nao permitido
            #a seguir, condicao de movimento da torre
        if(int(nova_posicao[0]) == posicao_linha_antiga): #se mvto for na linha
            if(int(nova_posicao[1]) > posicao_coluna_antiga): #se mvto é para direita
                if (posicao_coluna_antiga + 1 == int(nova_posicao[1])):
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                    
                else:
                    for posicao in range(posicao_coluna_antiga, int(nova_posicao[1])): #for para checar as intermed
                        peca_na_posicao = matriz[posicao_linha_antiga][posicao]
                        if (peca_na_posicao == "___"): #se livre
                
            #for iterando] = "___" OK, else not ok
            #posicao_coluna_antiga = inicio
            #nova_posicao[1] = fim
            #tem que checar se as posicoes entre inicio e destino estão = "___"
            #or int[nova_posicao[1] == posicao_coluna_antiga] 
        #se a linha é igual, o mvto é na coluna, se a coluna é igual, o movimento é na linha
            #se tiver peça no caminho, movt nao permitido
            
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                    
                        elif(peca_na_posicao[1] == "b"):
                            self.set_posicao(peca_na_posicao)
                            print("Você comeu uma peça no meio do caminho")
                    
                        else: 
                            self.set_posicao(peca_na_posicao)
                            print("Movimento não permitido")

            elif(int(nova_posicao[1]) < posicao_coluna_antiga): #se mvto para esquerda
                if(posicao_coluna_antiga - 1 == int(nova_posicao[1])):
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                else:
                    for posicao in range(posicao_coluna_antiga, int(nova_posicao[1]), -1): #for para checar as intermed
                        peca_na_posicao2 = matriz[posicao_linha_antiga][posicao]
                        if (peca_na_posicao2 == "___"): #se possivel
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            matriz = Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                        
                        elif(peca_na_posicao2[1] == "b"):
                            self.set_posicao(peca_na_posicao)
                            print("Você comeu uma peça no meio do caminho")
                        
                        else: 
                            
                            self.set_posicao(posicao_antiga)
                            print("Movimento nao permitido")

        elif(int(nova_posicao[1]) == posicao_coluna_antiga): #se mvto for na coluna
            if(int(nova_posicao[0]) > posicao_linha_antiga): #se for para baixo
                #a = posicao_linha_antiga + 1 
                #print("aqui?{} vs {}".format(a, nova_posicao[0]))
                if(posicao_linha_antiga + 1 == int(nova_posicao[0])):
                    #print("e aqui?")
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    #print(self.get_posicao())
                    #print("ta voltando?")
                    teste = Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    #print("agoraAAAAAAAAA? {}".format(teste[1][3]))
                    return pos_antiga
                else:
                    #print("aqui????")
                    for posicao in range(posicao_linha_antiga, int(nova_posicao[0])):
                        peca_na_posicao3 = matriz[posicao][posicao_coluna_antiga] 
                        if (peca_na_posicao3 == "___"):
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                        
                        elif(peca_na_posicao3[1] == "b"):
                            self.set_posicao(peca_na_posicao)
                            print("Você comeu uma peça no meio do caminho")
                        
                        else: 
                            
                            self.set_posicao(posicao_antiga)
                            print("Movimento nao permitido")
            
            elif(int(nova_posicao[0]) < posicao_linha_antiga): #se para cima
                if(posicao_linha_antiga - 1 == int(nova_posicao[0])):
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                else:
                    for posicao in range(posicao_linha_antiga, int(nova_posicao[0]), -1): 
                        peca_na_posicao4 = matriz[posicao][posicao_coluna_antiga]
                        if (peca_na_posicao4 == "___"):
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
            
                        elif(peca_na_posicao4[1] == "b"):
                            self.set_posicao(peca_na_posicao)
                            print("Você comeu uma peça no meio do caminho")
                        
                        else: 
                            
                            self.set_posicao(posicao_antiga)
                            print("Movimento nao permitido")
        
    @staticmethod
    def movimento_cavalo_preto(self, nova_posicao, matriz):
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "p"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")  
        
        checa_mvt_cavalo_dupla_linha = int(nova_posicao[0]) + 2 == posicao_linha_antiga or int(nova_posicao[0]) - 2 == posicao_linha_antiga
        checa_mvt_cavalo_simples_linha = int(nova_posicao[0]) + 1 == posicao_linha_antiga or int(nova_posicao[0]) - 1 == posicao_linha_antiga
        checa_mvt_cavalo_dupla_coluna = int(nova_posicao[1]) + 2 == posicao_coluna_antiga or int(nova_posicao[1]) - 2 == posicao_coluna_antiga
        checa_mvt_cavalo_simples_coluna = int(nova_posicao[1]) + 1 == posicao_coluna_antiga or int(nova_posicao[1]) - 1 == posicao_coluna_antiga
        
        if((checa_mvt_cavalo_dupla_linha and checa_mvt_cavalo_simples_coluna) or (checa_mvt_cavalo_simples_linha and checa_mvt_cavalo_dupla_coluna)):
        #se a mvt do cavalo for dupla na linha deve ser simples na coluna e vice-versa
            pos_antiga = self.altera_posicao(self, nova_posicao)
            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
            return pos_antiga
               
        else:
            print("Movimento nao permitido")            
            
    @staticmethod
    def movimento_bispo_preto(self, nova_posicao, matriz):
        #check = False
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_linha_nova = int(nova_posicao[0])
        posicao_coluna_nova = int(nova_posicao[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "p"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitidoOoOo")
                #exit()  
        
        #bispo só se move na diagonal. A distância em uma direção deve ser igual à distância na outra
        
        if(abs(posicao_linha_antiga - posicao_linha_nova) != abs(posicao_coluna_antiga - posicao_coluna_nova)):
            self.set_posicao(posicao_antiga)
            print("Movimento não permitido!")
            #exit()
                    
        #tabuleiro = [] #inicializa tabuleiro como lista vazia
        #for i in range(8): #laço que criará os elementos do tabuleiro (cada linha = uma lista)
            #linha = []
            #for j in range(8): #esse for preenche cada uma das linhas com o numero de elementos (8, pq xadrez)
             #   linha.append("___") #o 0 é o valor default de preenchimento
                #print(linha)
            #abuleiro.append(linha) #a linha preenchida de zeros é adicionada ao tabuleiro como um elemento
        #Tabuleiro.imprime_matriz(tabuleiro) #chama o método que imprime a matriz tabuleiro de maneira adequada
        #return tabuleiro     
        #checar se o mvto pode ser feito, assim como no movt da torre
        
        #guardar as posicoes que devem ser checadas 
      
        #for posicao in range(posicao_coluna_antiga + 1, posicao_coluna_nova): #percorre colunas
                      
         #   coluna.append(posicao)
            
        #for posicao in range(posicao_linha_antiga + 1, posicao_linha_nova): #percorre linhas
         #   linha.append(posicao)

        step_bispo = abs(posicao_linha_antiga - posicao_linha_nova)
        #print(step_bispo)
        #se movimento é diagonal para baixo para a direita
        if(posicao_linha_nova > posicao_linha_antiga and posicao_coluna_nova > posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga + 1 + posicao][posicao_coluna_antiga + 1 + posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga

       # elif(peca_na_posicao[1] == "b"):
        #    pos_antiga = self.set_posicao(peca_na_posicao)
         #   Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
          #  print("Você comeu uma peça no meio do caminho")  
           # return pos_antiga

        #Se movimento é na diagonal para baixo para a esquerda     
        if(posicao_linha_nova > posicao_linha_antiga and posicao_coluna_nova < posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga + 1 + posicao][posicao_coluna_antiga - 1 - posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga

       # elif(peca_na_posicao[1] == "b"):
        #    pos_antiga = self.set_posicao(peca_na_posicao)
         #   Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
          #  print("Você comeu uma peça no meio do caminho")  
           # return pos_antiga
        
          #Se movimento é na diagonal para cima para a direita      
        if(posicao_linha_nova < posicao_linha_antiga and posicao_coluna_nova > posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga - 1 - posicao][posicao_coluna_antiga + 1 + posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga


        #Se movimento é na diagonal para cima para a esquerda      
        if(posicao_linha_nova < posicao_linha_antiga and posicao_coluna_nova < posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga - 1 - posicao][posicao_coluna_antiga - 1 - posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga


       # elif(peca_na_posicao[1] == "b"):
         #   pos_antiga = self.set_posicao(peca_na_posicao)
          #  Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
           # print("Você comeu uma peça no meio do caminho")  
           # return pos_antiga
                   
                  
        
           
                    
            #for iterando] = "___" OK, else not ok
            #posicao_coluna_antiga = inicio
            #nova_posicao[1] = fim
            #tem que checar se as posicoes entre inicio e destino estão = "___"
            #or int[nova_posicao[1] == posicao_coluna_antiga] 
        #se a linha é igual, o mvto é na coluna, se a coluna é igual, o movimento é na linha
            #se tiver peça no caminho, movt nao permitido
            
                    
    @staticmethod
    def movimento_rainha_preto(self, nova_posicao, matriz):
        #a rainha é torre + bispo. Se ela está em (x,y), ela pode, nas adjacencias, ir para: 
        #(x+1,y) / (x-1,y) / (x,y+1) / (x, y-1) / (x+1, y+1) / (x+1, y-1) / (x-1,y+1) / (x-1, y-1)
        #ideia: checa se mvto é "torre" ou "bispo". Se x ou y permanecerem = à pos_antiga, "torre"
        #elseif x e y != pos_antiga[0] e pos_antiga[1], "bispo".
        q_bispo = False
        q_torre = False 
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_linha_nova = int(nova_posicao[0])
        posicao_coluna_nova = int(nova_posicao[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "p"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
               # exit()  
        
        if(posicao_linha_antiga == posicao_linha_nova or posicao_coluna_antiga == posicao_coluna_nova):
            q_torre = True
            #print("aqui?????")
        elif(abs(posicao_linha_antiga - posicao_linha_nova) == abs(posicao_coluna_antiga - posicao_coluna_nova)): 
            q_bispo = True
            #print("ou aqui??")
        else:
            #print("é aqui né")
            self.set_posicao(posicao_antiga)
            print("Movimento nao permitido, certo?")
          #  exit()

        if(q_torre == True):
            q_torre = False
          #  print("eai?")
            #print("{}   {}  ".format(self.get_posicao(), nova_posicao))
            Tabuleiro.movimento_torre_preto(self, nova_posicao, matriz)
            #print("claro q volto pra cá, certo? {}".format(tabuleiro[1][3]))
            #return tabuleiro
        
        elif(q_bispo == True): 
            q_bispo = False
            print("Hdjaohjksfhja")
            Tabuleiro.movimento_bispo_preto(self, nova_posicao, matriz)

    @staticmethod
    def movimento_rei_preto(self, nova_posicao, matriz):
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_linha_nova = int(nova_posicao[0])
        posicao_coluna_nova = int(nova_posicao[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        
    #o rei pode se mover em qualquer uma das direções, mas apenas uma casa. É como se fosse bispo e torre
    #mas somente na condição de mover uma casa. Não há que testar se tem "peça" no caminho, tão somente
    #se a posicao para a qual o rei se move está livre
    #"nova_posicao" tem um conjunto de possibilidades = 
    #(x+1,y) / (x-1,y) / (x,y+1) / (x, y-1) / (x+1, y+1) / (x+1, y-1) / (x-1,y+1) / (x-1, y-1)
    #Entao: se nova_posicao == qualquer uma das possibilidades acima e se a casa a ir estiver livre, move
    #A checagem se está livre já está feita. O que se deve checar é se o movimento é possível

        #lista de espaços possiveis = 8: 
        lista_espacos_possiveis = []
        #possibilidades = 8
        espaco_possivel1 = str(abs(posicao_linha_antiga + 1))+str(posicao_coluna_antiga)
        espaco_possivel2 = str(abs(posicao_linha_antiga - 1))+str(posicao_coluna_antiga)
        espaco_possivel3 = str(posicao_linha_antiga)+str(abs(posicao_coluna_antiga + 1))
        espaco_possivel4 = str(posicao_linha_antiga)+str(abs(posicao_coluna_antiga - 1))
        espaco_possivel5 = str(abs(posicao_linha_antiga + 1))+str(abs(posicao_coluna_antiga + 1))
        espaco_possivel6 = str(abs(posicao_linha_antiga + 1))+str(abs(posicao_coluna_antiga - 1))
        espaco_possivel7 = str(abs(posicao_linha_antiga - 1))+str(abs(posicao_coluna_antiga + 1))
        espaco_possivel8 = str(abs(posicao_linha_antiga - 1))+str(abs(posicao_coluna_antiga - 1))

        #como automatizar tanto a primeira qto a segunda parte desse código?
        lista_espacos_possiveis.append(espaco_possivel1)
        lista_espacos_possiveis.append(espaco_possivel2)
        lista_espacos_possiveis.append(espaco_possivel3)
        lista_espacos_possiveis.append(espaco_possivel4)
        lista_espacos_possiveis.append(espaco_possivel5)
        lista_espacos_possiveis.append(espaco_possivel6)
        lista_espacos_possiveis.append(espaco_possivel7)
        lista_espacos_possiveis.append(espaco_possivel8)

        if(posicao_tabuleiro != "___"):
            #print("entro aqui?")
            if(posicao_tabuleiro[1] == "p"):
                print("e aqui?")
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
                lista_espacos_possiveis.clear()
                self.set_posicao(posicao_antiga)
                #print("Movimento nao permitido")
                #exit()  
 

            elif(nova_posicao in lista_espacos_possiveis):
                #print("quantas vezes eu entro aqui?")
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                lista_espacos_possiveis.clear()
                return pos_antiga
        
        elif(nova_posicao in lista_espacos_possiveis):
                #print("quantas vezes eu entro aqui?")
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                lista_espacos_possiveis.clear()
                return pos_antiga
                
        else:
            self.set_posicao(posicao_antiga)
            print("Movimento nao permitido")
            lista_espacos_possiveis.clear()
            self.set_posicao(posicao_antiga)
                            
            #exit()  



        #elif():


    @staticmethod
    def movimento_peao_branco(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        lista_duplicada = Peca.lista_pecas_inicial_duplicata()
        dicionario = self.dicionario_posicoes_iniciais_peoes(lista_duplicada)
        #print(dicionario)
        #my_dict = {"a": 1, "b": 2}

        if(posicao_antiga == dicionario[self.get_nome()]): #se peao na posicao inicial
            print(dicionario[self.get_nome()])
            if(posicao_coluna_antiga == int(nova_posicao[1]) and ((posicao_linha_antiga == int(nova_posicao[0]) + 1) or (posicao_linha_antiga == int(nova_posicao[0]) + 2))): #se uma ou duas para frente
                #print("aqui nao?")
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                return pos_antiga
            else:
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")

        
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "b"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")  
            elif(int(nova_posicao[0]) + 1 == posicao_linha_antiga and ((int(nova_posicao[1]) - 1 == posicao_coluna_antiga) or (int(nova_posicao[1]) + 1 == posicao_coluna_antiga))):
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                return pos_antiga
            else: 
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
        elif(int(nova_posicao[0]) + 1 == posicao_linha_antiga and int(nova_posicao[1]) == posicao_coluna_antiga):
            print("aqui?")
            pos_antiga = self.altera_posicao(self, nova_posicao)
            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
            return pos_antiga
        else: 
            #a = self.get_posicao()
            #print("movimento não é permitido")
            #print(a)
            #print(posicao_antiga)
            return posicao_antiga
        
    def cria_lista_pecas_mortas():
        pecas_mortas = []

    @staticmethod
    def movimento_torre_branco(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "b"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
            #se peça for preta, movimento nao permitido
            #a seguir, condicao de movimento da torre
        if(int(nova_posicao[0]) == posicao_linha_antiga): #se mvto for na linha
            if(int(nova_posicao[1]) > posicao_coluna_antiga): #se mvto é para a direita
                if (posicao_coluna_antiga + 1 == int(nova_posicao[1])):
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                else:
                    for posicao in range(posicao_coluna_antiga, int(nova_posicao[1])): #for para checar as intermed
                        if (matriz[posicao_linha_antiga][posicao] == "___"): #se livre
                    
                #for iterando] = "___" OK, else not ok
                #posicao_coluna_antiga = inicio
                #nova_posicao[1] = fim
                #tem que checar se as posicoes entre inicio e destino estão = "___"
                #or int[nova_posicao[1] == posicao_coluna_antiga] 
            #se a linha é igual, o mvto é na coluna, se a coluna é igual, o movimento é na linha
                #se tiver peça no caminho, movt nao permitido
                
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                    
            elif(int(nova_posicao[1]) < posicao_coluna_antiga): #se mvto para esquerda
                if(posicao_coluna_antiga - 1 == int(nova_posicao[1])):
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                else:
                    for posicao in range(posicao_coluna_antiga, int(nova_posicao[1]), -1): #for para checar as intermed
                        if (matriz[posicao_linha_antiga][posicao] == "___"): #se possivel
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                    
        elif(int(nova_posicao[1]) == posicao_coluna_antiga): #se mvto for na coluna
            if(int(nova_posicao[0]) > posicao_linha_antiga): #se for para baixo
                if(posicao_linha_antiga + 1 == int(nova_posicao[0])):
                    #print("e aqui?")
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                else:
                    for posicao in range(posicao_linha_antiga, int(nova_posicao[0])): 
                        if (matriz[posicao][posicao_coluna_antiga] == "___"):
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                
            elif(int(nova_posicao[0]) < posicao_linha_antiga): #se para cima
                #print("aqui?")
                if(posicao_linha_antiga - 1 == int(nova_posicao[0])):
                    #print("aqui")
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga
                else:
                    for posicao in range(posicao_linha_antiga, int(nova_posicao[0]), -1): 
                        if (matriz[posicao][posicao_coluna_antiga] == "___"):
                            pos_antiga = self.altera_posicao(self, nova_posicao)
                            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                            return pos_antiga
                        
    @staticmethod
    def movimento_cavalo_branco(self, nova_posicao, matriz):
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "b"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")  
        
        checa_mvt_cavalo_dupla_linha = int(nova_posicao[0]) + 2 == posicao_linha_antiga or int(nova_posicao[0]) - 2 == posicao_linha_antiga
        checa_mvt_cavalo_simples_linha = int(nova_posicao[0]) + 1 == posicao_linha_antiga or int(nova_posicao[0]) - 1 == posicao_linha_antiga
        checa_mvt_cavalo_dupla_coluna = int(nova_posicao[1]) + 2 == posicao_coluna_antiga or int(nova_posicao[1]) - 2 == posicao_coluna_antiga
        checa_mvt_cavalo_simples_coluna = int(nova_posicao[1]) + 1 == posicao_coluna_antiga or int(nova_posicao[1]) - 1 == posicao_coluna_antiga
        
        if((checa_mvt_cavalo_dupla_linha and checa_mvt_cavalo_simples_coluna) or (checa_mvt_cavalo_simples_linha and checa_mvt_cavalo_dupla_coluna)):
        #se a mvt do cavalo for dupla na linha deve ser simples na coluna e vice-versa
            pos_antiga = self.altera_posicao(self, nova_posicao)
            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
            return pos_antiga
            
    
        else:
            print("Movimento nao permitido")
    
    @staticmethod
    def movimento_bispo_branco(self, nova_posicao, matriz):
        #check = False
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_linha_nova = int(nova_posicao[0])
        posicao_coluna_nova = int(nova_posicao[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "b"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
             #   exit()  
        
        #bispo só se move na diagonal. A distância em uma direção deve ser igual à distância na outra
        
        if(abs(posicao_linha_antiga - posicao_linha_nova) != abs(posicao_coluna_antiga - posicao_coluna_nova)):
            self.set_posicao(posicao_antiga)
            print("Movimento não permitido!")
        #    exit()
                    
        #tabuleiro = [] #inicializa tabuleiro como lista vazia
        #for i in range(8): #laço que criará os elementos do tabuleiro (cada linha = uma lista)
            #linha = []
            #for j in range(8): #esse for preenche cada uma das linhas com o numero de elementos (8, pq xadrez)
             #   linha.append("___") #o 0 é o valor default de preenchimento
                #print(linha)
            #abuleiro.append(linha) #a linha preenchida de zeros é adicionada ao tabuleiro como um elemento
        #Tabuleiro.imprime_matriz(tabuleiro) #chama o método que imprime a matriz tabuleiro de maneira adequada
        #return tabuleiro     
        #checar se o mvto pode ser feito, assim como no movt da torre
        
        #guardar as posicoes que devem ser checadas 
      
        #for posicao in range(posicao_coluna_antiga + 1, posicao_coluna_nova): #percorre colunas
                      
         #   coluna.append(posicao)
            
        #for posicao in range(posicao_linha_antiga + 1, posicao_linha_nova): #percorre linhas
         #   linha.append(posicao)

        step_bispo = abs(posicao_linha_antiga - posicao_linha_nova)
        #print(step_bispo)
        #se movimento é diagonal para baixo para a direita
        if(posicao_linha_nova > posicao_linha_antiga and posicao_coluna_nova > posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga + 1 + posicao][posicao_coluna_antiga + 1 + posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga

       # elif(peca_na_posicao[1] == "b"):
        #    pos_antiga = self.set_posicao(peca_na_posicao)
         #   Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
          #  print("Você comeu uma peça no meio do caminho")  
           # return pos_antiga

        #Se movimento é na diagonal para baixo para a esquerda     
        if(posicao_linha_nova > posicao_linha_antiga and posicao_coluna_nova < posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga + 1 + posicao][posicao_coluna_antiga - 1 - posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga

       # elif(peca_na_posicao[1] == "b"):
        #    pos_antiga = self.set_posicao(peca_na_posicao)
         #   Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
          #  print("Você comeu uma peça no meio do caminho")  
           # return pos_antiga
        
          #Se movimento é na diagonal para cima para a direita      
        if(posicao_linha_nova < posicao_linha_antiga and posicao_coluna_nova > posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga - 1 - posicao][posicao_coluna_antiga + 1 + posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga


        #Se movimento é na diagonal para cima para a esquerda      
        if(posicao_linha_nova < posicao_linha_antiga and posicao_coluna_nova < posicao_coluna_antiga):
            for posicao in range(0, step_bispo): #concatena em uma lista
                peca_na_posicao = matriz[posicao_linha_antiga - 1 - posicao][posicao_coluna_antiga - 1 - posicao]
                #print("OLHA AQUI{}".format(peca_na_posicao))
                if(peca_na_posicao) == "___": #check posicoes mvt bispo
                    pos_antiga = self.altera_posicao(self, nova_posicao)
                    Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                    return pos_antiga


       # elif(peca_na_posicao[1] == "b"):
         #   pos_antiga = self.set_posicao(peca_na_posicao)
          #  Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
           # print("Você comeu uma peça no meio do caminho")  
           # return pos_antiga
                   
                  
        
           
                    
            #for iterando] = "___" OK, else not ok
            #posicao_coluna_antiga = inicio
            #nova_posicao[1] = fim
            #tem que checar se as posicoes entre inicio e destino estão = "___"
            #or int[nova_posicao[1] == posicao_coluna_antiga] 
        #se a linha é igual, o mvto é na coluna, se a coluna é igual, o movimento é na linha
            #se tiver peça no caminho, movt nao permitido
            
                    
    @staticmethod
    def movimento_rainha_branco(self, nova_posicao, matriz):
        #a rainha é torre + bispo. Se ela está em (x,y), ela pode, nas adjacencias, ir para: 
        #(x+1,y) / (x-1,y) / (x,y+1) / (x, y-1) / (x+1, y+1) / (x+1, y-1) / (x-1,y+1) / (x-1, y-1)
        #ideia: checa se mvto é "torre" ou "bispo". Se x ou y permanecerem = à pos_antiga, "torre"
        #elseif x e y != pos_antiga[0] e pos_antiga[1], "bispo".
        q_bispo = False
        q_torre = False 
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_linha_nova = int(nova_posicao[0])
        posicao_coluna_nova = int(nova_posicao[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
            if(posicao_tabuleiro[1] == "p"):
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitidoOoOo")
              #  exit()  
        
        if(posicao_linha_antiga == posicao_linha_nova or posicao_coluna_antiga == posicao_coluna_nova):
            q_torre = True
        elif(abs(posicao_linha_antiga - posicao_linha_nova) == abs(posicao_coluna_antiga - posicao_coluna_nova)): 
            q_bispo = True
        else: 
            self.set_posicao(posicao_antiga)
            print("Movimento nao permitido")
            #exit()

        if(q_torre == True):
            q_torre = False
            Tabuleiro.movimento_torre_branco(self, nova_posicao, matriz)
        elif(q_bispo == True): 
            q_bispo = False
            Tabuleiro.movimento_bispo_branco(self, nova_posicao, matriz)
            
    @staticmethod
    def movimento_rei_branco(self, nova_posicao, matriz):
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_linha_nova = int(nova_posicao[0])
        posicao_coluna_nova = int(nova_posicao[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        
    #o rei pode se mover em qualquer uma das direções, mas apenas uma casa. É como se fosse bispo e torre
    #mas somente na condição de mover uma casa. Não há que testar se tem "peça" no caminho, tão somente
    #se a posicao para a qual o rei se move está livre
    #"nova_posicao" tem um conjunto de possibilidades = 
    #(x+1,y) / (x-1,y) / (x,y+1) / (x, y-1) / (x+1, y+1) / (x+1, y-1) / (x-1,y+1) / (x-1, y-1)
    #Entao: se nova_posicao == qualquer uma das possibilidades acima e se a casa a ir estiver livre, move
    #A checagem se está livre já está feita. O que se deve checar é se o movimento é possível

        #lista de espaços possiveis = 8: 
        lista_espacos_possiveis = []
        #possibilidades = 8
        espaco_possivel1 = str(abs(posicao_linha_antiga + 1))+str(posicao_coluna_antiga)
        espaco_possivel2 = str(abs(posicao_linha_antiga - 1))+str(posicao_coluna_antiga)
        espaco_possivel3 = str(posicao_linha_antiga)+str(abs(posicao_coluna_antiga + 1))
        espaco_possivel4 = str(posicao_linha_antiga)+str(abs(posicao_coluna_antiga - 1))
        espaco_possivel5 = str(abs(posicao_linha_antiga + 1))+str(abs(posicao_coluna_antiga + 1))
        espaco_possivel6 = str(abs(posicao_linha_antiga + 1))+str(abs(posicao_coluna_antiga - 1))
        espaco_possivel7 = str(abs(posicao_linha_antiga - 1))+str(abs(posicao_coluna_antiga + 1))
        espaco_possivel8 = str(abs(posicao_linha_antiga - 1))+str(abs(posicao_coluna_antiga - 1))

        #como automatizar tanto a primeira qto a segunda parte desse código?
        lista_espacos_possiveis.append(espaco_possivel1)
        lista_espacos_possiveis.append(espaco_possivel2)
        lista_espacos_possiveis.append(espaco_possivel3)
        lista_espacos_possiveis.append(espaco_possivel4)
        lista_espacos_possiveis.append(espaco_possivel5)
        lista_espacos_possiveis.append(espaco_possivel6)
        lista_espacos_possiveis.append(espaco_possivel7)
        lista_espacos_possiveis.append(espaco_possivel8)

        if(posicao_tabuleiro != "___"):
            #print("entro aqui?")
            if(posicao_tabuleiro[1] == "p"):
                print("e aqui?")
                self.set_posicao(posicao_antiga)
                print("Movimento nao permitido")
                lista_espacos_possiveis.clear()
                #exit()  
 

            elif(nova_posicao in lista_espacos_possiveis):
                print("quantas vezes eu entro aqui?")
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                lista_espacos_possiveis.clear()
                return pos_antiga
        
        elif(nova_posicao in lista_espacos_possiveis):
                #print("quantas vezes eu entro aqui?")
                pos_antiga = self.altera_posicao(self, nova_posicao)
                Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                lista_espacos_possiveis.clear()
                return pos_antiga
                
        else:
            self.set_posicao(posicao_antiga)
            print("Movimento nao permitido")
            lista_espacos_possiveis.clear()
            #exit()  



        #elif():

#tabuleiro = Tabuleiro.cria_tabuleiro_normal()
#pecas_mortas = Tabuleiro.cria_lista_pecas_mortas
#lista_pecas = Peca.cria_pecas()
#input("Qual peça você quer mover?")

#for i in range(len(lista_pecas)):
    #a = lista_pecas.index(lista_pecas[i].get_nome())
    #print(a)
#print(a)
#Tabuleiro.inicializa_tabuleiro(tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#print("\n\n\n")
#Tabuleiro.movimento_peao_preto(lista_pecas[2], "32", tabuleiro)
#Tabuleiro.movimento_peao_branco(lista_pecas[9], "41", tabuleiro)
#Tabuleiro.movimento_peao_preto(lista_pecas[0], "41", tabuleiro)
#Tabuleiro.movimento_rei_preto(lista_pecas[30], "54", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#print("\n\n\n{}     {}".format(lista_pecas[0].get_posicao(), lista_pecas[9].get_posicao()))
#print(lista_pecas[30].get_posicao())
#Tabuleiro.movimento_rei_preto(lista_pecas[30], "65", tabuleiro)
#print(lista_pecas[30].get_posicao())
#Tabuleiro.movimento_cavalo_preto(lista_pecas[20], "22", tabuleiro)

#Tabuleiro.movimento_cavalo_preto(lista_pecas[22], "52", tabuleiro)
#Tabuleiro.movimento_peao_preto(lista_pecas[3], "23", tabuleiro)
#Tabuleiro.movimento_rainha_preto(lista_pecas[28], "12", tabuleiro)
#Tabuleiro.movimento_rainha_preto(lista_pecas[28], "67", tabuleiro)
#Tabuleiro.movimento_peao_preto(lista_pecas[0], "20", tabuleiro)
#Tabuleiro.movimento_torre_preto(lista_pecas[16], "10", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#print("\n\n\n")
#Tabuleiro.movimento_peao_branco(lista_pecas[11], "53", tabuleiro)
#Tabuleiro.movimento_rainha_branco(lista_pecas[29], "63", tabuleiro)
#Tabuleiro.movimento_rainha_branco(lista_pecas[29], "31", tabuleiro)
#Tabuleiro.movimento_bispo_branco(lista_pecas[26], "61", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_bispo_preto(lista_pecas[24], "13", tabuleiro)
#print("\n\n\n")
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_bispo_preto(lista_pecas[24], "31", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_bispo_preto(lista_pecas[24], "20", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_bispo_preto(lista_pecas[24], "11", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_bispo_preto(lista_pecas[24], "55", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_bispo_preto(lista_pecas[24], "23", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)

#Tabuleiro.movimento_cavalo_preto(lista_pecas[20], "70", tabuleiro)
#print("\n\n\n")
#Tabuleiro.imprime_matriz(tabuleiro)

#pt = Tabuleiro.movimento_torre_preto(lista_pecas[16], "60", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#print("\n\n\n")
#pt = Tabuleiro.movimento_torre_preto(lista_pecas[16], "20", tabuleiro)
#print(lista_pecas[16].get_posicao())
#Tabuleiro.imprime_matriz(tabuleiro)
#pos_antiga = Peca.movimento_peao_branco(lista_pecas[8], "50")
#pos_antiga = Tabuleiro.movimento_peao_preto(lista_pecas[0], "21", tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#print(lista_pecas[14].get_tipo())
#print(lista_pecas[14].get_posicao())
#pa = Tabuleiro.movimento_peao_branco(lista_pecas[14], "57", tabuleiro)
#print(lista_pecas[9].get_posicao())
#Tabuleiro.altera_matriz(pos_antiga, lista_pecas[8], tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#tabuleiro = Tabuleiro()
#tabuleiro_de_jogo = Tabuleiro.cria_tabuleiro_normal()
#Tabuleiro.imprime_matriz(tabuleiro_de_jogo)
#Tabuleiro.altera_matriz(tabuleiro_de_jogo, "55", "10")
#print("\n\n\n")
#Tabuleiro.imprime_matriz(tabuleiro_de_jogo)
#print(a[0][0])
#a[0][0] = 10
#print(a[0][0])
#Tabuleiro.cria_tabuleiro_biblioteca()