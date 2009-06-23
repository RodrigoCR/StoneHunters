#!/usr/bin/python
# coding: latin-1

import pygame, random
from constants import *

class Stone(object):

    def __init__(self, pos):
    	self.x = -int(round(c.FIELD_SIZE*0.25))
    	self.y = -int(round(c.FIELD_SIZE*0.25))
    	self.img = pygame.image.load("images/bg/stone.png").convert_alpha()
    	self.rect = pygame.Rect(pos[0]+int(round(c.FIELD_SIZE*0.25)), pos[1]+int(round(c.FIELD_SIZE*0.25)), c.FIELD_SIZE/2, c.FIELD_SIZE/2)
    	self.player = 0
    	self.owned = False

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
    	if not self.owned:
    		screen.blit(self.img, (self.rect.x + self.x,self.rect.y + self.y))
    	else:
    		self.move(self.player.rect.x, self.player.rect.y)
    		screen.blit(self.img, (self.player.rect.x,self.player.rect.y + self.y))

    def set_player(self, player):
    	self.player = player

# Class to hold a wall rect
class Wall(object):
    def __init__(self, pos, image):
        self.rect = pygame.Rect(pos[0], pos[1], c.FIELD_SIZE, c.FIELD_SIZE)
        self.img = image

# Class to hold a Floor rect
class Floor(object):
    def __init__(self, pos, image):
        self.rect = pygame.Rect(pos[0], pos[1], c.FIELD_SIZE, c.FIELD_SIZE)
        self.img = image

# Class to hold a Water rect
class Water(object):
    def __init__(self, pos, image):
        self.rect = pygame.Rect(pos[0], pos[1], c.FIELD_SIZE, c.FIELD_SIZE)
        self.img = image

# Class to hold a Base rect
class Base(object):
    def __init__(self, pos, image):
        self.rect = pygame.Rect(pos[0], pos[1], c.FIELD_SIZE, c.FIELD_SIZE)
        self.img = image

class Stage(object):

    def __init__(self):

    	# Graphics for level
    	self.floor_img = []
    	self.floor_img.append(pygame.image.load("images/bg/grass1.png").convert())
    	self.floor_img.append(pygame.image.load("images/bg/grass2.png").convert())
    	self.floor_img.append(pygame.image.load("images/bg/grass3.png").convert())
    	self.floor_img.append(pygame.image.load("images/bg/grass4.png").convert())
    	self.wall_img = []
    	self.wall_img.append(pygame.image.load("images/bg/stone1.png").convert())
    	self.wall_img.append(pygame.image.load("images/bg/stone2.png").convert())
    	self.water_img = pygame.image.load("images/bg/water.png").convert()
    	self.base_img = pygame.image.load("images/bg/base.png").convert()

		# Elements containers
    	self.walls = [] # List to hold the walls
    	self.water = [] # List to hold the "make me invincible" water
    	self.base = [] # List to hold the base floor
    	self.floor = [] # List to hold the floor

		# Parse the level
    	self.set_level()

    	# Create the stones container
    	self.stones = []

    def set_level(self):
    	'''Parses the level file.

    	S = wall, F = floor, W = water, B = base.
    	'''
    	x = y = 0
    	f = open(c.STAGES[c.STAGE], 'r')
    	for row in f:
    		for col in row:
    			if col == "B":
    				self.base.append(Base((x*c.FIELD_SIZE,y*c.FIELD_SIZE), self.base_img))
    			elif col == "W":
    				self.water.append(Water((x*c.FIELD_SIZE,y*c.FIELD_SIZE), self.water_img))
    			elif col == "S":
    				r = random.randint(0,1)
    				self.walls.append(Wall((x*c.FIELD_SIZE,y*c.FIELD_SIZE), self.wall_img[r]))
    			elif col == "F":
    				r = random.randint(0,3)
    				self.floor.append(Floor((x*c.FIELD_SIZE,y*c.FIELD_SIZE), self.floor_img[r]))
    			x += 1
    		y += 1
    		x = 0

    def set_stones(self):
    	'''Set a random place for the stones.'''
    	self.stones = []
    	for _ in range(5):
    		self.stones.append(self.set_stone())

    def set_stone(self):
    	return Stone(self.get_floor())

    def get_base(self):
    	'''Get a random place from base sectors.'''
    	elem = random.choice(self.base)
    	return (elem.rect.x, elem.rect.y)

    def get_floor(self):
    	'''Get a random place from floor sectors.'''
    	elem = random.choice(self.floor)
    	return (elem.rect.x, elem.rect.y)

    def draw(self, screen):
    	'''Paints the stage (the background) into the screen.'''
    	for elem in self.walls:
    		screen.blit(elem.img, (elem.rect.x, elem.rect.y))
    	for elem in self.floor:
    		screen.blit(elem.img, (elem.rect.x, elem.rect.y))
    	for elem in self.base:
    		screen.blit(elem.img, (elem.rect.x, elem.rect.y))
    	for elem in self.water:
    		screen.blit(elem.img, (elem.rect.x, elem.rect.y))

    	for elem in self.stones:
    		elem.draw(screen)
