import tabuleiro
import estado
import queue as q
# import numpy as np

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
        expandedStates = 0
        while True:
            # if frontier.qsize()%1000 == 0:
            #     print(frontier.qsize())
                # print(len(explored))
            if len(frontier) == 0: return None
            node = frontier.pop(0)
            # print(node.profundidade)
            explored.add(str(node.estado.tabuleiro))
            possibleStates = node.funcaoSucessora()
            expandedStates += len(possibleStates)
            while len(possibleStates) != 0:
                child = possibleStates.pop(0)
                if str(child.estado.tabuleiro) not in explored:
                    if child.testeObjetivo():
                        print("\tNós expandidos:\t", expandedStates)
                        return child
                    frontier.append(child)


    #Iterative deepening search    
    def iterativeDeepening(self):
        # limitDepth = 0
        # result = None

        # while result is None:
        #     result, remaining = self.depthLimited(self.inicio, limitDepth)
        #     limitDepth += 1
        #     if result is not None:
        #         return result
        #     elif not remaining:
        #         return None

        limitDepth = 0
        result = None
        while result is None:
            result = self.depthLimited(limitDepth)
            limitDepth += 1
        return result

    def depthLimited(self, depth):
        # if depth == 0:
        #     if node.testeObjetivo(): return (node,True)
        #     else: return (None, True)
        
        # elif depth > 0:
        #     print(depth)
        #     any_remaining = False
        #     possibleStates = node.funcaoSucessora()
        #     for child in possibleStates:
        #         found, remaining = self.depthLimited(child, depth-1)
        #         if found is not None: return (found, True)
        #         if remaining:
        #             any_remaining = True
        #     return (None, any_remaining)


        # node = self.inicio
        frontier = [self.inicio]
        # if depth == 0:
        #     if node.testeObjetivo(): return node
        #     else: return None

        explored = set()
        expandedStates = 0
        while True:
            if len(frontier) == 0: return None
            node = frontier.pop(0)
            explored.add(str(node.estado.tabuleiro))
            # print(node.profundidade)
            if node.testeObjetivo(): 
                print("\tNós expandidos:\t", expandedStates)
                return node
            elif node.profundidade is not depth:
                possibleStates = node.funcaoSucessora()
                expandedStates += len(possibleStates)
                while len(possibleStates) != 0:
                    new_node = possibleStates.pop(0)
                    if str(new_node.estado.tabuleiro) not in explored:
                        frontier.append(new_node)


    #Uniform-cost search    
    def uniformCost(self):
        node = self.inicio
        frontier = q.PriorityQueue()
        frontier.put((node.profundidade, node))
        explored = set()
        expandedStates = 0
        while True:
            if frontier.empty(): return None
            node = frontier.get()[1]
            if node.testeObjetivo(): 
                print("\tNós expandidos:\t", expandedStates)
                return node
            
            explored.add(str(node.estado.tabuleiro))
            possibleStates = node.funcaoSucessora()
            expandedStates += len(possibleStates)
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
        expandedStates = 0
        while True:
            if frontier.empty(): return None
            node = frontier.get()[1]
            if node.testeObjetivo(): 
                print("\tNós expandidos:\t", expandedStates)
                return node
                
            elif str(node.estado.tabuleiro) not in closed:
                closed.append(str(node.estado.tabuleiro))
                possibleStates = node.funcaoSucessora()
                expandedStates += len(possibleStates)
                while len(possibleStates) != 0:
                    child = possibleStates.pop(0)
                    frontier.put((child.custoHeuristica(heuristica)+child.profundidade, child))


    #Greedy best-first search
    def greedyBestFirst(self, heuristica):
        node = self.inicio
        frontier = q.PriorityQueue()
        frontier.put((node.custoHeuristica(heuristica),node))
        closed = []
        expandedStates = 0
        while True:
            if frontier.empty(): return None
            node = frontier.get()[1]
            if node.testeObjetivo():
                print("\tNós expandidos:\t", expandedStates)
                return node
                
            elif str(node.estado.tabuleiro) not in closed:
                closed.append(str(node.estado.tabuleiro))
                possibleStates = node.funcaoSucessora()
                expandedStates += len(possibleStates)
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

