#!/usr/bin/python
# coding: latin-1

import pygame, math
from vector2 import Vector2

class Player(object):

    def __init__(self, img, stage, team, keys, pos = (0,0),
                ofs_x = -1.0 , ofs_y = -25.0, speed = 150):

    	# We load the sprite image
    	self.image = pygame.image.load(img).convert_alpha()

        # We use this to know the current frame to blit
        self.frame_num = 0
        self.frame_sum = 0.
        self.facing = 1

        # We use this to know how many frames we have to animate the sprite
        self.col_num, self.row_num = 3, 4

        # We use this to know the current width & height of each frame
        self.width = 29
        self.height = 53

        # ... and where does the top-left corner of the image is
        self.ofs_y = ofs_y
        self.ofs_x = ofs_x

        # The current position
        self.rect = pygame.Rect(pos[0],pos[1],27,24)

        # The current speed (pixels per second)
        self.speed = speed

        # Othe important data
        self.stage = stage
        self.alive = True
        self.own = False
        self.team = team
        self.keys = keys
        self.stone = -1

    def get_move(self, pressed_keys, time):
    	'''Defines if the input keys will change the position

    	Then it normalizes the movement vector to maintain the
    	movement ratio in all directions.'''
    	position = Vector2(0,0)
        if pressed_keys[self.keys[1]]:
            position.x = -c.STEP
        if pressed_keys[self.keys[3]]:
            position.x = c.STEP
        if pressed_keys[self.keys[0]]:
            position.y = -c.STEP
        if pressed_keys[self.keys[2]]:
            position.y = c.STEP
        position.normalize()
        self.move(position.x,position.y,time)

    def update_frame(self):
    	'''Updates the frame while the user is moving.'''
        self.frame_sum += 0.26
        if self.frame_sum == 4:
            self.frame_sum = 0
        numb = int(self.frame_sum) % 4
        if numb == 0 or numb == 2:
            self.frame_num = 0
        elif numb == 1:
            self.frame_num = 1
        else:
            self.frame_num = 2

    def draw(self, screen):
    	'''Draw the player to the screen.'''
        screen.blit(self.image, (self.rect.x + self.ofs_x, self.rect.y + self.ofs_y), (self.width*self.frame_num, self.height*self.facing, self.width, self.height))

    def move(self, dx, dy, time):
        '''Call __move() for the x axis, then the y axis.'''
        if dx != 0:
            if dx < 0:
            	self.facing = 2
            else:
            	self.facing = 0
            self.__move(dx, 0, time)
        if dy != 0:
            if dy < 0:
            	self.facing = 3
            else:
            	self.facing = 1
            self.__move(0, dy, time)
        if dx != 0 or dy != 0:
        	self.update_frame()

    def __move(self, dx, dy, time):
        '''Move the rect and check for collisions.'''

        self.rect.x += (dx * self.speed * time)
        self.rect.y += (dy * self.speed * time)

        for wall in self.stage.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Hit the left side of a wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Hit the right side of a wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Hit the top side of a wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Hit the bottom side of a wall
                    self.rect.top = wall.rect.bottom

        # If we are on Team B, we can't walk on the base
        if self.team == 'B':
        	for base in self.stage.base:
        		if self.rect.colliderect(base.rect):
        			if dx > 0: # Hit the left side of the base
        				self.rect.right = base.rect.left
        			if dx < 0: # Hit the right side of the base
        				self.rect.left = base.rect.right
        			if dy > 0: # Hit the top side of the base
        				self.rect.bottom = base.rect.top
        			if dy < 0: # Hit the bottom side of the base
        				self.rect.top = base.rect.bottom

    def is_in_water(self):
    	'''Check if this characto is in a safety water sector.'''
    	
    	for water in self.stage.water:
    		if self.rect.colliderect(water.rect):
    			return True
    	return False

    def set_rect(self, axis):
    	'''Move the characto rect to the specified axis.'''
    	
        self.rect.topleft = (axis[0]*c.FIELD_SIZE, axis[1]*c.FIELD_SIZE)
