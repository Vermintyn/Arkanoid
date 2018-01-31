#First project with Python created by Vermintyn

import pygame

from Game.settings import Settings
from Game.Player import Player
import game_functions as gf



'''Game loop'''
def run_game():

    ''' Game window initialization'''
    pygame.init()
    ai_settings = Settings()
    pygame.mixer.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Arkanoid v1.0")

    '''create'''
    player = Player(ai_settings, screen)


    while True:

        gf.check_events(ai_settings, screen, player)
        player.update()

        gf.update_screen(ai_settings, screen, player)

run_game()
