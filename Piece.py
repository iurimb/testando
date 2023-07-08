#from Board import Tabuleiro 

class Peca:
    def __init__(self, nome, posicao, tipo):
        self.__nome = nome
        self.__posicao = posicao
        self.__tipo = tipo

    def get_nome(self):
        return self.__nome
    
    def get_posicao(self):
        return self.__posicao
    
    def get_tipo(self):
        return self.__tipo
    
    def set_posicao(self, posicao):
        self.__posicao = posicao

    pecas_mortas = [] #lista de peças mortas, variavel global da classe

    #eu vou ter um método para criar todas as peças, gravar em uma lista e aí passar pra arrumar o tabuleiro
    

        #peoes pretos e brancos; torres pretas e brancas; cavalos pretos e brancos; 
        #bispos pretos e brancos; rei preto e branco; rainha preta e branca
    def cria_pecas():
        #peoes
        Pp1 = Peca("Pp1", "10", "preto") #peao preto 1 [0...7] = [Pp1...Pp8]
        Pp2 = Peca("Pp2", "11", "preto") #peao preto 2
        Pp3 = Peca("Pp3", "12", "preto") #peao preto 3
        Pp4 = Peca("Pp4", "23", "preto") #peao preto 4
        Pp5 = Peca("Pp5", "14", "preto") #peao preto 5
        Pp6 = Peca("Pp6", "15", "preto") #peao preto 6
        Pp7 = Peca("Pp7", "16", "preto") #peao preto 7
        Pp8 = Peca("Pp8", "17", "preto") #peao preto 8

        Pb1 = Peca("Pb1", "60", "branco") #peao branco 1 [8...15] = Pb1...Pb8]
        Pb2 = Peca("Pb2", "61", "branco") #peao branco 2
        Pb3 = Peca("Pb3", "62", "branco") #peao branco 3
        Pb4 = Peca("Pb4", "63", "branco") #PB4...
        Pb5 = Peca("Pb5", "64", "branco") 
        Pb6 = Peca("Pb6", "65", "branco") 
        Pb7 = Peca("Pb7", "66", "branco") 
        Pb8 = Peca("Pb8", "67", "branco") 

        #torres

        Tp1 = Peca("Tp1", "00", "preto") #torre preta 1 [16-17] Tp1-Tp2
        Tp2 = Peca("Tp2", "07", "preto") #torre preta 2 

        Tb1 = Peca("Tb1", "70", "branco") #torre branca 1 [18-19] Tb1-Tb2
        Tb2 = Peca("Tb2", "77", "branco") #torre branca 2

        #cavalos

        Cp1 = Peca("Cp1", "01", "preto") #[20-21] Cp1-Cp2
        Cp2 = Peca("Cp2", "06", "preto")

        Cb1 = Peca("Cb1", "71", "branco") #[22-23] Cb1-Cb2
        Cb2 = Peca("Cb2", "76", "branco")
        
        #bispos

        Bp1 = Peca("Bp1", "02", "preto") #[24-25] Bp1-Bp2
        Bp2 = Peca("Bp2", "05", "preto") 

        Bb1 = Peca("Bb1", "72", "branco") #[26-27] Bb1-Bb2
        Bb2 = Peca("Bb2", "75", "branco")

        #Rainhas

        Qp = Peca("Qp", "03", "preto") #28 QP
        Qb = Peca("Qb", "73", "branco") #29 QB

        #Reis

        Rp = Peca("Rp", "04", "preto") #30 RP
        Rb = Peca("Rb", "22", "branco") #31 RB

        lista_pecas = [Pp1, Pp2, Pp3, Pp4, Pp5, Pp6, Pp7, Pp8, Pb1, Pb2, Pb3, Pb4, Pb5, Pb6, Pb7, Pb8, Tp1, Tp2, Tb1, Tb2, Cp1, Cp2, Cb1, Cb2, Bp1, Bp2, Bb1, Bb2, Qp, Qb, Rp, Rb]

        return lista_pecas
    
    @staticmethod
    def lista_pecas_inicial_duplicata():
        lista_duplicada = Peca.cria_pecas()
        return lista_duplicada

    @staticmethod 
    def dicionario_posicoes_iniciais_peoes(lista_duplicada):
        lista_pecas_string = Peca.cria_lista_pecas_string(lista_duplicada)
        lista_peoes_string = lista_pecas_string[0:16]
        #print(lista_peoes_string[0])
        #print(lista_peoes_string[1])
        dicionario_posicoes_iniciais_peoes = {}
        #print(lista_peoes_string)
        for i in range (len(lista_peoes_string)): #cria o dicionario
            string_peao = lista_peoes_string[i]
            dicionario_simples = {string_peao: lista_duplicada[i].get_posicao()}
            #dicionario_simples = dict(a=lista_pecas[i].get_posicao()) 
            #o dict imprime literalmente o que está antes do "=", não recebe "parametrizacao"
            #print(dicionario_simples)
            #print(dicionario_simples)
            dicionario_posicoes_iniciais_peoes.update(dicionario_simples)
        return dicionario_posicoes_iniciais_peoes
        #print(dicionario_posicoes_peoes)
        #print(dicionario_posicoes_peoes)
        #recebe um dicionario: peao X -> posicao inicial Y        

    @staticmethod
    def cria_lista_pecas_string(lista_pecas):
        lista_pecas_string = []
        for i in range(len(lista_pecas)):
        
            lista_pecas_string.append(lista_pecas[i].get_nome())
            #print(lista_pecas_string[i])
        return lista_pecas_string
        #print(lista_pecas_string)    

    #metodos de movimento para cada peça
    #metodos de checagem de movimento
    #precisa de uma classe jogador? Qq o jogador faz? ele movimenta as peças. 
    #Mas "movimentar as peças" = alterar posicao das peças + modificacao do tabuleiro
    
   
       
    
    #def altera_ao_comer_pecas(self, peca2):
        #self.set_posicao(peca2.get_posicao())
        #pecas_mortas.append(peca2)


    @staticmethod
    def altera_posicao(self, nova_posicao):
        posicao_antiga = self.get_posicao()
        print(nova_posicao)
        self.set_posicao(nova_posicao)
        #posicao = self.get_posicao()
        #print(posicao)
        #print(newpos)

        return posicao_antiga
        #define a movimentação dos peoes. Um peão, a principio, pode apenas se mover uma casa para frente. 
        #1a condição: se peao for branco, 
lista_pecas = Peca.cria_pecas()
Peca.cria_lista_pecas_string(lista_pecas)
Peca.dicionario_posicoes_iniciais_peoes(lista_pecas)

#def inicializa_tabuleiro(tabuleiro):
  #  for i in range(32):
    #    tabuleiro = Tabuleiro.altera_matriz(tabuleiro, lista_pecas[i].get_tipo(), lista_pecas[i].get_posicao())
    #return tabuleiro

#tabuleiro_inicial = Tabuleiro.cria_tabuleiro_normal()
#lista_pecas = Peca.cria_pecas()
#tabuleiro = inicializa_tabuleiro(tabuleiro_inicial)

#print("\n\n\n")

#Tabuleiro.imprime_matriz(tabuleiro)
#Tabuleiro.imprime_matriz(tabuleiro)
#print("\n\n\n")

#Tabuleiro.imprime_matriz(tabuleiro)
#a = peca.get_posicao()
#print(a)
#b = peca.get_tipo()
#print(b)
#peca.set_posicao(77)
#a = peca.get_posicao()
#print(a)