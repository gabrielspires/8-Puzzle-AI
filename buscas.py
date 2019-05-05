import tabuleiro
import estado
import queue as q

class Buscas:
    def __init__(self, tabuleiro):
        """Inicia com um tabuleiro como estado inicial da busca"""
        self.inicio = estado.Estado(tabuleiro)

    #Breadth-first search
    def bfs(self):
        folhas = q.Queue()  # FIFO queue
        visitados = set()
        # Testar goal ao GERAR estado
        # Discartar caminhos por estados que já estão na fronteira ou já foram visitados
        pass

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