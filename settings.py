class Settings:
    """A class to store all the settings for Space Invaders"""

    def __init__(self):
        """Initalize the game settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5