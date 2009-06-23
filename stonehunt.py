#!/usr/bin/python
# coding: latin-1

import pygame, os, random, sys, results
from pygame.locals import *
from constants import *
from stage import Stage
from player import Player

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

class Info(object):
	def __init__(self):
		self.score = [0]*c.PLAYERS
		self.time = 0.0
		self.turn = 0
		self.font = pygame.font.Font("accid.ttf", 18)
		self.reload_score()
		self.arrows = pygame.image.load("images/arrows.png").convert_alpha()

	def reload_score(self):
		'''Creates the text for the score board.'''
		self.score_text = ''
		for i in range(c.PLAYERS):
			self.score_text += 'Player ' + str(i + 1) +' has ' + str(self.score[i]) + ' points  >> '

	def draw(self,screen, players):
		'''Draws the scoreboard into the screen.'''
		score_label = self.font.render(self.score_text, 1, (230,230,230))
		pygame.draw.rect(screen, (20, 30, 20), (0, c.FIELD_SIZE*25, c.FIELD_SIZE*30, 30))
		screen.blit(score_label, (15, c.FIELD_SIZE*25 + 5))
		time = str(self.time).split('.')
		time_stamp = ' Current elapsed time: ' + str(time[0])+'.'+str(time[1][0])+' s >>'
		time_label = self.font.render(time_stamp, 1, (255,255,255))
		screen.blit(time_label, (15 + score_label.get_width() + 15, c.FIELD_SIZE*25 + 5))
		for p in range(c.PLAYERS):
			if not players[p].alive:
				continue
			if players[p].team == 'A':
				x_off = 0
			else:
				x_off = 1
			screen.blit(self.arrows, (players[p].rect.x, players[p].rect.y - 40), (30*x_off, 16*p, 30, 16))

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

def create_players(info,stage):
	'''Create the players in accordance with the turn and the current team.'''
	players = []
	p_img = "images/hunterA1.png"
	p2_img = "images/hunterB1.png"
	for x in range(c.PLAYERS):
		if c.TEAM[info.turn][x] == "A":
			pos = stage.get_base()
			img = p_img
			team = 'A'
		else:
			pos = stage.get_floor()
			img = p2_img
			team = 'B'
		#print "Creating player at", pos
		players.append(Player(img, stage, team, c.KEYS[x], pos))
	return players

def start():
	'''Generates the loop to draw into the screen with the game logic.'''
	screen = pygame.display.set_mode((30*c.FIELD_SIZE, 25*c.FIELD_SIZE + 30), DOUBLEBUF | HWSURFACE, 32)
	pygame.mouse.set_visible(False)
	info = Info()

	clock = pygame.time.Clock()
	c.GAME_SONG.play(-1)
	stage = Stage()
	stage.set_stones()

	spawners = []
	players = create_players(info,stage)

	running = True

	while running:

		# We make the game run at desired FPS
		time_passed = clock.tick(c.FPS)

		# We take the current time to show it in the scoreboard
		time_passed_seconds = time_passed / 1000.0
		info.time += time_passed_seconds

		# Here we check if it's other players turn
		if c.HUNTING_TIME*(info.turn + 1) <= int(info.time):
			print "Ended turn time..."
			info.turn += 1
			if info.turn > (c.PLAYERS - 1):
				running = False
				continue
			players = create_players(info,stage)

		# If a player is death and have to respawn, here we check
		# if it's time to do it.
		if spawners:
			offset = 0
			for s in range(len(spawners)):
				if spawners[s+offset][0] <= int(info.time):
					for p in spawners[s+offset][1:3]:
						players[p].alive = True
						pos = stage.get_base()
						players[p].rect.x = pos[0]
						players[p].rect.y = pos[1]
					del spawners[s+offset]
					offset -= 1

		# The game logic is here
		for p in range(c.PLAYERS):
			if not players[p].alive:
				continue

			if players[p].team == 'B':
				for p2 in range(c.PLAYERS):
					if p != p2 and players[p2].team == 'A' and players[p2].alive:
						if players[p].rect.colliderect(players[p2].rect) and not players[p2].is_in_water():
							if players[p2].own:
								stage.stones[players[p2].stone] = stage.set_stone()
								players[p2].stone = -1
								players[p2].own = False
							players[p2].alive = False
							spawners.append([info.time + c.SPAWN_TIME,p2])
							info.score[p] += 1
							info.reload_score()

			elif players[p].team == 'A':
				for s in range(len(stage.stones)):
					if players[p].rect.colliderect(stage.stones[s].rect) and not players[p].own:
						players[p].own = True
						players[p].stone = s
						stage.stones[s].owned = True
						stage.stones[s].set_player(players[p])

				if players[p].own:
					for elem in stage.base:
						if players[p].rect.colliderect(elem.rect):
							info.score[p] += 1
							info.reload_score()
							players[p].own = False
							stage.stones[players[p].stone] = stage.set_stone()
							players[p].stone = -1

		# Here we crontol the events
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
				running = False

		# And at the same time, we draw the stage, the users and the scoreboard
		# to the screen
		stage.draw(screen)

		key = pygame.key.get_pressed()
		for p in range(c.PLAYERS):
			if not players[p].alive:
				continue
			players[p].get_move(key, time_passed_seconds)
			players[p].draw(screen)

		info.draw(screen, players)

		pygame.display.update()

	# At the end, we stop the music and start the menu one, with the results
	c.GAME_SONG.stop()
	c.MENU_SONG.play(-1)
	results.start(info.score)
