import Pos # Facilitar a representação das posições (tuplas)
import numpy as np

class Tabuleiro(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabuleiro = np.arange(1,tamanho**2+1).reshape(tamanho, tamanho)
        self.tabuleiro[tamanho-1][tamanho-1] = 0
        self.vazio = Pos.ponto(tamanho-1, tamanho-1)
        
    
    def leTabuleiro(self, pecas):
        '''Lê o tabuleiro a partir de uma string com 
        os números separados por espaço'''
        p = pecas.split(" ")
                
    
    def verificaTabuleiro(self):
        '''Verifica se a disposiçao passada do 
        tabuleiro é uma solução válida.'''
        pass
    
    def trocaPeca(self, pos1, pos2):
        '''Movimenta uma peça para o espaço vazio,
        ou seja, troca a peça de posição com o
        espaço vazio do tabuleiro.'''
        pass
    
    def cima(self):
        '''Movimenta o espaço em branco pra cima'''
        pass
    
    def baixo(self):
        '''Movimenta o espaço em branco pra baixo'''
        pass
    
    def esquerda(self):
        '''Movimenta o espaço em branco pra esquerda'''
        pass
    
    def direita(self):
        '''Movimenta o espaço em branco pra direita'''
        pass
    
    def moverPeca(self, direcao):
        '''Executa um movimento de acordo com o
        comando passado na sequencia'''
        if direcao == 'C': self.cima()
        if direcao == 'B': self.baixo()
        if direcao == 'D': self.esquerda()
        if direcao == 'E': self.direita()
    
    def leSequenciaMovimentos(self, sequencia):
        '''Lê uma sequência de movimentos a partir de uma string'''
        for direcao in sequencia:
            self.moverPeca(direcao)
    
    def mostraTabuleiro(self):
        print(self.tabuleiro)

a = Tabuleiro(12)
a.mostraTabuleiro()