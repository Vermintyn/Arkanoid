'''Game Settings'''

class Settings():
    def __init__(self):

        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.fps = 60

        #Default colors
        self.player_color = (0, 255, 0)
        self.bg_color = (0,0,0)

        #PLayer
        self.player_speed_factor = 2