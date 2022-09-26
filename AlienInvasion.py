# -*- coding: gbk -*-
from email.headerregistry import Group
import sys 
from bullet import Bullet 
from setting import Setting
from ship import Ship
import pygame 
class AlienInvasion:
    def __init__(self):
        pygame.init()  
        self.setting=Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))  
        pygame.display.set_caption("Alien Invasion")  
        self.background = pygame.image.load(r'image\background.jpg').convert()
        self.background=pygame.transform.scale(self.background,(1200, 675))
        self.ship=Ship(self)
        self.clock=pygame.time.Clock()
        self.Bullets=[]
    def run_game(self):
        while True:
            self.clock.tick(60)
            self._check_event()   
            self._update_screen()
    def _check_event(self):
        for event in pygame.event.get():   
                if event.type == pygame.QUIT:   
                    sys.exit() 
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            self.ship._up_()
        if pressed_keys[pygame.K_s]:
            self.ship._down_()
        if pressed_keys[pygame.K_q]:
            sys.exit()
        if pressed_keys[pygame.K_SPACE]:
            if(self.ship.shoot()):
                new_Bullet=Bullet(self.ship.rect.centerx,self.ship.rect.centery)
                self.Bullets.append(new_Bullet)

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        self._update_bullet()
        pygame.display.flip() 
    def _update_bullet(self):
         for bullet in self.Bullets:
            bullet.update(self.screen.get_width())
            self.screen.blit(bullet.image,bullet.rect)
            if(bullet.boom):
                self.Bullets.remove(bullet)
game=AlienInvasion()
game.run_game()





