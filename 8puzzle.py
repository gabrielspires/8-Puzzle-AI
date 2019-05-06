#8puzzle

import tabuleiro
import buscas
import estado

import sys
import time

print("8-Puzzle - Solucionando o problema com Inteligência Artificial\n\n")
print("Escolha qual caso teste deseja executar: [0-31]")
opcao = int(input("> "))

a = tabuleiro.Tabuleiro(3)

if opcao == 0:
    a.leTabuleiro("1 2 3 4 5 6 7 8 0") # 0
if opcao == 1:
    a.leTabuleiro("1 2 3 4 5 6 7 0 8") # 1
if opcao == 2:
    a.leTabuleiro("1 2 3 4 0 5 7 8 6") # 2
if opcao == 3:
    a.leTabuleiro("1 0 3 4 2 5 7 8 6") # 3
if opcao == 4:
    a.leTabuleiro("1 5 2 1 0 3 7 8 6") # 4
if opcao == 5:
    a.leTabuleiro("1 5 2 0 4 3 7 8 6") # 5
if opcao == 6:
    a.leTabuleiro("1 5 2 4 8 3 7 6 0") # 6
if opcao == 7:
    a.leTabuleiro("1 5 2 4 8 0 7 6 3") # 7
if opcao == 8:
    a.leTabuleiro("0 5 2 1 8 3 4 7 6") # 8
if opcao == 9:
    a.leTabuleiro("1 0 2 8 5 3 4 7 6") # 9
if opcao == 10:
    a.leTabuleiro("5 8 2 1 0 3 4 7 6") # 10
if opcao == 11:
    a.leTabuleiro("5 8 2 1 7 3 4 0 6") # 11
if opcao == 12:
    a.leTabuleiro("5 8 2 1 7 3 0 4 6") # 12
if opcao == 13:
    a.leTabuleiro("5 8 2 0 7 3 1 4 6") # 13
if opcao == 14:
    a.leTabuleiro("5 8 2 7 0 3 1 4 6") # 14
if opcao == 15:
    a.leTabuleiro("8 0 2 5 7 3 1 4 6") # 15
if opcao == 16:
    a.leTabuleiro("8 7 2 5 0 3 1 4 6") # 16
if opcao == 17:
    a.leTabuleiro("5 0 8 7 3 2 1 4 6") # 17
if opcao == 18:
    a.leTabuleiro("8 7 2 5 4 3 1 6 0") # 18
if opcao == 19:
    a.leTabuleiro("8 0 7 5 3 2 1 4 6") # 19
if opcao == 20:
    a.leTabuleiro("8 7 0 5 4 2 1 6 3") # 20
if opcao == 21:
    a.leTabuleiro("8 0 7 5 4 2 1 6 3") # 21
if opcao == 22:
    a.leTabuleiro("0 8 7 5 4 2 1 6 3") # 22
if opcao == 23:
    a.leTabuleiro("8 4 7 5 6 2 1 0 3") # 23
if opcao == 24:
    a.leTabuleiro("8 4 7 5 6 2 1 3 0") # 24
if opcao == 25:
    a.leTabuleiro("8 4 7 5 6 0 1 3 2") # 25
if opcao == 26:
    a.leTabuleiro("0 4 7 8 6 2 5 1 3") # 26
if opcao == 27:
    a.leTabuleiro("8 0 7 5 4 6 1 3 2") # 27
if opcao == 28:
    a.leTabuleiro("8 4 7 6 2 3 5 1 0") # 28
if opcao == 29:
    a.leTabuleiro("8 0 6 5 7 3 1 2 4") # 29
if opcao == 30:
    a.leTabuleiro("0 8 7 5 6 4 1 2 3") # 30
if opcao == 31:
    a.leTabuleiro("8 6 7 2 5 4 3 0 1") # 31

print("\nTabuleiro:")
a.mostraTabuleiro()
print("C -> Cima, B -> Baixo, D -> Direita, E -> Esquerda\n")
b = buscas.Buscas(a)

print("Rodando o BFS... :")
start_time = time.time()
s = b.bfs()
end_time = time.time()
total_time = end_time - start_time
print("\tResposta:\t", s)
print("\tNum. movimentos:", len(str(s)))
print("\tTempo:\t\t", "%.2f" % total_time, "segundos")

print("Rodando o uniformCost... : ")
start_time = time.time()
s = b.uniformCost()
end_time = time.time()
total_time = end_time - start_time
print("\tResposta:\t", s)
print("\tNum. movimentos:", len(str(s)))
print("\tTempo:\t\t", "%.2f" % total_time, "segundos")

print("Rodando o A* com a heurística da Distancia de Manhattan... : ")
start_time = time.time()
s = b.aStar(1)
end_time = time.time()
total_time = end_time - start_time
print("\tResposta:\t", s)
print("\tNum. movimentos:", len(str(s)))
print("\tTempo:\t\t", "%.2f" % total_time, "segundos")

print("Rodando o greedyBestFirst... : ")
start_time = time.time()
s = b.greedyBestFirst(0)
end_time = time.time()
total_time = end_time - start_time
print("\tResposta:\t", s)
print("\tNum. movimentos:", len(str(s)))
print("\tTempo:\t\t", "%.2f" % total_time, "segundos")

print("Rodando o iterativeDeepening... : ")
start_time = time.time()
s = b.iterativeDeepening()
end_time = time.time()
total_time = end_time - start_time
print("\tResposta:\t", s)
print("\tNum. movimentos:", len(str(s)))
print("\tTempo:\t\t", "%.2f" % total_time, "segundos")

# print("Rodando o hillClimbing... : ", end='')
# start_time = time.time()
# s = b.hillClimbing()
# end_time = time.time()
# total_time = end_time - start_time
# print("\tResposta:\t", s)
# print("\tNum. movimentos:", len(str(s)))
# print("\tTempo:\t\t", "%.2f" % total_time, "segundos")