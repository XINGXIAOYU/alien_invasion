class Settings(object):
    def __init__(self):
        # screen setting
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # ship setting
        self.ship_speed_factor = 5
        # bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5;
