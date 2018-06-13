import random as ran
import tkinter
import pygame
# varariables
width = 40
num_min = 10
dis = 9
# constructor
class Tile:
    def __init__(self):
        self.min = False
# mapa
def mapa (x,num_min) :
    grid = [[Tile() for n in range (x)]]
    for n in range (num_min):
        x=ran(0,8)
        y=ran(0,8)
        while True:
            if grid[y][x].min == False:
                grid[y][x].min == True
                break
def setup():
    size(800,600)
def draw (grid):
    y = 0
    for row in grid:
        x = 0
        for Tile in row:
            if Tile.min == True:
                fill (255, 0, 0)
            else:
                fill (255)
            rect(x,y,width,width)
            x+=width
        y+=width
setup()
mapa(x,num_min)
draw(grid)