import random
import numpy as np 
from Piece import Peca 


class Tabuleiro:
    def __init__(self):
        pass
    
    

    @staticmethod
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
        matriz[int(pos_antiga[0])][(int(pos_antiga[1]))] = "___"
        posicao = peca.get_posicao()
        valor_nome = peca.get_nome()
        matriz[int(posicao[0])][(int(posicao[1]))] = valor_nome 
        return matriz
        #Tabuleiro.imprime_matriz(matriz)
        #o valor que vai ser recebido é a legenda da peça ou *

    @staticmethod    
    def inicializa_tabuleiro(tabuleiro):
        
        for i in range(32):
            tabuleiro = Tabuleiro.altera_matriz("44", lista_pecas[i], tabuleiro)
        return tabuleiro

    @staticmethod
    def movimento_peao_preto(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
        if(posicao_tabuleiro != "___"):
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
        elif(int(nova_posicao[0]) - 1 == int(posicao_linha_antiga)):
            pos_antiga = self.altera_posicao(self, nova_posicao)
            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
            return pos_antiga
        else: 
            a = self.get_posicao()
            print("movimento não é permitido", a)
            #print(a)
            #print(posicao_antiga)
            return posicao_antiga
    
    @staticmethod
    def movimento_torre_preto(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        posicao_antiga = self.get_posicao()
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
            if(int(nova_posicao[1]) > posicao_coluna_antiga): #se mvto é para a direita
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
                for posicao in range(posicao_coluna_antiga, int(nova_posicao[1]), -1): #for para checar as intermed
                    if (matriz[posicao_linha_antiga][posicao] == "___"): #se possivel
                        pos_antiga = self.altera_posicao(self, nova_posicao)
                        Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                        return pos_antiga
                    
        elif(int(nova_posicao[1]) == posicao_coluna_antiga): #se mvto for na coluna
            if(int(nova_posicao[0]) > posicao_linha_antiga): #se for para baixo
                for posicao in range(posicao_linha_antiga, int(nova_posicao[0])): 
                    if (matriz[posicao][posicao_coluna_antiga] == "___"):
                        pos_antiga = self.altera_posicao(self, nova_posicao)
                        Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                        return pos_antiga
            
            elif(int(nova_posicao[0]) < posicao_linha_antiga):
                for posicao in range(posicao_linha_antiga, int(nova_posicao[0]), -1): 
                    if (matriz[posicao][posicao_coluna_antiga] == "___"):
                        pos_antiga = self.altera_posicao(self, nova_posicao)
                        Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                        return pos_antiga
        else: 
            self.set_posicao(posicao_antiga)
            print("Movimento nao permitido")
       
    
    @staticmethod
    def movimento_peao_branco(self, nova_posicao, matriz):
        #se a nova_posicao for possivel, altera_posicao(), else: "movimento n permitido"
        posicao_antiga = self.get_posicao()
        posicao_linha_antiga = int(posicao_antiga[0])
        posicao_coluna_antiga = int(posicao_antiga[1])
        posicao_tabuleiro = matriz[int(nova_posicao[0])][int(nova_posicao[1])] 
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
        elif(int(nova_posicao[0]) + 1 == int(posicao_linha_antiga)):
            pos_antiga = self.altera_posicao(self, nova_posicao)
            Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
            return pos_antiga
        else: 
            a = self.get_posicao()
            print("movimento não é permitido", a)
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
                for posicao in range(posicao_coluna_antiga, int(nova_posicao[1]), -1): #for para checar as intermed
                    if (matriz[posicao_linha_antiga][posicao] == "___"): #se possivel
                        pos_antiga = self.altera_posicao(self, nova_posicao)
                        Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                        return pos_antiga
                    
        elif(int(nova_posicao[1]) == posicao_coluna_antiga): #se mvto for na coluna
            if(int(nova_posicao[0]) > posicao_linha_antiga): #se for para baixo
                for posicao in range(posicao_linha_antiga, int(nova_posicao[0])): 
                    if (matriz[posicao][posicao_coluna_antiga] == "___"):
                        pos_antiga = self.altera_posicao(self, nova_posicao)
                        Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                        return pos_antiga
            
            elif(int(nova_posicao[0]) < posicao_linha_antiga):
                for posicao in range(posicao_linha_antiga, int(nova_posicao[0]), -1): 
                    if (matriz[posicao][posicao_coluna_antiga] == "___"):
                        pos_antiga = self.altera_posicao(self, nova_posicao)
                        Tabuleiro.altera_matriz(posicao_antiga, self, matriz)
                        return pos_antiga

tabuleiro = Tabuleiro.cria_tabuleiro_normal()
pecas_mortas = Tabuleiro.cria_lista_pecas_mortas
lista_pecas = Peca.cria_pecas()[:]
Tabuleiro.inicializa_tabuleiro(tabuleiro)
Tabuleiro.imprime_matriz(tabuleiro)
print("\n\n\n")
pt = Tabuleiro.movimento_torre_preto(lista_pecas[16], "60", tabuleiro)
Tabuleiro.imprime_matriz(tabuleiro)
print("\n\n\n")
pt = Tabuleiro.movimento_torre_preto(lista_pecas[16], "20", tabuleiro)
print(lista_pecas[16].get_posicao())
Tabuleiro.imprime_matriz(tabuleiro)
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