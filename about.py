#!/usr/bin/python
# coding: latin-1

import pygame, os, sys
from pygame.locals import *

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

def wait(seconds):
    time_limit = pygame.time.get_ticks() + seconds*1000
    clock = pygame.time.Clock()
    events = []
    while pygame.time.get_ticks() <= time_limit:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                return 1
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return 1

def start():

    '''Draws the about screen to the surface.'''

    screen = pygame.display.set_mode((640, 480),0, 32)
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    font = pygame.font.Font("accid.ttf", 20)
    background = pygame.image.load("images/info-bg.png").convert()
    running = True

    about = [
	"StoneHunters está desarrollado en Python y usa el framework",
	" Pygame. Ambos proyectos de código abierto.",
	" ",
	"Fue desarrollado por Rodrigo Contreras Reyes (aka RoCR) como",
	"parte de un proyecto para el Seminario de Programación que",
	"se impartió en la Facultad de Ciencias de la UNAM.",
	" ",
	"Por lo tanto es un proyecto 100% Mexicano :)",
	" ",
	"Agradecimientos a Python Fundation, Pygame Community, a mis",
	"padres, amigos y profesores (y ayudantes).",
	" ",
	"Y EN ESPECIAL A GAB POR SER MI MAYOR INSPIRACION <3"
        ]
    os_x = 80
    os_y = 100

    while running:

        # We make the game run at desired FPS
        time_passed = clock.tick(c.FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        screen.blit(background, (0, 0))

        for i, elem in about.enumerate():
            ren = font.render(elem, 1, (240,240,240))
            screen.blit(ren, (os_x, os_y + i*(font.get_height())))

            pygame.display.update()
