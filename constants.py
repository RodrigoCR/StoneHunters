import pygame
from pygame.locals import *

# This object holds special constant data like game
# configurations.
class Container:

    def __init__(self):
        self.FILE_NAME = 'settings.conf' # The file for saving configuration
        self.FIELD_SIZE = 35 # The size of each sector in the map

        self.STAGE = 0 # The current stage
        self.STAGES = [
					"stages/stage1.stg",
					"stages/stage2.stg",
					"stages/stage3.stg",
					"stages/stage4.stg",
					"stages/generated_stage.stg"
					]# Stages filenames

        self.GAME_SONG = pygame.mixer.Sound("sounds/audio-1.ogg") # Audio namefiles
        self.MENU_SONG = pygame.mixer.Sound("sounds/audio-2.ogg")

        self.PLAYERS = 3 # Number of players in game
        self.KEYS = [
					[K_w, K_a, K_s, K_d],
					[K_i, K_j, K_k, K_l],
					[K_UP, K_LEFT, K_DOWN, K_RIGHT]
					] # Keys for players movement

		# The menu colors (selected, unselected)
        self.MENU_COLOURS = [[[250, 250, 250], [170, 210, 170]],
                [[230, 230, 255], [50, 180, 250]],
                [[255, 230, 230], [255, 50, 80]]]

        # How the teams will be formed for each turn
        self.TEAM = [["A","B","B"],['B','A','B'],['B','B','A']]
        self.SPAWN_TIME = 0 # Time to wait before spawning again
        self.GOALS = 3 # Max number of stones to collect
        self.HUNTING_TIME = 30 # Hunting time for each turn
        self.FPS = 30 # Frames Per Second Rate

		# Constants for menu displaying
        self.NORMAL = 0
        self.OPTIONS = 1
        self.END = 2

		# We open the file and parse the info in each line
        f = open(self.FILE_NAME, 'r')
        for line in f:
            a,b = line.split()
            self.set_var(a,b)
        self.STEP = self.FIELD_SIZE/12

    def set_var(self, a,b):
        '''Check if a token is in the config file and change the actual value.'''
        
        if a == 'PLAYERS':
            self.PLAYERS = int(b)
        if a == 'SPAWN_TIME':
            self.SPAWN_TIME = int(b)
        if a == 'GOALS':
            self.GOALS = int(b)
        if a == 'HUNTING_TIME':
            self.HUNTING_TIME = int(b)
        if a == 'FPS':
            self.FPS = int(b)
        if a == 'FIELD_SIZE':
            self.FIELD_SIZE = int(b)
        if a == 'STAGE':
        	self.STAGE = int(b)

    def save_settings(self):
    	'''Save the current settings into the file.'''
    	
        f = open(self.FILE_NAME, 'w')
        f.write('PLAYERS '+str(self.PLAYERS))
        f.write('\nSPAWN_TIME '+str(self.SPAWN_TIME))
        f.write('\nGOALS '+str(self.GOALS))
        f.write('\nHUNTING_TIME '+str(self.HUNTING_TIME))
        f.write('\nFPS '+str(self.FPS))
        f.write('\nFIELD_SIZE '+str(self.FIELD_SIZE))
        f.write('\nSTAGE '+str(self.STAGE))
        f.close()
