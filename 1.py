import pygame, sys, random, button, radiobutton
from pygame.locals import *
from button import *
from radiobutton import radiobutton

WHITE =         (255,  255, 255)
BLACK =         (0,     0,    0)
RED =           (155,   0,    0)
BRIGHTRED =     (255,   0,    0)
GREEN =         (0,    155,   0)
BRIGHTGREEN =   (0,    255,   0)
BLUE =          (0,     0,  155)
NAVYBLUE =      (60,   60,   60)
BRIGHTBLUE =    (0,     0,  255)
YELLOW =        (155,  155,   0)
BRIGHTYELLOW =  (255,  255,   0)
GRAY =          (100,  100, 100)
ORANGE =        (255,  160,   0)
PURPLE =        (255,   0,  255)
CYAN =          (0,    255, 255)
DARKGRAY =      (40,    40,  40)
DARKGREEN =     (10,   100,  50)
LIGHTBLUE =     (104,  147, 238)
DARKBLUE =      (4,      3,  56)
WIDTH = 0
HEIGHT = 0
FPS = 40
BGCOLOR = ORANGE



def start_f():
    global SELECTED, ALIVE, selection_completed, change
    if (selection_completed):
        SELECTED = True
        ALIVE = True
        change = True


def option_f():
    global drawOptions,change
    drawOptions = True
    change=True


def back_f():
    global changed,back
    changed=True
    back= True


def enter_f():
    global enter
    enter = True


class fish(object):
    def __init__(self, spritedx, spritesx, x, y, deltax, deltay,Y_LIMIT, score_bonus, energy_bonus, boost_bonus, kill_effect,sound):
        self.spritedx = spritedx
        self.spritesx = spritesx
        self.sprite_u_dx = pygame.transform.rotate(self.spritedx, 35)
        self.sprite_d_dx = pygame.transform.rotate(self.spritedx, -35)
        self.sprite_u_sx = pygame.transform.rotate(self.spritesx, -35)
        self.sprite_d_sx = pygame.transform.rotate(self.spritesx, 35)
        self.x = x
        self.y = y
        if( x ==0):
            self.dirx = 1
        else:
            self.dirx = -1
        self.initial_steps = 8
        self.initial_dir = self.dirx
        self.diry = 0
        self.Y_LIMIT = Y_LIMIT
        self.deltax = deltax
        self.deltay = deltay
        self.score_bonus = score_bonus
        self.energy_bonus = energy_bonus
        self.boost_bonus = boost_bonus
        self.kill_effect = kill_effect
        self.sound = sound

    def draw(self):
        move = 0
        # change_dir indica se il pesce cambierà direzione o no
        change_dir = random.randint(0,4)
        if move ==0:
            if change_dir == 0:
                randx = random.choice((1,-1))
                self.dirx = randx
                if (self.initial_steps>0):
                    self.dirx = self.initial_dir
                    self.initial_steps -= 1
            if random.randint(0,2)==0:
                if self.diry ==0:
                    randy = random.choice((0,1,-1))
                elif self.diry == 1:
                    randy = random.choice((0,-1))
                else:
                    randy = random.choice((0,1))
                self.diry += randy

            self.x = self.x + self.deltax*self.dirx
            if (self.diry == 1):
                if self.y - self.deltay > YLIMIT+self.sprite_d_dx.get_height()/2 :
                    self.y = self.y - self.deltay
                else:
                    self.diry = random.choice((0,-1))
                    self.y = self.y + self.deltay*(-self.diry)
            elif self.diry == -1:
                if (self.y +self.deltay + self.sprite_d_sx.get_height()*1.5 < HEIGHT):
                    self.y = self.y + self.deltay
                else:
                    self.diry = random.choice((0,1))
                    self.y = self.y + self.deltay*(-self.diry)
        # movimento solo orizzontale
        if (self.diry == 0):
            # verso dx
            if self.dirx == 1:
                DISPLAYSURF.blit(self.spritedx, (self.x, self.y))
            # verso sx
            else:
                DISPLAYSURF.blit(self.spritesx, (self.x, self.y))
        else:
            # movimento in alto
            if (self.diry == 1):
                if self.dirx == 1:
                    DISPLAYSURF.blit(self.sprite_u_dx, (self.x, self.y))
                else:
                    DISPLAYSURF.blit(self.sprite_u_sx, (self.x, self.y))
            # movimento in basso
            else:
                if self.dirx == 1:
                    DISPLAYSURF.blit(self.sprite_d_dx, (self.x, self.y))
                else:
                    DISPLAYSURF.blit(self.sprite_d_sx, (self.x, self.y))


class seagull(object):
    def __init__(self, sprite1sx,sprite1dx,sprite2sx,sprite2dx):
        self.l = []
        self.r = []
        self.spritedx = sprite2dx
        self.spritesx = sprite2sx

        self.l.insert(0, sprite1sx)
        self.l.insert(1, sprite1sx)
        self.l.insert(2, sprite1sx)
        self.l.insert(3, sprite2sx)
        self.l.insert(4, sprite2sx)
        self.l.insert(5, sprite2sx)

        self.r.insert(0, sprite1dx)
        self.r.insert(1, sprite1dx)
        self.r.insert(2, sprite1dx)
        self.r.insert(3, sprite2dx)
        self.r.insert(4, sprite2dx)
        self.r.insert(5, sprite2dx)

        self.counter = 0
        self.diry = 0
        self.y = YLIMIT - sprite2dx.get_height()
        if(random.randint(0,1)==0):
            self.x = 0
            self.dirx= 1
        else:
            self.x = WIDTH-sprite2dx.get_width()-10
            self.dirx = -1

    def draw(self):
        #va da sx a dx
        if(self.dirx == 1):
            DISPLAYSURF.blit(self.r[self.counter],(self.x,self.y))
            self.x += self.r[1].get_width()/3
        else:
            DISPLAYSURF.blit(self.l[self.counter], (self.x, self.y))
            self.x -= self.l[1].get_width()/3
        if self.counter%2 == 0:
            self.y -= self.spritedx.get_width() /2
        else:
            self.y += self.spritedx.get_width()/2
        self.counter += 1
        self.counter= self.counter%self.l.__len__()


