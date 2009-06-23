#!/usr/bin/python

import pygame, os, random

class Menu:

    def __init__(self, options, c):
        self.c = c
        self.fce = lambda: None # Dummy function to post-compare type
        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font("accid.ttf", 24)
        self.sound = pygame.mixer.Sound("sounds/option.wav")
        self.option = 0
        self.width = 1
        self.height = len(self.options)*self.font.get_height()
        self.background = pygame.image.load("images/menu-bg.png").convert_alpha()
        # We calculate the menu total width
        for i in range(len(self.options)):
            text = self.options[i][0]
            if self.options[i][3]:
                text += '  < '+str(self.options[i][3][3])+self.options[i][3][4]+' >'
            ren = self.font.render(text, 1, self.c.MENU_COLOURS[0][0])
            if ren.get_width() > self.width:
                self.width = ren.get_width()

    def draw(self, surface):
        """Draw the menu to the surface."""
        
        surface.blit(self.background, (0, 0))
        i=0
        for o in self.options:
            clr = self.c.MENU_COLOURS[o[2]][1]
            if i == self.option:
                clr = self.c.MENU_COLOURS[o[2]][0]
            text = o[0]
            if o[3]:
                text += '  < '+str(o[3][3])+o[3][4]+' >'
            else:
            	if i == self.option:
            		text += "  +"
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x - 200, self.y + i*(self.font.get_height()*.9+10)))
            i+=1

    def stopMusic(self):
    	self.song.stop()

    def update(self, events):
        """Update the menu and get input for the menu."""
        
        for e in events:
            if e.type == pygame.KEYDOWN:
            	self.sound.stop()
            	self.sound.play(0,1000,500)
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    if type( self.options[self.option][1] ) == type(self.fce) or type( self.options[self.option][1] ) == type(self.update):
                        if self.option == 0:
                        	c.MENU_SONG.stop()
                        self.options[self.option][1]()
                        return 1
                if e.key == pygame.K_LEFT:
                    if not self.options[self.option][3]:
                        continue
                    self.options[self.option][3][3] -= self.options[self.option][3][2]
                    if self.options[self.option][3][3] < self.options[self.option][3][0]:
                        self.options[self.option][3][3] = self.options[self.option][3][1]
                    self.c.set_var(self.options[self.option][1], self.options[self.option][3][3])
                if e.key == pygame.K_RIGHT:
                    if not self.options[self.option][3]:
                        continue
                    self.options[self.option][3][3] += self.options[self.option][3][2]
                    if self.options[self.option][3][3] > self.options[self.option][3][1]:
                        self.options[self.option][3][3] = self.options[self.option][3][0]
                    self.c.set_var(self.options[self.option][1], self.options[self.option][3][3])
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

    def set_pos(self, x, y):
        """Set the topleft of the menu at x,y."""
        
        self.x = x
        self.y = y

    def set_font(self, font):
        """Set the font used for the menu."""
        
        self.font = font

    def set_highlight_color(self, color):
        """Set the highlight color."""
        
        self.hcolor = color

    def set_normal_color(self, color):
        """Set the normal color."""
        
        self.color = color

    def center_at(self, x, y):
        """Center the center of the menu at x,y."""
        
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
