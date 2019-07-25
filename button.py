import sys,pygame
from pygame.locals import *


class button(pygame.Surface):
    def __init__(self,caption,x,y, onClickFun, bgcolor, shadowcolor, display):
        self.caption = caption
        self.rect = pygame.Rect(x-100, y-25, 200, 50)
        self.onClickFun = onClickFun
        self.bgcolor= bgcolor
        self.shadowcolor = shadowcolor
        self.display = display

    def get_rect(self):
        return self.rect

    def collidepoint(self,p):
        return self.rect.collidepoint(p)

    def onDraw(self,mouse_pos, bool):
        if self.rect.collidepoint(mouse_pos) and bool:
            pygame.draw.rect(self.display, self.shadowcolor, (self.rect.x - 3, self.rect.y - 3, self.rect.width + 6, self.rect.height + 6),0)
        pygame.draw.rect(self.display, self.bgcolor, self.rect, 0)
        self.display.blit(self.caption,(self.rect.x + self.rect.width / 2 - self.caption.get_width() / 2, self.rect.y + self.rect.height / 2 - self.caption.get_height() / 2))

    def onClick(self):
        self.onClickFun()
