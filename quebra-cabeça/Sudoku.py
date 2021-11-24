import numpy as np
import math
import random
#Usamos o Backtracking que é um algoritmo para problemas que envolvem recursão
#Verificamos se tem o mesmo valor em linha e coluna
def possivel(list, linha, c, num):
  for i in range(9):
    if grid[linha][i]==num:
      return False

  for i in range(9):
    if grid[i][c]==num:
      return False
#Deve retornar falso porque se na mesma linha tivermos o mesmo número, esse movimento não pode ser válido
#linha-linha%3 para encontrar a linha superior a esquerda, mesma coisa para as colunas

#Separamos em 3x3 e verificamos se tem o mesmo valor no quadrado
  valor_1=(c//3)*3 
  valor_2=(linha//3)*3

  for i in range(3):
    for j in range(3):
      if grid[valor_2+i][valor_1+j]==num:
        return False

  return True

def res(grid, linha,c):
  if c==9: #lista/coluna de tamanho 9
    if linha==8: #o ultimo valor na verdade é 8
      return True #teremos o sudoku resolvido
    linha+=1 #A ideia é que se formos além da ultima coluna, vamos para a proxima linha, exceto quando já é a linha final
    c=0
  if grid[linha][c]>0: #se não for igual a 8
    return res(grid, linha, c+1)
    
  for num in range(1,10):
    if possivel(grid,linha,c,num):
      grid[linha][c]=num
      if res(grid,linha,c+1):
        return True

    grid[linha][c]=0

  return False

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

if res(grid, 0, 0):
  for i in range(9):
    for j in range(9):
      print(grid[i][j], end=" ")
    print()
else:
    print("Não tem solução")

#a solução é sempre correta