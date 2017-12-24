# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:40:07 2017

@author: eridanus
"""

import pygame
from pygame.locals import *   #constantes de pygames
import sys

from tejolib import *

###############################################################################
#                   Constantes, variables previas
###############################################################################
size_pantalla = (900,480)
pantalla_centro = np.array(size_pantalla)/2


###############################################################################
#                   Constantes y cosas del juego
###############################################################################
pygame.init()#siempre antes de usar cualquier funcion de pygames


FPS=30
dt=1
fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode(size_pantalla, 0, 32)#para definir el tamaño de la ventana
pygame.display.set_caption("Tejo power ranger")#titulo a la ventana

#________________Musica______________________
#pygame.mixer.music.load("Binary Sunset.mp3")

#_______________Colores______________________
WHITE=(255,255,255)
DARK=(0,0,0)

#_______________Imagenes_____________________
ball_im = pygame.image.load("ball.png")
# ImJup=pygame.image.load("Jupiter.png")
# ImSol=pygame.image.load("Sol.png")

#_______________Objetos______________________
ball = Pelota(np.array(pantalla_centro, dtype = np.float64), 10*(np.random.rand(2)*2-1), 10, ball_im)


###############################################################################
#                   El juego en si
###############################################################################

#pygame.mixer.music.play(-1, 0.0)
while True:#loop principal del juego
    screen.fill(DARK)
    screen.blit(ball.imagen, ball.ballrect)
    
    #DISPLAYSURF.blit(ImSol,centro-rs)    
    #DISPLAYSURF.blit(ImTerra,post)   
    #DISPLAYSURF.blit(ImJup,centro+Rj-rs-rj)    
    
    ball.andar()
    ball.rebotar(size_pantalla)
    ball.gol(size_pantalla[Y])
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()#sale de pygame
            sys.exit()#sale del programa
            
    pygame.display.update()
    fpsClock.tick(FPS)
    
    





