def clear(arr):
    for el in arr:
        if el.x >= WIDTH or el.x+el.spritesx.get_width() <= 0:
            arr.remove(el)


def eats(a,b):
    if (a.dirx == 1 and a.diry == 0):
        recta = pygame.Rect(a.x+a.spritedx.get_width()/1.5, a.y+a.spritedx.get_height()/4, a.spritedx.get_width()/3, a.spritedx.get_height()/3)
        if (VIEWFINDER): pygame.draw.rect(DISPLAYSURF, RED, recta, 1)
    elif( a.dirx == 1 and a.diry == 1):
        recta = pygame.Rect(a.x+a.spritedx.get_width()/1.5, a.y+a.spritedx.get_height()/4, a.spritedx.get_width()/3, a.spritedx.get_height()/3)
        if (VIEWFINDER): pygame.draw.rect(DISPLAYSURF, RED, recta, 1)
    elif (a.dirx == 1 and a.diry == -1):
        recta = pygame.Rect(a.x+a.sprite_d_dx.get_width()/1.5, a.y+a.spritedx.get_height()/4*3.5, a.sprite_d_dx.get_width()/4, a.spritedx.get_height()/3)
        if (VIEWFINDER): pygame.draw.rect(DISPLAYSURF, RED, recta, 1)
    elif (a.dirx == -1 and a.diry == 0):
        recta = pygame.Rect(a.x, a.y+a.spritesx.get_height()/4, a.spritesx.get_width()/3, a.spritesx.get_height()/3)
        if (VIEWFINDER): pygame.draw.rect(DISPLAYSURF, RED, recta, 1)
    elif (a.dirx == -1 and a.diry == 1):
        recta = pygame.Rect(a.x+30, a.y+a.spritesx.get_height()/4, a.spritesx.get_width()/3, a.spritesx.get_height()/3)
        if (VIEWFINDER): pygame.draw.rect(DISPLAYSURF, RED, recta, 1)
    else:
        recta = pygame.Rect(a.x+20, a.y+a.spritesx.get_height()/4*3.5, a.sprite_d_sx.get_width()/4, a.spritesx.get_height()/3)
        if (VIEWFINDER): pygame.draw.rect(DISPLAYSURF, RED, recta, 1)

    if (b.dirx == 1 and b.diry == 0):
        rectb = pygame.Rect(b.x+10,b.y+10,b.spritedx.get_width()-10,b.spritedx.get_height()-10)
    elif( b.dirx == 1 and b.diry == 1):
        rectb = pygame.Rect(b.x+10,b.y+10,b.spritedx.get_width()-10,b.spritedx.get_height()-10)
    elif (b.dirx == 1 and b.diry == -1):
        rectb = pygame.Rect(b.x+10, b.y+10, b.spritedx.get_width()-10, b.spritedx.get_height()-10)
    elif (b.dirx == -1 and b.diry == 0):
        rectb = pygame.Rect(b.x+10, b.y+10, b.spritesx.get_width()-10, b.spritesx.get_height()-10)
    elif (b.dirx == -1 and b.diry == 1):
        rectb = pygame.Rect(b.x+10, b.y+10, b.spritesx.get_width()-10, b.spritesx.get_height()-10)
    else:
        rectb = pygame.Rect(b.x+10, b.y+10, b.spritesx.get_width()-10, b.spritesx.get_height()-10)

    #pygame.draw.rect(DISPLAYSURF, RED, rectb, 1)
    if recta.colliderect(rectb) and ((a.dirx==1 and a.x+a.spritedx.get_width()>=b.x) or (a.dirx==-1 and a.dirx)):
        return True
    else:
        return False


def eat_animation(shark1, f):
    global SCORE
    f.sound.play()
    SCORE += f.score_bonus
    if (shark1.energy + f.energy_bonus) <= 100 and (shark1.energy + f.energy_bonus) >= 0:
        shark1.energy += f.energy_bonus
    elif (shark1.energy + f.energy_bonus) >= 0:
        shark1.energy = 100
    else:
        shark1.energy = 0
    if (shark1.boost + f.boost_bonus) <= 100:
        shark1.boost += f.boost_bonus
    else:
        shark1.boost = 100
    font = pygame.font.SysFont("Comic Sans MS", 30)
    if (f.energy_bonus >= 0):
        label = font.render(str(f.energy_bonus), 1, DARKGREEN)
    else:
        label = font.render(str(f.energy_bonus), 1, RED)
    DISPLAYSURF.blit(label, (f.x, f.y - 20))
    label1 = font.render(str(f.boost_bonus), 1, BLUE)
    DISPLAYSURF.blit(label1, (f.x + label.get_width() + 10, f.y - 20))
    DISPLAYSURF.blit(f.kill_effect, (f.x, f.y))


