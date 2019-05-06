import Pos # Facilitar a representação das posições (tuplas)
# import numpy as np # Facilitar a manipulação da matriz (tabuleiro)
import random # Ajuda pra gerar as permutações do tabuleiro
from copy import deepcopy

class Tabuleiro(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        # self.tabuleiro = np.arange(1,tamanho**2+1).reshape(tamanho, tamanho)
        self.tabuleiro = []
        count=1
        for i in range(self.tamanho):
            self.tabuleiro.append([])
            for j in range(self.tamanho):
                self.tabuleiro[i].append(count%(self.tamanho**2))
                count+=1
        # self.tabuleiro[tamanho-1][tamanho-1] = 0
        self.vazio = Pos.ponto(tamanho-1, tamanho-1)
        self.movimentosPossiveis = ['C','B','D','E']
        
    def embaralhaTabuleiro(self, numMovimentos):
        """Embaralha o tabuleiro executando um número especificado
        de movimentos"""
        print("Tabuleiro embaralhado com os movimentos: ", end="")
        for _ in range(0, numMovimentos):
            vazioAnterior = self.vazio
            while self.vazio == vazioAnterior:  # Peça nenhuma andou
                m = random.choice(self.movimentosPossiveis)
                self.moverPeca(m)
            print(m, end="")
        print()

    def leTabuleiro(self, pecas):
        """Lê o tabuleiro a partir de uma string com
        os números separados por espaço"""

        pecas = pecas.split(" ")

        count=0
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if int(pecas[count]) == 0:
                    self.vazio = Pos.ponto(int(i), int(j))
                self.tabuleiro[i][j] = int(pecas[count])
                count += 1


        # self.tabuleiro = np.fromstring(pecas, dtype=int, sep=" ")
        # self.tabuleiro = self.tabuleiro.reshape(self.tamanho, self.tamanho)
        # x, y = np.where(self.tabuleiro == 0)
        # self.vazio = Pos.ponto(int(x), int(y))
        
    def verificaTabuleiro(self):
        """Verifica se a disposiçao passada do
        tabuleiro é uma solução válida."""
        count = 1
        for linha in self.tabuleiro:
            for item in linha:
                if item != count%(self.tamanho**2):
                    return False
                count += 1
        return True
    
    def trocaPeca(self, pos1, pos2):
        """Troca duas pecas de posição"""
        aux = self.tabuleiro[pos1.x][pos1.y]
        self.tabuleiro[pos1.x][pos1.y] = self.tabuleiro[pos2.x][pos2.y]
        self.tabuleiro[pos2.x][pos2.y] = aux
    
    def cima(self):
        """Movimenta o espaço em branco pra cima"""
        if self.vazio.x > 0:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x-1,self.vazio.y))
            self.vazio = Pos.ponto(self.vazio.x-1,self.vazio.y)
    
    def baixo(self):
        """Movimenta o espaço em branco pra baixo"""
        if self.vazio.x != self.tamanho-1:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x+1,self.vazio.y))
            self.vazio = Pos.ponto(self.vazio.x+1,self.vazio.y)
    
    def esquerda(self):
        """Movimenta o espaço em branco pra esquerda"""
        if self.vazio.y > 0:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x,self.vazio.y-1))
            self.vazio = Pos.ponto(self.vazio.x,self.vazio.y-1)
    
    def direita(self):
        """Movimenta o espaço em branco pra direita"""
        if self.vazio.y < self.tamanho-1:
            self.trocaPeca(self.vazio, Pos.ponto(self.vazio.x,self.vazio.y+1))
            self.vazio = Pos.ponto(self.vazio.x,self.vazio.y+1)
    
    def moverPeca(self, direcao):
        """Executa um movimento de acordo com o
        comando passado na sequencia"""
        if direcao == 'C': self.cima()
        elif direcao == 'B': self.baixo()
        elif direcao == 'D': self.direita()
        elif direcao == 'E': self.esquerda()
    
    def leSequenciaMovimentos(self, sequencia):
        """Lê uma sequência de movimentos a partir de uma string"""
        for direcao in sequencia:
            self.moverPeca(direcao)
    
    def mostraTabuleiro(self):
        for linha in self.tabuleiro:
            for peca in linha:
                if peca == 0: print(peca, end=' ')
                else: print(peca, end=' ')
            print()
        print()


# a = Tabuleiro(3)
# a.leTabuleiro("8 6 7 2 5 4 3 0 1")  # 31
# a.leTabuleiro("7 2 4 5 0 6 8 3 1")
# print("Posição vazia:", a.vazio.x, a.vazio.y)
# a.mostraTabuleiro()
# a.trocaPeca(Pos.ponto(1,1), Pos.ponto(0,1))
# a.mostraTabuleiro()
# print(a.verificaTabuleiro())
# a.direita()
# a.mostraTabuleiro()
# print(a.verificaTabuleiro())
# a.embaralhaTabuleiro(31)
# a.mostraTabuleiro()
