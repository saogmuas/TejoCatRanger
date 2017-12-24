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
dy = 10
JUGADOR_VELOCIDAD = 10

class Pelota:
    
    def __init__(self, posicion, velocidad, radio, imagen):
        self.posicion = posicion #numpy array
        self.velocidad = velocidad #numpy array
        self.radio = radio
        self.imagen = imagen
        self.ballrect = self.imagen.get_rect()
        self.ballrect.center = posicion
        
    def andar(self):
        self.ballrect = self.ballrect.move(self.velocidad)
        self.posicion = self.ballrect.center
        
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


class Jteclas:
	up = None
	down = None


class Jugador:
	
	def __init__(self, posicion, nombre, imagen, teclas):
		self.posicion = posicion
		self.nombre = nombre
		self.imagen = imagen
		self.imagenrect = self.imagen.get_rect()
		self.imagenrect.center = self.posicion
		self.teclas = teclas
	
	def mover(self, keypress, size_pantalla):
		#keypress es de tipo "keypress" de pygame
		#pygame.time.delay(100)
		if keypress[self.teclas.up]:
			self.imagenrect = self.imagenrect.move([0, -JUGADOR_VELOCIDAD])
		if keypress[self.teclas.down]:
			self.imagenrect = self.imagenrect.move([0, JUGADOR_VELOCIDAD])
		self.posicion = self.imagenrect.center
			
			
			