def spawn_fish(FISHES, effects, bite, shock, sprites):
    if FISHES.__len__() <12:
        if FISHES.__len__() >3:
            val = random.randint(0,5)
        else:
            val = random.randint(0,6)

        if val > 1:
            val = random.randint(0,6)
            if val == 0 or val ==1:
                fleft = sprites[0]
                FISHES.append(fish(fleft, fleft, random.choice((0, WIDTH - fleft.get_width() - 20)),
                                   random.randint(YLIMIT + fleft.get_height() + 50, HEIGHT - fleft.get_height() - 50), 8,
                                   4, YLIMIT, 0, -35, 0, effects[1], shock))
            elif (val == 2 or val == 3):
                fleft = sprites[1]
                fright = sprites[2]
                FISHES.append(fish(fright, fleft, random.choice((0,WIDTH-fleft.get_width()-20)),
                                   random.randint(YLIMIT+fleft.get_height()+50,HEIGHT-fleft.get_height()-50), 8,
                                   6, YLIMIT , 15, 15, 10, effects[0], bite))
            elif (val == 4 or val == 5):
                fleft = sprites[3]
                fright = sprites[4]
                FISHES.append(fish(fright, fleft, random.choice((0, WIDTH - fleft.get_width() - 30)),
                                   random.randint(YLIMIT + fleft.get_height() + 50, HEIGHT - fleft.get_height() - 50), 8,
                                   4, YLIMIT, 10, 10, 15, effects[0], bite))
            elif val == 6:
                fleft=sprites[5]
                fright=sprites[6]
                FISHES.append(fish(fright, fleft, random.choice((0, WIDTH - fleft.get_width() - 30)),
                                   random.randint(YLIMIT + fleft.get_height() + 50, HEIGHT - fleft.get_height() - 50), 25,
                                   10, YLIMIT, 30, 20, 15, effects[0], bite))


def spawn_seagull(SEAGULLS, seagull_1l, seagull_1r, seagull_2l, seagull_2r):
    SEAGULLS.append(seagull(seagull_1l,seagull_1r,seagull_2l,seagull_2r))


