import tabuleiro
import estado
import queue as q
import numpy as np

from copy import deepcopy
class Buscas:
    def __init__(self, tabuleiro):
        """Inicia com um tabuleiro como estado inicial da busca"""
        self.inicio = estado.Estado(tabuleiro)

    #Breadth-first search
    def bfs(self):
        # Testar goal ao GERAR estado
        # Discartar caminhos por estados que já estão na fronteira ou já foram visitados
        node = self.inicio
        path_cost = 0
        if self.inicio.testeObjetivo():
            return self.inicio
        frontier = q.Queue()  # FIFO queue
        frontier.put(self.inicio)
        explored = set()
        while True:
            # if frontier.qsize()%500 == 0: print(frontier.qsize())
            if frontier.empty(): return None
            node = frontier.get()
            explored.add(np.array2string(node.estado.tabuleiro))
            possibleStates = node.funcaoSucessora()
            while not possibleStates.empty():
                child = possibleStates.get()
                if np.array2string(child.estado.tabuleiro) not in explored:
                    if child.testeObjetivo(): return child
                    frontier.put(child)


    #Iterative deepening search    
    def iterativeDeepening(self):
        pass

    #Uniform-cost search    
    def uniformCost(self):
        pass

    #A* search    
    def aStar(self):
        pass

    #Greedy best-first search
    def greedyBestFirst(self):
        pass
    
    #Hill Climbing, permitindo movimentos laterais
    def hillClimbing(self):
        pass



a = tabuleiro.Tabuleiro(3)
a.leTabuleiro("8 6 7 2 5 4 3 0 1")  # 31
# a.leTabuleiro("1 3 0 7 2 6 5 4 8")
# a.leTabuleiro("8 0 7 5 3 2 1 4 6")
# a.leTabuleiro("1 2 3 4 5 6 7 8 0")
# a.embaralhaTabuleiro(10)
a.mostraTabuleiro()
print("Posição vazia:", a.vazio.x, a.vazio.y)
b = Buscas(a)
print(b.bfs())