import imp
import pygame
class Bullet():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=50
        self.height=20
        self.boom=False
        self.speed=10
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.image=pygame.image.load(r'image/connanball.png')
        self.image=pygame.transform.scale(self.image,(self.width, self.height))
    def update(self,width):
        self.x+=self.speed
        self.rect.x=self.x
        if(self.rect.bottom<=0 or self.x>=width):
            self.boom=True
    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)

