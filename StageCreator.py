#!/usr/bin/python
# coding: utf-8

# Author: Rodrigo Contreras Reyes

import pygame, sys
from pygame.locals import *

def start():
    '''Generates a map based in the draw on the screen to a file.'''
    pygame.init()
    cha_cod = ['S','F','W','B']
    cha_num = [0,0,0,0]
    cha_col = [(175,121,191),(210,228,140),(137,190,228),(212,114,87)]

	# This is the structure to save the map
    map_struct = [[0 for i in range(30)] for i in range(25)]
    for i in range(1,24):
        for j in range(1,29):
            map_struct[i][j] = 1

    cha_num[0] = 30*25 - 28*23
    cha_num[1] = 28*23

    screen = pygame.display.set_mode((30*20,25*20), DOUBLEBUF | HWSURFACE, 32)
    pygame.display.set_caption("StoneHunters [MAP CREATOR] - By RoCR [ To Gab ]")
    icon = pygame.image.load("images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)
    screen.fill((20, 20, 20))

    running = True
    font = pygame.font.Font("accid.ttf", 14)
    x, y = 1, 1

    while running:
    	# Event managing:
        events = pygame.event.get()
        if events:
            for e in events:
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                    if e.key == pygame.K_DOWN:
                        y += 1
                    if e.key == pygame.K_UP:
                        y -= 1
                    if e.key == pygame.K_LEFT:
                        x -= 1
                    if e.key == pygame.K_RIGHT:
                        x += 1
                    if e.key == pygame.K_SPACE:
                        cha_num[map_struct[y][x]] -= 1
                        if cha_num[3] == 0:
                            cha_num[3] += 1
                            map_struct[y][x] = 3
                        else:
                            map_struct[y][x] = (map_struct[y][x] + 1) % 4
                            cha_num[map_struct[y][x]] += 1
                    if e.key == pygame.K_s:
                        if cha_num[3] == 0:
                            cha_num[3] += 1
                            map_struct[y][x] = 3
                        else:
                            cha_num[map_struct[y][x]] -= 1
                            map_struct[y][x] = 0
                            cha_num[map_struct[y][x]] += 1

                    if e.key == pygame.K_f:
                        if cha_num[3] == 0:
                            cha_num[3] += 1
                            map_struct[y][x] = 3
                        else:
                            cha_num[map_struct[y][x]] -= 1
                            map_struct[y][x] = 1
                            cha_num[map_struct[y][x]] += 1

                    if e.key == pygame.K_w:
                        if cha_num[3] == 0:
                            cha_num[3] += 1
                            map_struct[y][x] = 3
                        else:
                            cha_num[map_struct[y][x]] -= 1
                            map_struct[y][x] = 2
                            cha_num[map_struct[y][x]] += 1

                    if e.key == pygame.K_b:
                        cha_num[map_struct[y][x]] -= 1
                        map_struct[y][x] = 3
                        cha_num[map_struct[y][x]] += 1
            if x < 1:
                x = 28
            if x > 28:
                x = 1
            if y < 1:
                y = 23
            if y > 23:
                y = 1

        for i in range(25):
            for j in range(30):
                pygame.draw.rect(screen, cha_col[map_struct[i][j]], (j*20,i*20,20,20))
                text = cha_cod[map_struct[i][j]]
                ren = font.render(text, 1, (20,20,20))
                screen.blit(ren,(j*20+8,i*20+2))
        for i in range(1,30):
            pygame.draw.line(screen, (20,20,20), (i*20, 0), (i*20, 500))
        for i in range(1,25):
            pygame.draw.line(screen,(20,20,20), (0,i*20), (600, i*20))

        draw_cursor(screen, x*20, y*20)
        pygame.display.flip()

	# Save the map info in to the file
    my_file = "generated_stage.stg"
    f = open(my_file, 'w')
    for i in range(25):
        for j in range(30):
            f.write(cha_cod[map_struct[i][j]])
        f.write('\n')
    f.close()

    sys.exit()

def draw_cursor(screen,x,y):
    '''Draws a red non-filled square to represent the cursor.'''
    pygame.draw.line(screen, (255, 0, 0), (x, y), (x+20, y))
    pygame.draw.line(screen, (255, 0, 0), (x, y), (x, y+20))
    pygame.draw.line(screen, (255, 0, 0), (x+20, y), (x+20, y+20))
    pygame.draw.line(screen, (255, 0, 0), (x, y+20), (x+20, y+20))

if __name__ == "__main__":
    start()
