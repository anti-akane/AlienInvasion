# -*- coding: gbk -*-
import sys   
from setting import Setting
import pygame 
class AlienInvasion:
    def __init__(self):
        pygame.init()  
        self.setting=Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))  
        pygame.display.set_caption("Alien Invasion")  
        self.background = pygame.image.load(r'image\background.jpg').convert()
        self.background=pygame.transform.scale(self.background,(1200, 675))
    def run_game(self):

        while True:

            for envent in pygame.event.get():   
                if envent.type == pygame.QUIT:   
                    sys.exit()    
            self.screen.fill(self.setting.bg_color)
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()    
game=AlienInvasion()
game.run_game()





