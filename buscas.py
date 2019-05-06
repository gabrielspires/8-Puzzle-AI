import tabuleiro
import estado
import queue as q
import numpy as np

import operator

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
        limitDepth = 0
        result = None
        while result is None:
            result = self.depthLimited(limitDepth)
            limitDepth += 1
        return result

    def depthLimited(self, depth):
        node = self.inicio
        frontier = [node]
        while True:
            if len(frontier) == 0: return None
            node = frontier.pop(len(frontier)-1)
            if node.testeObjetivo(): return node
            elif node.profundidade is not depth:
                possibleStates = node.funcaoSucessora()
                while len(possibleStates) != 0:
                    frontier.append(possibleStates.pop(0))


    #Uniform-cost search    
    def uniformCost(self):
        node = self.inicio
        frontier = q.PriorityQueue()
        frontier.put((node.profundidade, node))
        explored = set()
        while True:
            if frontier.empty(): return None
            node = frontier.get()[1]
            if node.testeObjetivo(): return node
            
            explored.add(str(node.estado.tabuleiro))
            possibleStates = node.funcaoSucessora()
            while len(possibleStates) != 0:
                child = possibleStates.pop(0)
                if str(child.estado.tabuleiro) not in explored:
                    frontier.put((child.profundidade, child))
                # elif:
                    # uma otimização é substituir os estados que
                    # estao na fila se eles aparecerem com custo
                    # menor depois

    #A* search
    def aStar(self, heuristica):
        node = self.inicio
        frontier = q.PriorityQueue()
        frontier.put((node.custoHeuristica(heuristica),node))
        closed = []
        while True:
            if frontier.empty(): return None
            node = frontier.get()[1]
            if node.testeObjetivo(): return node
                
            elif str(node.estado.tabuleiro) not in closed:
                closed.append(str(node.estado.tabuleiro))
                possibleStates = node.funcaoSucessora()
                while len(possibleStates) != 0:
                    child = possibleStates.pop(0)
                    frontier.put((child.custoHeuristica(heuristica)+child.profundidade, child))


    #Greedy best-first search
    def greedyBestFirst(self, heuristica):
        node = self.inicio
        frontier = q.PriorityQueue()
        frontier.put((node.custoHeuristica(heuristica),node))
        closed = []
        while True:
            if frontier.empty(): return None
            node = frontier.get()[1]
            if node.testeObjetivo(): return node
                
            elif str(node.estado.tabuleiro) not in closed:
                closed.append(str(node.estado.tabuleiro))
                possibleStates = node.funcaoSucessora()
                while len(possibleStates) != 0:
                    child = possibleStates.pop(0)
                    frontier.put((child.custoHeuristica(heuristica), child))
    
    #Hill Climbing, permitindo movimentos laterais
    def hillClimbing(self):
        current = self.inicio
        frontier = [current]
        explored = set()

        while len(frontier) != 0:
            node = frontier.pop(0)
            if node.testeObjetivo(): return node

            explored.add(str(node.estado.tabuleiro))

            possibleStates = node.funcaoSucessora()
            possibleStates.sort(key=operator.attrgetter('distManhattan'))
            for item in possibleStates:
                if str(item.estado.tabuleiro) in explored or str(item.estado.tabuleiro) in frontier:
                    print("PENES")
                    possibleStates.remove(item)
                    print(len(frontier))
            frontier = possibleStates + frontier


            



a = tabuleiro.Tabuleiro(3)
a.leTabuleiro("8 6 7 2 5 4 3 0 1")  # 31
# a.leTabuleiro("1 3 0 7 2 6 5 4 8")
# a.leTabuleiro("8 0 7 5 3 2 1 4 6")
# a.leTabuleiro("5 8 2 7 0 3 1 4 6") # 14
# a.leTabuleiro("5 8 2 1 0 3 4 7 6") # 10
# a.leTabuleiro("8 7 2 5 4 3 1 6 0") # 18
# a.leTabuleiro("8 4 7 5 6 0 1 3 2") # 25
# a.leTabuleiro("0 8 7 5 4 2 1 6 3") # 22
print(a.verificaTabuleiro())
# a.embaralhaTabuleiro(10)
a.mostraTabuleiro()
# print("Posição vazia:", a.vazio.x, a.vazio.y)
b = Buscas(a)
# print(b.inicio.distManhattan)

# print("Rodando o BFS... : ", end='')
# s = b.bfs()
# print(s, len(str(s)), "movimentos")

# Rodando o BFS... : CCDBEEBDDCEECDDBEBECCDBBECCDDBB 31 movimentos
# python3 buscas.py  199,25s user 0,73s system 100% cpu 3:19,79 total

# print("Rodando o uniformCost... : ", end='')
# s = b.uniformCost()
# print(s, len(str(s)), "movimentos")

# Rodando o BFS... : CCDBEEBDDCEECDDBEBECCDBBECCDDBB 31 movimentos
# python3 buscas.py  199,25s user 0,73s system 100% cpu 3:19,79 total

# print("Rodando o aStar... : ", end='')
# s = b.aStar(1)
# print(s, len(str(s)), "movimentos")

# Rodando o aStar... : DCCEBBDCCEBEBDCECDBBDCCEBEBDCDB 31 movimentos
# python3 buscas.py  21,06s user 0,21s system 100% cpu 21,071 total

# print("Rodando o greedyBestFirst... : ", end='')
# s = b.greedyBestFirst(0)
# print(s, len(str(s)), "movimentos")

# Rodando o greedyBestFirst... : ECCDDBBEECCDDBBEECCDDBBEECCDDBEBDCECDBBECDCEBBDCECDBB 53 movimentos
# python3 buscas.py  0,30s user 0,16s system 172% cpu 0,267 total

print("Rodando o iterativeDeepening... : ", end='')
s = b.iterativeDeepening()
print(s, len(str(s)), "movimentos")

# print("Rodando o hillClimbing... : ", end='')
# s = b.hillClimbing()
# print(s, len(str(s)), "movimentos")
