#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
import menu, instructions, about, stonehunt, stage, player, results
from pygame.locals import *
from constants import Container

def start(c):
	# We create the screen surface
    screen = pygame.display.set_mode((640,480), DOUBLEBUF | HWSURFACE, 32)
    pygame.display.set_caption("StoneHunters - By RoCR [ To Gab ]")
    icon = pygame.image.load("images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)
    screen.fill((0, 10, 0))
    # We specify for each import, the constant object as a global var
    stonehunt.c = c
    stage.c = c
    player.c = c
    about.c = c
    instructions.c = c
    menu.c = c
    results.c = c
    # We create the menu with this characteristics
    # [text, method, type, None]
    game_menu = menu.Menu([
            ["Hunt Stones", stonehunt.start, c.NORMAL, None],
            ["About the Game", about.start, c.NORMAL, None],
            ["Instructions", instructions.start, c.NORMAL, None],
            ["Options", options, c.OPTIONS, None],
            ["Quit Game", end, c.END, None]], c)
    game_menu.center_at(320, 200)
    c.MENU_SONG.play(-1) # Infinite loop the song
    loop(game_menu, screen)
    c.save_settings()

def loop(game_menu, screen):
    '''Create a loop to show the menu in the screen suface.

    It also catches the events to update the menu.
    '''

    running = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        events = pygame.event.get()
        if events:
            if game_menu.update(events):
                screen = pygame.display.set_mode((640,480),DOUBLEBUF | HWSURFACE, 32)
            for e in events:
                if e.type == pygame.QUIT:
                    return
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        return
            screen.fill((50, 50, 50))
            game_menu.draw(screen)
            pygame.display.flip()

def end():
    '''End of the game.'''
    pygame.event.post(pygame.event.Event(pygame.QUIT,{}))


def options():
    '''Shows the options submenu.

    Thies method will be executed if the options option is selected in
    the general menu.'''

    screen = pygame.display.set_mode((640,480),DOUBLEBUF | HWSURFACE, 32)
    screen.fill((50, 100, 0))
    # It works identicall as the main menu but with more options to select
    game_menu = menu.Menu([
			#[text, variable_name, colour, [min, max, step, actual_value, sign]]
            ["Players", "PLAYERS", c.NORMAL, [2,3,1,c.PLAYERS, '']],
            ["Stage", "STAGE", c.NORMAL, [0,len(c.STAGES)-1,1,c.STAGE,'']],
            ["Spawn time", "SPAWN_TIME", c.NORMAL, [0,3,1,c.SPAWN_TIME,' s']],
            ["Goals", "GOALS", c.NORMAL, [1,10,1,c.GOALS,'']],
            ["Hunting time", "HUNTING_TIME", c.NORMAL, [20,60,5,c.HUNTING_TIME,' s']],
            ["Maximum FPS", "FPS", c.NORMAL, [20,60,5,c.FPS,'']],
            ["Back to Menu", end, c.END, None]], c)
    game_menu.center_at(320, 200)
    loop(game_menu, screen)

if __name__ == "__main__":
    c = Container()
    start(c)
