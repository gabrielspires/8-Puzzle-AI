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
        # path_cost = 0
        if node.testeObjetivo():
            return node
        frontier = [node]  # FIFO queue
        explored = set()
        while True:
            # if frontier.qsize()%1000 == 0:
            #     print(frontier.qsize())
                # print(len(explored))
            if len(frontier) == 0: return None
            node = frontier.pop(0)
            # print(node.profundidade)
            explored.add(str(node.estado.tabuleiro))
            possibleStates = node.funcaoSucessora()
            while len(possibleStates) != 0:
                child = possibleStates.pop(0)
                if str(child.estado.tabuleiro) not in explored:
                    if child.testeObjetivo(): return child
                    frontier.append(child)


    #Iterative deepening search    
    def iterativeDeepening(self):
        depth = 0
        result = None
        while result is None:
            result = self.depthLimited(depth)
            depth += 1
        return result

    def depthLimited(self, depth):
        node = self.inicio
        frontier = [node]
        while True:
            if len(frontier) == 0:
                return None
            node = frontier.pop(len(frontier)-1)
            if node.testeObjetivo():
                return node
            elif node.profundidade is not depth:
                possibleStates = node.funcaoSucessora()
                while len(possibleStates) != 0:
                    frontier.append(possibleStates.pop(0))


    #Uniform-cost search    
    def uniformCost(self):
        node = self.inicio
        frontier = q.PriorityQueue()
        frontier.put(node)
        explored = set()
        while True:
            if frontier.empty(): return None
            node = frontier.get()
            if node.testeObjetivo():
                return node
            
            explored.add(str(node.estado.tabuleiro))
            possibleStates = node.funcaoSucessora()
            while len(possibleStates) != 0:
                child = possibleStates.pop(0)
                if str(child.estado.tabuleiro) not in explored:
                    frontier.put(child)
                # elif:
                    # uma otimização é substituir os estados que
                    # estao na fila com custo maior se eles
                    # aparecerem com custo menor depois

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
# a.leTabuleiro("1 2 3 4 5 6 7 0 8")
# a.leTabuleiro("5 8 2 1 0 3 4 7 6") # 10
# a.leTabuleiro("8 7 2 5 4 3 1 6 0") # 18
# a.leTabuleiro("8 4 7 5 6 0 1 3 2") # 25
# a.leTabuleiro("0 8 7 5 4 2 1 6 3") # 22
print(a.verificaTabuleiro())
# a.embaralhaTabuleiro(10)
a.mostraTabuleiro()
print("Posição vazia:", a.vazio.x, a.vazio.y)
b = Buscas(a)

# print("Rodando o BFS... : ", end='')
# s = b.bfs()
# print(s, len(str(s)), "movimentos")

# print("Rodando o iterativeDeepening... : ", end='')
# s = b.iterativeDeepening()
# print(s, len(str(s)), "movimentos")

print("Rodando o uniformCost... : ", end='')
s = b.uniformCost()
print(s, len(str(s)), "movimentos")

# e = estado.Estado(a)
# a2 = tabuleiro.Tabuleiro(3)
# a2.leTabuleiro("1 2 3 4 5 6 7 0 8")
# e1 = estado.Estado(a2)
# a3 = tabuleiro.Tabuleiro(3)
# a3.leTabuleiro("1 2 3 4 5 6 7 0 8")
# e2 = estado.Estado(a3)
# front = []
# front.append(e)
# front.append(e2)

# frontier_check = []


# print(frontier_check)
