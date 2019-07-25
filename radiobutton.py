import pygame, sys, random, button
from pygame.locals import *

class radiobutton():
    def __init__(self,display,color,tickcolor,cx,cy,r, status=False):
        self.display = display
        self.cx = cx
        self.cy = cy
        self.r = r
        self.status = status
        self.color = color
        self.tickcolor = tickcolor
        self.rect = pygame.Rect(0,0,self.r*2,self.r*2)
        self.rect.center = (self.cx,self.cy)

    def onDraw(self):
        pygame.draw.circle(self.display, self.color, (self.cx,self.cy),self.r)
        if self.status:
            pygame.draw.circle(self.display, self.tickcolor, (self.cx, self.cy), self.r//2)

    def collidepoint(self,p):
        return self.rect.collidepoint(p)

    def onClick(self):
        self.status = not self.status
        return self.status