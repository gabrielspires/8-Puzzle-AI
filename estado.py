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
        estadosPossiveis = Queue()
        movimentosPossiveis = ['C','B','D','E']

        for direcao in movimentosPossiveis:
            tabuleiro = deepcopy(self.estado)
            tabuleiro.moverPeca(direcao)
            if tabuleiro.vazio is not self.estado.vazio: # Testa se o tabuleiro mudou
                estadosPossiveis.put(Estado(tabuleiro, self, direcao))
        return estadosPossiveis
    
