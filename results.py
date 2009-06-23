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

def start(results):
	'''Shows the results screen given the results data.'''

	screen = pygame.display.set_mode((640, 480),0, 32)
	pygame.mouse.set_visible(False)

	clock = pygame.time.Clock()
	font = pygame.font.Font("accid.ttf", 54)
	background = pygame.image.load("images/res-bg.png").convert()
	running = True

	winner = 0
	draw = False
	for j in range(1, c.PLAYERS):
		if results[j] == results[winner]:
			draw = True
		if results[j] > results[winner]:
			winner = j
			draw = False

	if not draw:
		text = "Player " + str(winner + 1) + " is the winner!"
	else:
		text = "The game was a Draw!"

	font2 = pygame.font.Font("accid.ttf", 24)

	res_text = [
	" ",
	"Here are the results:"
	]
	for x in range(c.PLAYERS):
		tex = "Player " + str(x+1) + " got " + str(results[x]) + " points."
		res_text.append(tex)
	os_y = 200

	while running:

		# We make the game run at desired FPS
		time_passed = clock.tick(c.FPS)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
				running = False

		screen.blit(background, (0, 0))
		ren = font.render(text, 1, (255, 50, 80))
		screen.blit(ren, (320 - ren.get_width()/2, 150))
		i = 0
		for elem in res_text:
			ren = font2.render(elem, 1, (240,240,240))
			screen.blit(ren, (320 - ren.get_width()/2, os_y + i*(font2.get_height())))
			i += 1

		pygame.display.update()
