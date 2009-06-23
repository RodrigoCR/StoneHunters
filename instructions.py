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
	'''Draws the instructions screen in the surface.'''

	screen = pygame.display.set_mode((640, 480),0, 32)
	pygame.mouse.set_visible(False)

	clock = pygame.time.Clock()
	font = pygame.font.Font("accid.ttf", 20)
	background = pygame.image.load("images/inst-bg.png").convert()
	running = True

	instructions = [
	"There is a total of 3 players in the game:",
	" + Player 1 uses the W, A, S and D keys",
	" + Player 2 uses the I, J, K and L keys",
	" + Player 3 uses the UP, LEFT, DOWN and RIGHT keys",
	"As you can see, the first key is to move your character",
	"upside, the second one to move it to the left, the third one",
	"to move it downside and the last one to move it to the right.",
	"Every one has a turn to be a Stone Hunter, you have to get the",
	"stones and bring theme back to your base.",
	"The other ones are simply Hunters, and have to get the Stone",
	"Hunter to end the game.",
	"The player with more Stones collected at the end, wins."
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
		
		for i, elem in instructions.enumerate():
			ren = font.render(elem, 1, (240,240,240))
			screen.blit(ren, (os_x, os_y + i*(font.get_height())))

		pygame.display.update()
