from queue import Queue
from copy import deepcopy

class Estado:
    def __init__(self, tabuleiro, estadoPai = None, movimento=""):
        '''
        Inicia um estado com ou sem estado pai, no caso de não ter estado pai
        o estado começa com profundidade zero e apenas com o movimento passado
        como parametro.
        Caso o estado tenha um estado pai, ele herda seus movimentos anteriores
        e soma 1 na profundidade do pai
        '''
        self.estado = tabuleiro
        self.estadoPai = estadoPai
        self.profundidade = 0
        if self.estadoPai is not None:
            self.profundidade = estadoPai.profundidade + 1
            self.movimentos = estadoPai.movimentos + movimento
        else:
            self.movimentos = movimento
            
        self.distManhattan = self.distanciaManhattan()
    
    def __str__(self):
        """Retorna uma string com os movimentos executados do estado inicial
        até o atual"""
        return str(self.movimentos)

    def __lt__(self, value):
        """Serve pra poder comparar a classe por < ou >. Útil ao usar fila de prioridades."""
        return self.profundidade < value.profundidade

    def testeObjetivo(self):
        '''
        Verifica se o estado é o objetivo
        '''
        return self.estado.verificaTabuleiro()

    def funcaoSucessora(self):
        '''
        Função sucessora que retorna todos os estados possíveis
        a partir de uma determinada configuração.
        '''
        estadosPossiveis = []

        for direcao in self.estado.movimentosPossiveis:
            tabuleiro = deepcopy(self.estado)
            tabuleiro.moverPeca(direcao)
            if tabuleiro.vazio is not self.estado.vazio: # Testa se o tabuleiro mudou
                estadosPossiveis.append(Estado(tabuleiro, self, direcao))
        return estadosPossiveis
    
    # Heurísticas

    def custoHeuristica(self, numHeuristica):  #OK
        """Retorna o custo da heurística selecionada.\\
        0 -> nPecasErradas()\\
        1 -> distanciaManhattan()"""

        if numHeuristica == 0:
            return self.nPecasErradas()
        elif numHeuristica == 1:
            return self.distanciaManhattan()

    def distanciaManhattan(self):  #OK
        """Heurística 1: Distancia Manhattan
        Consiste na soma da distância horizontal e vertical das peças até sua posição correta
        Foi encontrado que a posição horizontal das peças no 8-puzzle é sempre (n-1)%tamanho
        e a posição vertical é (n-1)/tamanho, sendo n o número da peça, então a partir disso
        podemos calcular a distância.

        Heurística admissível, pois, a única coisa que qualquer movimento pode fazer é mover uma
        peça um passo mais próximo do objetivo."""

        resultado = 0
        for i in range(self.estado.tamanho):
            for j in range(self.estado.tamanho):
                indice = self.estado.tabuleiro[i][j] - 1
                if indice == -1:
                    distancia = (self.estado.tamanho-1 - i)+(self.estado.tamanho-1 - j)
                else:
                    distancia = abs(i - int(indice/self.estado.tamanho)) + abs(j - (indice%self.estado.tamanho))
                resultado += distancia
        return resultado
    
    def nPecasErradas(self):  #OK
        """Heurística 2: Número de Peças Na Posição Errada
        É o número de peças que não estão na posição que deveriam estar de acordo com o tabuleiro
        objetivo.
        
        Heurística admissível, pois, fica claro que qualquer peça que esteja fora do lugar, precisará
        ser movida ao menos uma vez."""

        pecas_erradas = 0
        num_peca = 1
        for i in range(self.estado.tamanho):
            for j in range(self.estado.tamanho):
                if self.estado.tabuleiro[i][j] != (num_peca%(self.estado.tamanho**2)):
                    pecas_erradas += 1
                num_peca += 1
        return pecas_erradas