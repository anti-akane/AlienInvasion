import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image=pygame.image.load(r'image/lisailiu.png')
        self.rect=self.image.get_rect()
        self.rect.center=(100,300)
        self.y=300-self.rect.height/2
        self.x=100-self.rect.width/2
        self.speed=3
        self.ifmove=False
        self.shoot_cd=10
        self.shoot_clock=0
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def _up_(self):
        if(self.rect.y>10):
            self.y-=self.speed
            self.rect.y=self.y
    def _down_(self):
        if(self.rect.y<self.screen_rect.height-150):
            self.y+=self.speed
            self.rect.y=self.y
    def shoot(self):
        if(self.shoot_clock<self.shoot_cd):
            self.shoot_clock+=1
            return False
        else:
            self.shoot_clock=0
            return True

    