class shark(object):
    def __init__(self, spritedx, spritesx, x, y, deltax, deltay, Y_LIMIT, wave_l, wave_r):
        self.spritedx = spritedx
        self.spritesx = spritesx
        self.sprite_u_dx = pygame.transform.rotate(self.spritedx, 35)
        self.sprite_d_dx = pygame.transform.rotate(self.spritedx, -35)
        self.sprite_u_sx = pygame.transform.rotate(self.spritesx, -35)
        self.sprite_d_sx = pygame.transform.rotate(self.spritesx, 35)
        self.x = x
        self.y = y
        self.dirx = 1
        self.diry = 0
        self.Y_LIMIT = Y_LIMIT
        self.deltax = deltax
        self.deltay= deltay
        self.energy = 100
        self.boost = 100
        self.sprinting = 0
        self.jumping = False
        self.jump_power = 0
        self.wave_l = wave_l
        self.wave_r = wave_r
        self.wave_u_dx = pygame.transform.rotate(self.wave_r, 35)
        self.wave_d_dx = pygame.transform.rotate(self.wave_r, -35)
        self.wave_u_sx = pygame.transform.rotate(self.wave_l, -35)
        self.wave_d_sx = pygame.transform.rotate(self.wave_l, 35)

    def draw(self):
        global SCORE
        #se non sto saltando
        if not self.jumping:
            # movimento solo orizzontale
            if(self.diry == 0):
                # verso dx
                if self.dirx == 1:
                    DISPLAYSURF.blit(self.spritedx, (self.x, self.y))
                    if self.sprinting == 1 :
                        DISPLAYSURF.blit(self.wave_r, (self.x-self.wave_r.get_width()-10, self.y+self.spritedx.get_height()/3))
                #verso sx
                else:
                    DISPLAYSURF.blit(self.spritesx, (self.x, self.y))
                    if self.sprinting == 1 :
                        DISPLAYSURF.blit(self.wave_l, (self.x+self.spritesx.get_width()+10, self.y+self.spritedx.get_height()/3))
            else:
                #movimento in alto
                if(self.diry == 1):
                    if self.dirx == 1:
                        DISPLAYSURF.blit(self.sprite_u_dx, (self.x, self.y))
                        if self.sprinting == 1:
                            DISPLAYSURF.blit(self.wave_u_dx, (self.x - self.wave_u_dx.get_width()/2, self.y + self.sprite_u_dx.get_height()/3*2))
                    else:
                        DISPLAYSURF.blit(self.sprite_u_sx, (self.x, self.y))
                        if self.sprinting == 1:
                            DISPLAYSURF.blit(self.wave_u_sx, (self.x + self.sprite_u_sx.get_width()/4*3, self.y + self.sprite_u_sx.get_height()/3*2))
                #movimento in basso
                else:
                    if self.dirx == 1:
                        DISPLAYSURF.blit(self.sprite_d_dx, (self.x, self.y))
                        if self.sprinting == 1:
                            DISPLAYSURF.blit(self.wave_d_dx, (self.x - self.wave_d_dx.get_width()/2, self.y - self.wave_d_dx.get_height()/5))
                    else:
                        DISPLAYSURF.blit(self.sprite_d_sx, (self.x, self.y))
                        if self.sprinting == 1:
                            DISPLAYSURF.blit(self.wave_d_sx, (self.x + self.sprite_d_sx.get_width()/1.3, self.y - self.wave_d_sx.get_height()/5))
        #se sto saltando
        else:
            # se il salto è ancora in corso
            if self.jump_power >= -10:
                if self.boost >0:
                    self.boost -= 1
                if (self.x + self.deltax*self.dirx > 0 ) and (self.x + self.deltax*self.dirx + self.spritedx.get_width() < WIDTH - 75):
                    self.x += self.deltax * self.dirx
                neg = 1
                self.diry = -1
                if self.jump_power <0:
                    neg = -1
                    self.diry = -1
                self.y -= 10*(neg)*(-self.diry)
                self.jump_power -= 1
                if(self.jump_power >= 0 and self.dirx== 1):
                    self.diry = 1
                    DISPLAYSURF.blit(self.sprite_u_dx, (self.x, self.y))
                elif(self.jump_power < 0 and self.dirx== 1):
                    DISPLAYSURF.blit(self.sprite_d_dx, (self.x, self.y))
                elif(self.jump_power >= 0 and self.dirx== -1):
                    self.diry = 1
                    DISPLAYSURF.blit(self.sprite_u_sx, (self.x, self.y))
                else:
                    DISPLAYSURF.blit(self.sprite_d_sx, (self.x, self.y))
            #se il salto è terminato
            else:
                self.y = self.Y_LIMIT
                if(self.dirx== 1):
                    DISPLAYSURF.blit(self.sprite_u_dx, (self.x, self.y))
                else:
                    DISPLAYSURF.blit(self.sprite_u_sx, (self.x, self.y))
                self.jumping = False
        self.draw_stats()

    def draw_stats(self):
        if(self.energy >=50):
            color = GREEN
        elif(self.energy >=25):
            color = BRIGHTYELLOW
        else:
            color= BRIGHTRED
        font = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.draw.rect(DISPLAYSURF, color, (WIDTH//20, HEIGHT//15-15, 2*self.energy, 10))
        pygame.draw.rect(DISPLAYSURF, BLACK, (WIDTH//20*1-1, HEIGHT//15-16, 201, 11), 1)
        label = font.render("HEALTH", 1, BLACK)
        DISPLAYSURF.blit(label, (WIDTH//20, HEIGHT//15-40))
        label = font.render("SCORE:", 1, BLACK)
        DISPLAYSURF.blit(label, (WIDTH // 20 * 17, HEIGHT // 15 - 40))
        label = font.render(str(SCORE), 1, BLACK)
        DISPLAYSURF.blit(label, (WIDTH // 20 * 17, HEIGHT // 15 - 10))
        if (self.boost >= 30):
            color = BLUE
        else:
            color = RED
        pygame.draw.rect(DISPLAYSURF, color, (WIDTH // 20 , HEIGHT // 15*2-20, 2 * self.boost, 10))
        pygame.draw.rect(DISPLAYSURF, BLACK, (WIDTH // 20 - 1, HEIGHT // 15*2 - 21, 201, 11), 1)
        label = font.render("BOOST", 1, BLACK)
        DISPLAYSURF.blit(label, (WIDTH // 20, HEIGHT // 15*2 - 45))

    def move_r(self):
        if not self.jumping:
            self.dirx = 1
            self.diry = 0
            if self.x+self.deltax < WIDTH-self.spritedx.get_width()*1.5 and not self.jumping:
                self.x += (self.dirx*self.deltax)+ (10*self.sprinting)
                self.sprinting = 0
        self.draw()

    def move_l(self):
        if not self.jumping:
            self.dirx = -1
            self.diry = 0
            if self.x - self.deltax > 0 :
                self.x = self.x + (self.dirx*self.deltax) - (10*self.sprinting)
                self.sprinting = 0
        self.draw()

    def move_up(self):
        if not self.jumping:
            if self.y-self.deltay >= self.Y_LIMIT:
                self.diry = 1
                self.y = self.y - self.deltay - (10*self.sprinting)
                self.sprinting = 0
            elif self.sprinting == 1 and self.boost >= 25:
                self.jumping = True
                self.jump_power = 10
                self.diry = 1
                self.y = self.y - self.deltay - (10 * self.sprinting)
                self.sprinting = 0
            else:
                self.diry = 0
        self.draw()

    def move_down(self):
        if not self.jumping:
            if self.y+self.deltay < HEIGHT-self.spritedx.get_height()*1.5 and not self.jumping:
                self.diry = -1
                self.y += self.deltay + (10*self.sprinting)
                self.sprinting = 0
        self.draw()

    def resetposition(self):
        if not self.jumping:
            self.diry=0
            self.sprinting = 0

    def decrease_energy(self):
        global ALIVE
        if(self.energy>2):
            self.energy -= 2
        else:
            self.energy=0
            ALIVE = False

    def sprint(self):
        if self.boost >=1 and not self.jumping:
            self.boost -= 1
            self.sprinting = 1


def welcome_animation():
    logo = pygame.image.load("res/logo.png")
    logo = pygame.transform.scale(logo, (300, 200))
    logo_rect = logo.get_rect(center=(WIDTH/2,HEIGHT/2))
    text = pygame.image.load("res/txt.png")
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2- logo.get_height()/2- text.get_height()))
    DISPLAYSURF.fill(DARKBLUE)
    DISPLAYSURF.blit(logo, logo_rect)
    DISPLAYSURF.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(3000)


def lose_animation(shark, ocean,fishes, seagulls, enemys):
    if shark.dirx == 1:
        dead_shark = pygame.transform.rotate(shark.spritesx,180)
    else:
        dead_shark = pygame.transform.rotate(shark.spritedx,-180)
    while(shark.y+dead_shark.get_height()+30 < HEIGHT):
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(ocean, (-100, -HEIGHT * 0.3))
        clear(fishes)
        clear(seagulls)
        DISPLAYSURF.blit(dead_shark,(shark.x,shark.y))
        for fish in fishes:
            fish.draw()
        for seagull in seagulls:
            seagull.draw()
        for e in enemys:
            e.draw()
        shark.y += 30
        shark.draw_stats()
        pygame.display.update()
        pygame.time.delay(100)

    pygame.time.delay(1000)
    DISPLAYSURF.fill(BLACK)
    font = pygame.font.SysFont("Comic Sans MS", 120, 1,1)
    label = font.render("YOU LOSE!", 1, RED)
    DISPLAYSURF.blit(label, (WIDTH // 2 -label.get_width()//2, HEIGHT //2 - label.get_height()))
    pygame.display.update()
    pygame.time.delay(3000)


def update_score(scoreboard,score):
    global enter
    font = pygame.font.SysFont('Comicsans', 50)
    font1 = pygame.font.SysFont('Comicsans', 30)
    txt_your_score = "Your score :"
    txt_your_score = font.render(txt_your_score, 1 , WHITE)
    txt_score = str(score)
    txt_score = font.render(txt_score,1,BRIGHTGREEN)
    text = "Enter your name :"
    text = font.render(text,1,WHITE)
    enter = False
    typed = False
    name = ''
    mouse_pos=(0,0)
    start_click_pos = (0,0)
    change = True
    isin = False
    btt = button(font1.render("ENTER",1,BLACK), WIDTH / 2, HEIGHT - 300, enter_f,GRAY,DARKGRAY,DISPLAYSURF)
    while not (enter and typed):
        DISPLAYSURF.fill(DARKBLUE)
        DISPLAYSURF.blit(txt_your_score, (WIDTH/2-txt_your_score.get_width(), HEIGHT/3))
        DISPLAYSURF.blit(txt_score, (WIDTH/2+ 50, HEIGHT/3))
        DISPLAYSURF.blit(text, (WIDTH/2-txt_your_score.get_width(), HEIGHT/3+50))
        pygame.draw.rect(DISPLAYSURF, WHITE, (WIDTH/2+ text.get_width()/2,HEIGHT/3+50, 300, 30))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                start_click_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                change = True
                mouse_pos = event.pos
                if(btt.collidepoint(mouse_pos) and btt.collidepoint(start_click_pos)):
                    btt.onClick()
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
                tmp = btt.collidepoint(mouse_pos)
                if not isin == tmp:
                    isin = tmp
                    change = True
            if event.type== KEYDOWN:
                enter = False
                change = True
                if (event.unicode.isalpha() or event.unicode.isdigit()) and name.__len__()<15:
                    name += str(event.unicode)
                    typed = True
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                    typed = name.__len__()>0
        name_1 = font1.render(name, 1, RED)
        DISPLAYSURF.blit(name_1, (WIDTH / 2 + text.get_width() / 2 + 10, HEIGHT / 3 + 55))
        if change:
            btt.onDraw(mouse_pos, True)
            pygame.display.update()
        change = False

    if name in scoreboard:
        old_score = scoreboard[name]
        if score > old_score:
            scoreboard[name] = score
    else:
        scoreboard[name] = score


def draw_options_menu():
    global VIEWFINDER, back,changed
    back = False
    changed = True
    isin = False
    mouse_pos = (0, 0)
    start_click_pos = (0,0)
    x = WIDTH / 2 - 200
    y = HEIGHT / 2 - 200
    font = pygame.font.SysFont('Comicsans', 30)
    back_btt = button(font.render("BACK",1,BLACK),WIDTH / 2, y + 350, back_f,GRAY,DARKGRAY,DISPLAYSURF)
    text = font.render("Enable viewfinder :", 1, BLACK)
    cx = (int(x + 400 - 50))
    cy = int(y + 100 + text.get_height() / 2)
    rb = radiobutton(DISPLAYSURF, WHITE, BLACK, cx, cy, 15, VIEWFINDER)
    while not back:
        pygame.draw.rect(DISPLAYSURF,LIGHTBLUE, (x, y, 400,400))
        pygame.draw.rect(DISPLAYSURF,BLACK, (x-1, y-1, 401,401),2)
        DISPLAYSURF.blit(text, (x+50, y+100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP and event.key == K_ESCAPE:
                back = True
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
                tmp = back_btt.collidepoint(mouse_pos)
                if not isin == tmp:
                    changed = True
                    isin = tmp
            if event.type == MOUSEBUTTONDOWN:
                start_click_pos = event.pos
            if event.type== MOUSEBUTTONUP :
                mouse_pos = event.pos
                if back_btt.collidepoint(mouse_pos) and back_btt.collidepoint(start_click_pos):
                    back_btt.onClick()
                if rb.collidepoint(mouse_pos) and rb.collidepoint(start_click_pos):
                    changed = True
                    VIEWFINDER = rb.onClick()
        if changed:
            back_btt.onDraw(mouse_pos,True)
            rb.onDraw()
            pygame.display.update()
        changed = False



def main():
    global DISPLAYSURF, FPSCLOCK, WIDTH, HEIGHT, ALIVE, SCORE, YLIMIT, VIEWFINDER
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init()

    energy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(energy_timer, 750)
    spawn_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(spawn_timer, 1500)

    VIEWFINDER = False

    SCORE = 0
    pygame.mixer.music.load("res/s.mp3")
    bite = pygame.mixer.Sound('res/bite.ogv')
    shock = pygame.mixer.Sound('res/spark.ogv')

    fishes_sprites = []
    f = pygame.image.load("res/jelly.png")
    f = pygame.transform.scale(f, (70, 50))
    fishes_sprites.insert(0,f)
    fleft = pygame.image.load("res/fish0left.png")
    fright = pygame.image.load("res/fish0right.png")
    fleft = pygame.transform.scale(fleft, (80, 50))
    fright = pygame.transform.scale(fright, (80, 50))
    fishes_sprites.insert(1,fleft)
    fishes_sprites.insert(2,fright)
    fleft = pygame.image.load("res/fish1left.png")
    fright = pygame.image.load("res/fish1right.png")
    fleft = pygame.transform.scale(fleft, (50, 30))
    fright = pygame.transform.scale(fright, (50, 30))
    fishes_sprites.insert(3,fleft)
    fishes_sprites.insert(4,fright)
    fleft = pygame.image.load("res/fish3left.png")
    fright = pygame.image.load("res/fish3right.png")
    fleft = pygame.transform.scale(fleft, (120, 70))
    fright = pygame.transform.scale(fright, (120, 70))
    fishes_sprites.insert(5,fleft)
    fishes_sprites.insert(6,fright)

    seagull_1l = pygame.image.load("res/bird1l.png")
    seagull_1l = pygame.transform.scale(seagull_1l,(70,50))
    seagull_1r = pygame.image.load("res/bird1r.png")
    seagull_1r = pygame.transform.scale(seagull_1r,(70,50))
    seagull_2l = pygame.image.load("res/bird2l.png")
    seagull_2l = pygame.transform.scale(seagull_2l,(70,50))
    seagull_2r = pygame.image.load("res/bird2r.png")
    seagull_2r = pygame.transform.scale(seagull_2r,(70,50))

    SEAGULLS = []
    FISHES = []

    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h
    FPSCLOCK = pygame.time.Clock()

    YLIMIT = HEIGHT/4

    bg = pygame.image.load("res/bg.png")
    bg = pygame.transform.scale(bg, (int(WIDTH), int(HEIGHT)))

    shark1_right = pygame.image.load('res/shark1right.png')
    shark1_left = pygame.image.load('res/shark1left.png')
    shark1_right = pygame.transform.scale(shark1_right, (140, 90))
    shark1_left = pygame.transform.scale(shark1_left, (140, 90))

    shark2_right = pygame.image.load('res/shark2right.png')
    shark2_left = pygame.image.load('res/shark2left.png')
    shark2_right = pygame.transform.scale(shark2_right, (140, 90))
    shark2_left = pygame.transform.scale(shark2_left, (140, 90))

    shark3_right = pygame.image.load('res/shark3right.png')
    shark3_left = pygame.image.load('res/shark3left.png')
    shark3_right = pygame.transform.scale(shark3_right, (140, 90))
    shark3_left = pygame.transform.scale(shark3_left, (140, 90))

    shark4_right = pygame.image.load('res/shark4right.png')
    shark4_left = pygame.image.load('res/shark4left.png')
    shark4_right = pygame.transform.scale(shark4_right, (140, 90))
    shark4_left = pygame.transform.scale(shark4_left, (140, 90))

    enemy_shark_r = pygame.image.load('res/shark5right.png')
    enemy_shark_l = pygame.image.load('res/shark5left.png')
    enemy_shark_l = pygame.transform.scale(enemy_shark_l, (140, 90))
    enemy_shark_r = pygame.transform.scale(enemy_shark_r, (140, 90))
    ENEMYS = []

    wave_l = pygame.image.load('res/wave_right.png')
    wave_r = pygame.image.load('res/wave_left.png')
    ocean = pygame.image.load('res/ocean.png')
    blood = pygame.image.load('res/blood.png')
    blood = pygame.transform.scale(blood, (100,100))
    spark = pygame.image.load('res/spark.png')
    spark = pygame.transform.scale(spark, (60, 60))
    ocean = pygame.transform.scale(ocean, (int(WIDTH*1.2), int(HEIGHT*1.3)))
    wave_l = pygame.transform.scale(wave_l, (WIDTH//20, HEIGHT//20))
    wave_r = pygame.transform.scale(wave_r, (WIDTH//20, HEIGHT//20))

    DISPLAYSURF = pygame.display.set_mode((WIDTH-60, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Shark survive")
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(ocean, (-100, 0))

    pygame.mixer.music.play(-1)
    welcome_animation()
    pygame.event.clear()
    scoreboard = {}

    buttons = []
    f1  = pygame.font.SysFont('Comicsans', 30)
    start = button(f1.render("START",1,BLACK), WIDTH / 2, HEIGHT / 2, start_f,GRAY,DARKGRAY,DISPLAYSURF)
    options = button(f1.render("OPTIONS",1,BLACK), WIDTH / 2, HEIGHT / 2 + 100, option_f,GRAY,DARKGRAY,DISPLAYSURF)
    buttons.append(start)
    buttons.append(options)
    global selection_completed, ALIVE,SELECTED, change,selected, drawOptions
    ALIVE = False
    SELECTED = False

    while True:
        #selectionLoop
        clicked = None
        selected=None
        def_selected=None
        start_click_pos = (0,0)
        mouse_pos=(0,0)
        change = True
        isin = False
        drawOptions = False
        selection_completed = False
        if not pygame.mixer.get_busy():
            pygame.mixer.music.play(-1)
        while not SELECTED:
            font = pygame.font.SysFont('Comicsans', 30)
            pygame.time.delay(40)
            DISPLAYSURF.fill(BRIGHTBLUE)
            DISPLAYSURF.blit(bg, (0, 0))
            xdim = int(shark1_left.get_width()*1.5)
            ydim = int(shark1_left.get_height()*1.5*4)
            s = pygame.Surface((xdim, ydim))
            s.set_alpha(200)
            s.fill((100, 100, 100))
            xs = 100
            ys =  HEIGHT/2-s.get_height()/2
            DISPLAYSURF.blit(s, (xs,ys))
            txt = font.render("SHARKS :",1, RED)
            DISPLAYSURF.blit(txt,((xs+s.get_width()/2-txt.get_width()/2, ys+20)))

            ydim = int(shark1_left.get_height()*1.5)
            s1 = pygame.Surface((xdim, ydim))
            s1.set_alpha(200)
            s1.fill((100, 100, 100))
            DISPLAYSURF.blit(s1,(WIDTH/2-xdim/2, 150))
            font = pygame.font.SysFont('Comicsans', 20)
            txt = font.render("Select your shark by dragging it here :",1, BLACK)
            DISPLAYSURF.blit(txt,(WIDTH/2-txt.get_width()/2, 100))
            selection_rect = pygame.Rect(WIDTH/2-xdim/2,150,xdim,ydim)

            if scoreboard.__len__() > 0:
                font = pygame.font.SysFont('Comicsans', 50)
                lb = font.render("LEADERBOARD :",1, RED)
                s= pygame.Surface( (int(WIDTH-(WIDTH-lb.get_width()*1.5-20)-100),int(HEIGHT-(HEIGHT/5-20)-100)))
                s.set_alpha(200)
                s.fill((100,100,100))
                DISPLAYSURF.blit(s,(WIDTH-lb.get_width()*1.5-20, HEIGHT/5-20))
                DISPLAYSURF.blit(lb, (WIDTH-lb.get_width()*1.5, HEIGHT/5))
                font = pygame.font.SysFont('Comicsans', 25)
                i = 0
                l=sorted(scoreboard.items(), reverse=True, key=lambda x:x[1])
                l = l[:10]
                for el in l:
                    k = el[0]
                    v = el[1]
                    k = font.render(str(k),1,BLACK)
                    v = font.render(str(v),1,DARKGREEN)
                    DISPLAYSURF.blit(k, (WIDTH-lb.get_width()*1.5,HEIGHT/5+lb.get_height()+20+i*(20)))
                    DISPLAYSURF.blit(v, (WIDTH-lb.get_width()/2-v.get_width()/2,HEIGHT/5+lb.get_height()+20+i*(20)))
                    i += 1

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEMOTION:
                    mouse_pos = event.pos
                    if not clicked is None:
                        change=True
                    else:
                        tmp = False
                        for b in buttons:
                            if b.collidepoint(mouse_pos):
                                tmp=True
                        if not tmp == isin:
                            change = True
                            isin = tmp
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    start_click_pos = mouse_pos
                    if rects1.collidepoint(mouse_pos) and def_selected!=shark1_right:
                        clicked = (mouse_pos[0]-rects1.x, mouse_pos[1]-rects1.y)
                        selected=shark1_right
                        tmp_index = 1
                        change=True
                    if rects2.collidepoint(mouse_pos)and def_selected!=shark2_right:
                        clicked = (mouse_pos[0] - rects2.x, mouse_pos[1] - rects2.y)
                        selected=shark2_right
                        tmp_index = 2
                        change=True
                    if rects3.collidepoint(mouse_pos)and def_selected!=shark3_right:
                        clicked = (mouse_pos[0] - rects3.x, mouse_pos[1] - rects3.y)
                        selected=shark3_right
                        tmp_index = 3
                        change=True
                    if rects4.collidepoint(mouse_pos)and def_selected!=shark4_right:
                        clicked = (mouse_pos[0] - rects4.x, mouse_pos[1] - rects4.y)
                        selected=shark4_right
                        tmp_index = 4
                        change=True

                if event.type== MOUSEBUTTONUP :
                    mouse_pos = event.pos
                    for btt in buttons:
                        if btt.collidepoint(mouse_pos) and btt.collidepoint(start_click_pos):
                            btt.onClick()
                    if selection_rect.collidepoint(mouse_pos):
                        if(clicked!=None):
                            def_selected = selected
                            selection_completed = True
                            index = tmp_index
                    selected=None
                    clicked=None
                    change = True
            for btt in buttons:
                if change:
                    btt.onDraw(mouse_pos,selected is None)

            xdim = int(shark1_left.get_width() * 1.5)
            ydim = int(shark1_left.get_height() * 1.5 * 4)
            s = pygame.Surface((xdim, ydim))
            s.set_alpha(200)
            s.fill((100, 100, 100))
            xs = 100
            ys = HEIGHT / 2 - s.get_height() / 2
            if (def_selected!=shark1_right and selected != shark1_right):
                DISPLAYSURF.blit(shark1_right, (xs+s.get_width()/2-shark1_right.get_width()/2, ydim/4 +30 ))
                rects1 = pygame.Rect(xs+s.get_width()/2-shark1_right.get_width()/2,ydim/4 +30,shark1_right.get_width(),shark1_right.get_height())
            if (def_selected!=shark2_right and selected != shark2_right):
                DISPLAYSURF.blit(shark2_right, (xs+s.get_width()/2-shark1_right.get_width()/2, ydim/4*2 +30 ))
                rects2 = pygame.Rect(xs+s.get_width()/2-shark1_right.get_width()/2,ydim/4*2 +30,shark2_right.get_width(),shark2_right.get_height())
            if (def_selected!=shark3_right and selected != shark3_right):
                DISPLAYSURF.blit(shark3_right, (xs+s.get_width()/2-shark1_right.get_width()/2, ydim/4*3 +30 ))
                rects3 = pygame.Rect(xs+s.get_width()/2-shark1_right.get_width()/2,ydim/4*3 +30,shark3_right.get_width(),shark3_right.get_height())
            if ( def_selected!=shark4_right and  selected != shark4_right):
                DISPLAYSURF.blit(shark4_right, (xs+s.get_width()/2-shark1_right.get_width()/2, ydim +30 ))
                rects4 = pygame.Rect(xs+s.get_width()/2-shark1_right.get_width()/2,ydim+30,shark4_right.get_width(),shark4_right.get_height())
            if selection_completed:
                DISPLAYSURF.blit(def_selected,(selection_rect.x+selection_rect.width/2-def_selected.get_width()/2,selection_rect.y+selection_rect.height/2-def_selected.get_height()/2))
            if (selected != None ):
                DISPLAYSURF.blit(selected, (mouse_pos[0]-clicked[0],mouse_pos[1]-clicked[1]))
            if change:
                pygame.display.update()
            change = False
            if drawOptions:
                draw_options_menu()
                mouse_pos=(0,0)
                drawOptions = False
                change = True

        if index == 1:
            shark_right = shark1_right
            shark_left = shark1_left
        elif index == 2:
            shark_right = shark2_right
            shark_left = shark2_left
        elif index == 3:
            shark_right = shark3_right
            shark_left = shark3_left
        elif index == 4:
            shark_right = shark4_right
            shark_left = shark4_left

        pygame.mixer.music.stop()
        shark1 = shark(shark_right, shark_left, WIDTH / 2 - 25, HEIGHT / 5 * 4, 20, 10, YLIMIT, wave_l, wave_r)
        for i in range(0,4):
            spawn_fish(FISHES, (blood, spark), bite, shock, fishes_sprites)
        #mainloop
        while ALIVE :
            pygame.time.delay(40)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == energy_timer:
                    shark1.decrease_energy()
                if event.type == spawn_timer:
                    spawn_fish(FISHES, (blood, spark), bite, shock, fishes_sprites)
                    if (random.randint(0, 9) == 0):
                        spawn_seagull(SEAGULLS, seagull_1l, seagull_1r, seagull_2l, seagull_2r)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or  keys[pygame.K_DOWN] or keys[pygame.K_0] or keys[pygame.K_9] :
                if (keys[pygame.K_LEFT]):
                    shark1.move_l()
                if (keys[pygame.K_RIGHT]):
                    shark1.move_r()
                if (keys[pygame.K_UP]):
                    shark1.move_up()
                if (keys[pygame.K_DOWN]):
                    shark1.move_down()
                if (keys[pygame.K_a] and not (keys[pygame.K_RIGHT] and keys[pygame.K_LEFT])):
                    shark1.sprint()
                if (keys[pygame.K_0]):
                    shark1.boost = 100
                    shark1.energy = 100
                if (keys[pygame.K_9]):
                    shark1.boost = 0
                    shark1.energy = 0
            else:
                shark1.resetposition()

            DISPLAYSURF.fill(BGCOLOR)
            DISPLAYSURF.blit(ocean, (-100, -HEIGHT*0.3))
            shark1.draw()
            clear(FISHES)
            if FISHES.__len__()<2:
                for i in range (0,3):
                    spawn_fish(FISHES, (blood, spark), bite, shock, fishes_sprites)
            clear(SEAGULLS)
            clear(ENEMYS)
            ###
            for e in ENEMYS:
                for f in FISHES:
                    if eats(e,f) and f.spritedx != fishes_sprites[0]:
                        FISHES.remove(f)
                        DISPLAYSURF.blit(f.kill_effect, (f.x, f.y))
                if eats(e,shark1):
                    if shark1.energy >= e.energy_bonus:
                        shark1.energy -= e.energy_bonus
                    else:
                        shark1.energy=0
                    e.dirx = -e.dirx
                    DISPLAYSURF.blit(blood, (shark1.x,shark1.y))
                if eats(shark1,e):
                    ###
                    if (SCORE % 300 > (SCORE + f.score_bonus) % 300):
                        ENEMYS.append(
                            fish(enemy_shark_r, enemy_shark_l, random.choice((0, WIDTH - enemy_shark_l.get_width())),
                                 random.randint(YLIMIT, HEIGHT - enemy_shark_l.get_height() - 30), 15, 8, YLIMIT, 50,
                                 30, 50,
                                 blood, bite))
                    ###
                    eat_animation(shark1, e)
                    ENEMYS.remove(e)
                    break
                e.draw()
            ###
            for f in FISHES:
                if eats(shark1,f):
                    ###
                    if (SCORE % 300 > (SCORE + f.score_bonus) % 300):
                        ENEMYS.append(
                            fish(enemy_shark_r, enemy_shark_l, random.choice((0, WIDTH - enemy_shark_l.get_width())),
                                 random.randint(YLIMIT, HEIGHT - enemy_shark_l.get_height() - 30), 15, 8, YLIMIT, 50,
                                 30, 50,
                                 blood, bite))
                    ###
                    eat_animation(shark1,f)
                    FISHES.remove(f)
                else:
                    f.draw()

            for seagull in SEAGULLS:
                if eats(shark1, seagull):
                    bite.play()
                    pygame.time.delay(10)
                    ###
                    if (SCORE % 300 > (SCORE + 70) % 300):
                        ENEMYS.append(fish(enemy_shark_r, enemy_shark_l, random.choice((0,WIDTH-enemy_shark_l.get_width())), random.randint(YLIMIT,HEIGHT-enemy_shark_l.get_height()-30), 15, 8, YLIMIT, 50, 30, 50, blood, bite))
                    ###
                    SCORE += 70
                    font = pygame.font.SysFont("Comic Sans MS", 50)
                    label = font.render(str(70), 1, DARKGREEN)
                    DISPLAYSURF.blit(label, (seagull.x, seagull.y-30))
                    SEAGULLS.remove(seagull)
                    DISPLAYSURF.blit(blood, (seagull.x, seagull.y))
                else:
                    seagull.draw()

            pygame.display.update()
            FPSCLOCK.tick(FPS)
        lose_animation(shark1, ocean, FISHES, SEAGULLS, ENEMYS)
        pygame.event.clear()
        update_score(scoreboard,SCORE)
        SCORE=0
        FISHES.clear()
        SEAGULLS.clear()
        ENEMYS.clear()
        mouse_pos = (0,0)
        SELECTED= False
    pygame.quit()
    sys.exit()


if __name__ != 'main':
    main()