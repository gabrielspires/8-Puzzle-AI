#http://ozzmaker.com/add-colour-to-text-in-python/


import Pos # Facilitar a representação das posições (tuplas)
import numpy as np
import pprint as pp

class Tabuleiro(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabuleiro = np.arange(1,tamanho**2+1).reshape(tamanho, tamanho)
        self.tabuleiro[tamanho-1][tamanho-1] = 0
        self.vazio = Pos.ponto(tamanho-1, tamanho-1)
        
    
    def leTabuleiro(self, pecas):
        '''Lê o tabuleiro a partir de uma string com 
        os números separados por espaço'''
        self.tabuleiro = np.fromstring(pecas, dtype=int, sep=" ")
        self.tabuleiro = self.tabuleiro.reshape(self.tamanho, self.tamanho)
        x, y = np.where(self.tabuleiro == 0)
        self.vazio = Pos.ponto(int(x), int(y))
        
    def verificaTabuleiro(self):
        '''Verifica se a disposiçao passada do 
        tabuleiro é uma solução válida.'''
        answer = Tabuleiro(self.tamanho)
        return np.array_equal(answer.tabuleiro, self.tabuleiro)
    
    def trocaPeca(self, pos1, pos2):
        '''Troca duas pecas de posição'''
        aux = self.tabuleiro[pos1.x][pos1.y]
        self.tabuleiro[pos1.x][pos1.y] = self.tabuleiro[pos2.x][pos2.y]
        self.tabuleiro[pos2.x][pos2.y] = aux
    
    def cima(self):
        '''Movimenta o espaço em branco pra cima'''
        if self.vazio.x > 0:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x-1,self.vazio.y))
            self.vazio = Pos.ponto(self.vazio.x-1,self.vazio.y)
    
    def baixo(self):
        '''Movimenta o espaço em branco pra baixo'''
        if self.vazio.x < self.tamanho-1:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x+1,self.vazio.y))
            self.vazio = Pos.ponto(self.vazio.x+1,self.vazio.y)
    
    def esquerda(self):
        '''Movimenta o espaço em branco pra esquerda'''
        if self.vazio.y > 0:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x,self.vazio.y-1))
            self.vazio = Pos.ponto(self.vazio.x,self.vazio.y-1)
    
    def direita(self):
        '''Movimenta o espaço em branco pra direita'''
        if self.vazio.y < self.tamanho-1:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x,self.vazio.y+1))
            self.vazio = Pos.ponto(self.vazio.x,self.vazio.y+1)
    
    def moverPeca(self, direcao):
        '''Executa um movimento de acordo com o
        comando passado na sequencia'''
        if direcao == 'C': self.cima()
        if direcao == 'B': self.baixo()
        if direcao == 'D': self.direita()
        if direcao == 'E': self.esquerda()
    
    def leSequenciaMovimentos(self, sequencia):
        '''Lê uma sequência de movimentos a partir de uma string'''
        for direcao in sequencia:
            self.moverPeca(direcao)
    
    def mostraTabuleiro(self):
        for linha in self.tabuleiro:
            for peca in linha:
                if peca == 0: print("\033[0;33;40m",peca, end=" ")
                else: print("\033[0;47;40m",peca, end=" ")
            print("\033[0;47;40m")
        print("\033[0;47;40m")

a = Tabuleiro(3)
a.leTabuleiro("1 2 3 4 5 6 7 0 8")
print("Posição vazia:", a.vazio.x, a.vazio.y)
a.mostraTabuleiro()
# a.trocaPeca(Pos.ponto(1,1), Pos.ponto(0,1))
# a.mostraTabuleiro()
print(a.verificaTabuleiro())
a.direita()
a.mostraTabuleiro()
print(a.verificaTabuleiro())