import pygame, sys, time, random, tkinter
pygame.init()


#colores
negro = (0,0,0)
blanco = (255)
rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)

#display
def CW ():
    global window, WH, WW, WT
    WH,WW =800,800
    WT = "perceo"
    pygame.display.set_caption(WT)
    pygame.display.set_mode((WH,WW), pygame.HWSURFACE | pygame.DOUBLEBUF)
CW()
def CFPS ():
    pass
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime('%S'):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.time.strftime('%S')

ML = True
while ML:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ML = False

    #graficos

    pygame.display.update()


pygame.quit()
sys.exit()