import sys
import pygame


def keyup_event(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False

def keydown_event(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True

def check_events(ai_settings, screen, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, player)
        elif event.type == pygame.KEYUP:
            keyup_event(event, player)

def update_screen(ai_settings, screen, player):
    # Draw / render
    screen.fill(ai_settings.bg_color)
    player.blitme()
    pygame.display.flip()