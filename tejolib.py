# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:40:07 2017

@author: eridanus
"""

import numpy as np
import pygame
from pygame.locals import *   #constantes de pygames


X = 0
Y = 1

class Pelota:
    
    def __init__(self, posicion, velocidad, radio, imagen):
        self.posicion = posicion #numpy array
        self.velocidad = velocidad #numpy array
        self.radio = radio
        self.imagen = imagen
        self.ballrect = self.imagen.get_rect()
        
    def andar(self):
        self.ballrect = self.ballrect.move(self.velocidad)
        #self.posicion += self.velocidad*dt
        
    def rebotar(self, size_pantalla):
        if self.ballrect.left < 0 or self.ballrect.right > size_pantalla[X]:
            self.velocidad[X] = -self.velocidad[X]
        if self.ballrect.top < 0 or self.ballrect.bottom > size_pantalla[Y]:
            self.velocidad[Y] = -self.velocidad[Y]
    	#self.velocidad = velocidad

    def gol(self,cancha_ancho):
    	if self.posicion[X]<0:
    		return 1
    	if self.posicion[X]>cancha_ancho:
    		return 2
    	return 0


