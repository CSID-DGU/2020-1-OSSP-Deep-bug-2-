#!/usr/bin/env python


#-*- coding: utf-8 -*-
import pygame
from random import randint
from time import sleep
import sys
from datetime import datetime
from pandas import read_csv
import csv


pygame.init()
## 게임 화면 크기 지정
size = (800, 600)
screen = pygame.display.set_mode(size)

## 컬러지정
yellow = (250, 250, 20)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
orange = (255,127,0)
blue = (0,0,225)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_orange = (255,215,0)

display_color = (255, 255, 255)

## 게임 속도(fps)지정
clock = pygame.time.Clock()
clock.tick(60)

## 키보드 연속입력
pygame.key.set_repeat(1,1)

## 파일 경로 지정
#file_path = "C:/Users/user_pc/Documents/GitHub/2020-1-OSSP1-Deepbug-2/Dodge-game/"
file_path = "/home/wj/OSSP/Dodge-game/"
#file_path = "C:/Users/82109/Documents/GitHub/2020-1-OSSP1-Deepbug-2/Dodge-game/"
#file_path = "/home/dohee/master/Dodge-game/"
#file_path = "C:/Users/82109/Documents/GitHub/2020-1-OSSP1-Deepbug-2/Dodge-game/"


## 이미지
# 배경, 인트로, button
background_image = pygame.image.load(file_path+"background.jpg").convert()
intro_image = pygame.image.load(file_path+"intro_image.jpg").convert()
pygame.display.set_caption("OSSP - DeepBug - Dodge v0.1.3")
help_image = pygame.image.load(file_path+"help_image.png")
arrow = pygame.image.load(file_path+"arrow.png")

# 비행기
playerimg1 = pygame.image.load(file_path+"type1.png")
playerimg2 = pygame.image.load(file_path+"type2-2.png")
playerimg3 = pygame.image.load(file_path+"type3-2.png")
playerimg4 = pygame.image.load(file_path+"type4-2.png")
playerimg11 = pygame.image.load(file_path+"type1_small.png")
playerimg22 = pygame.image.load(file_path+"type2_small.png")
playerimg33 = pygame.image.load(file_path+"type3_small.png")
playerimg44 = pygame.image.load(file_path+"type4_small.png")
playerdead = pygame.image.load(file_path+"explosion.png")

# 매뉴에 쓰는 비행기
type1_big = pygame.image.load(file_path+"type1_big.png")
type2_big = pygame.image.load(file_path+"type2_big.png")
type3_big = pygame.image.load(file_path+"type3_big.png")
type4_big = pygame.image.load(file_path+"type4_big.png")

# 아이템
itemimg1 = pygame.image.load(file_path+"speedup.png")
itemimg2 = pygame.image.load(file_path+"bomb.png")
itemimg3 = pygame.image.load(file_path+"item.png")

# 운석
fireball_w = pygame.image.load(file_path+"meteor_w.png")
fireball_r = pygame.image.load(file_path+"meteor_r.png")
fireball_p = pygame.image.load(file_path+"meteor_p.png")
fireball_g = pygame.image.load(file_path+"meteor_g.png")
fireball_w_big = pygame.image.load(file_path+"meteor_w_big.png")
fireball_r_big = pygame.image.load(file_path+"meteor_r_big.png")
fireball_p_big = pygame.image.load(file_path+"meteor_p_big.png")
fireball_g_big = pygame.image.load(file_path+"meteor_g_big.png")

# 도움말 이미지
menual = pygame.image.load(file_path+"help.png")

# 음소거 버튼 이미지
mute = pygame.image.load(file_path+"mute.png")
play_sound = pygame.image.load(file_path+"play.png")

# 게임 내에 text를 넣을때 쓰는 함수
def draw_text(text,font,surface,x,y,main_color) :
    text_obj = font.render(text,True,main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj,text_rect)

def text_objects(text, font):
    textSurface = font.render(text, True, (white))
    return textSurface, textSurface.get_rect()

# 일시정지 함수
def paused():
    transp_surf = pygame.Surface(size)
    transp_surf.set_alpha(1)
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects("PAUSED",largeText)
    TextRect.center = ((size[0]/2),(size[1]/3))
    default_font = pygame.font.SysFont('Gill Sans', 30)
    draw_text("Press 'c' to continue",default_font,screen,400,400,white)
    
    pause = True
    while pause:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_c :
                    pause = False
                elif event.key == pygame.K_q :
                    pygame.quit()
                    sys.exit()     
        screen.blit(transp_surf,transp_surf.get_rect())
        screen.blit(TextSurf, TextRect)
        draw_text("Press 'c' to continue",default_font,screen,400,400,white)
        button_img(help_image,705,25,70,70,help_ex)
        button("Menu",360,450,100,40,green,black,game_intro)
        button("Quit",530,450,100,40,green,black,quit_game)
        if choose == 1:
            button("Restart",150,450,140,40,green,black,game_loop) 
        elif choose == 2:
            button("Restart",150,450,140,40,green,black,game_loop2)
        pygame.display.update()
        clock.tick(10)

# 음소거 함수
def muted() :
    pygame.mixer.pause()
def sound_play() :
    pygame.mixer.unpause()

# 도움말 함수
def help_ex():
    global v
    screen.blit(menual, (0,0))
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    v = v - 0.005
                    if v < 0 :
                        v = 0
                explosion_sound.set_volume(v)
                item_sound.set_volume(v)
                whilegame.set_volume(v)
                if event.key == pygame.K_2:
                    v = v + 0.005
                    if v > 1 :
                        v = 1
                explosion_sound.set_volume(v)
                item_sound.set_volume(v)
                whilegame.set_volume(v)

            button_img(arrow,705,25,70,70,game_intro)
        pygame.display.update()

## 비행기
class Player(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    width = 0
    height = 0
    mode = 0
    death = 0
    dead_time = 0

    # 초기 설정
    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.mode = mode

    # 비행기의 위치 조절
    def update(self):
        if self.death == 0:
            self.x += self.x_speed
            self.y += self.y_speed

            global p_img, p_img2
            if self.mode == 1:
                if p_img == 1:
                    self.width = 40
                    self.height = 39
                    screen.blit(playerimg1, (self.x, self.y))
                elif p_img == 2:
                    self.width = 38
                    self.height = 60
                    screen.blit(playerimg2, (self.x, self.y))
                elif p_img == 3:
                    self.width = 50
                    self.height = 30
                    screen.blit(playerimg3, (self.x, self.y))
                elif p_img == 4:
                    self.width = 70
                    self.height = 70
                    screen.blit(playerimg4, (self.x, self.y))
                elif p_img == 11:
                    self.width = 20
                    self.height = 20
                    screen.blit(playerimg11, (self.x, self.y))
                elif p_img == 22:
                    self.width = 20
                    self.height = 32
                    screen.blit(playerimg22, (self.x, self.y))
                elif p_img == 33:
                    self.width = 30
                    self.height = 18
                    screen.blit(playerimg33, (self.x, self.y))
                elif p_img == 44:
                    self.width = 35
                    self.height = 35
                    screen.blit(playerimg44, (self.x, self.y))
            elif self.mode == 2:
                if p_img2 == 1:
                    self.width = 40
                    self.height = 39
                    screen.blit(playerimg1, (self.x, self.y))
                elif p_img2 == 2:
                    self.width = 38
                    self.height = 60
                    screen.blit(playerimg2, (self.x, self.y))
                elif p_img2 == 3:
                    self.width = 50
                    self.height = 30
                    screen.blit(playerimg3, (self.x, self.y))
                elif p_img2 == 4:
                    self.width = 70
                    self.height = 70
                    screen.blit(playerimg4, (self.x, self.y))
                elif p_img2 == 11:
                    self.width = 20
                    self.height = 20
                    screen.blit(playerimg11, (self.x, self.y))
                elif p_img2 == 22:
                    self.width = 20
                    self.height = 32
                    screen.blit(playerimg22, (self.x, self.y))
                elif p_img2 == 33:
                    self.width = 30
                    self.height = 18
                    screen.blit(playerimg33, (self.x, self.y))
                elif p_img2 == 44:
                    self.width = 35
                    self.height = 35
                    screen.blit(playerimg44, (self.x, self.y))

    # 비행기가 화면 밖으로 벗어나는것 방지
    def left_bound(self):
        if self.x <= 0:
            self.x = 0
            self.x_speed = self.x_speed * -1
    def right_bound(self):
        if self.x > size[0] - self.width:
            self.x = size[0] - self.width
            self.x_speed = self.x_speed * -1
    def top_bound(self):
        if self.y <= 0:
            self.y = 0
            self.y_speed = self.y_speed * -1
    def bottom_bound(self):
        if self.y >= size[1] - self.height:
            self.y = size[1] - self.height
            self.y_speed = self.y_speed * -1
    def bound(self):
        self.left_bound()
        self.right_bound()
        self.top_bound()
        self.bottom_bound()

    # 비행기 충돌
    def rectangle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



# 운석과 아이템 나오는곳, 방향 정하는 함수
def side_direc(self):
        if self.side == 1:
            self.x = -60 # get to the left of the window
            self.y = randint(0, size[1]-self.height)
            if self.direction == 2:
                self.x_speed = 1.4142135623731*5/2
                self.y_speed = -1.4142135623731*5/2
            elif self.direction == 4:
                self.x_speed = 1.4142135623731*5/2
                self.y_speed = 1.4142135623731*5/2
            else:
                self.x_speed = 5
        elif self.side == 2:
            self.x = randint(0, size[0]-self.width)
            self.y = -60
            if self.direction == 1:
                self.x_speed = -1.4142135623731*5/2
                self.y_speed = 1.4142135623731*5/2
            elif self.direction == 3:
                self.x_speed = 1.4142135623731*5/2
                self.y_speed = 1.4142135623731*5/2
            else:
                self.y_speed = 5
        elif self.side == 3:
            self.x = size[0] + 60
            self.y = randint(0, size[1]-self.height)
            if self.direction == 2:
                self.x_speed = -1.4142135623731*5/2
                self.y_speed = -1.4142135623731*5/2
            elif self.direction == 4:
                self.x_speed = -1.4142135623731*5/2
                self.y_speed = 1.4142135623731*5/2
            else:
                self.x_speed = -5
        elif self.side == 4:
            self.x = randint(0, size[0]-self.width)
            self.y = size[1] + 60
            if self.direction == 1:
                self.x_speed = -1.4142135623731*5/2
                self.y_speed = -1.4142135623731*5/2
            elif self.direction == 3:
                self.x_speed = 1.4142135623731*5/2
                self.y_speed = -1.4142135623731*5/2
            else:
                self.y_speed = -5

### 운석
class Fireball(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    width = 40
    height = 39
    has_reached_limit = False #This will let us know if it can de-spawn
    side = 0
    col = 0
    direction = 0

    # 암석 스폰 위치&색
    def __init__(self):
        self.side = randint(1,4)
        # 1 - left # 2 - top # 3 - right # 4 - bottom
        self.col = randint(1,8)
        # 1 - white # 2 - red # 3 - puple # 4 - green # 5 - whitebig # 6 - redbig # 7 - pupplebig # 8 - greenbig
        self.direction = randint(1,4)
        side_direc(self)
            
    #암석 움직이는 파트
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        # 운석 색상 다양화
        if self.col == 1:
            screen.blit(fireball_w, (self.x, self.y))
        elif self.col == 2:
            screen.blit(fireball_r, (self.x, self.y))
        elif self.col == 3:
            screen.blit(fireball_p, (self.x, self.y))
        elif self.col == 4:
            screen.blit(fireball_g, (self.x, self.y))
        elif self.col == 5:
            self.width = 60
            self.height = 59
            screen.blit(fireball_w_big, (self.x, self.y))
        elif self.col == 6:
            self.width = 60
            self.height = 59
            screen.blit(fireball_r_big, (self.x, self.y))
        elif self.col == 7:
            self.width = 60
            self.height = 59
            screen.blit(fireball_p_big, (self.x, self.y))
        elif self.col == 8:
            self.width = 60
            self.height = 59
            screen.blit(fireball_g_big, (self.x, self.y)) 
        
        if self.side == 1 and self.x > size[0]:
            self.has_reached_limit = True
        if self.side == 2 and self.y > size[1]:
            self.has_reached_limit = True
        if self.side == 3 and self.x < -40:
            self.has_reached_limit = True
        if self.side == 4 and self.y < -40:
            self.has_reached_limit = True  
    # 운석 충돌
    def rectangle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

### 아이템
class Item(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    width = 40
    height = 39
    side = 0
    direction = 0
    item1_t = 0
    item3_t = 0
    exist = 0
    useing = 0
    mode = 0

    # 초기 생성위치
    def __init__(self,mode):
        self.side = randint(1,4)
        self.direction = randint(1,4)
        side_direc(self)
        self.mode = mode

    # 아이템 별 이동
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.mode == 1:
            screen.blit(itemimg1, (self.x, self.y))
        elif self.mode == 2:
            screen.blit(itemimg2, (self.x, self.y))
        elif self.mode == 3:
            screen.blit(itemimg3, (self.x, self.y))

        if self.x <= 0:
            self.x = 0
            self.x_speed = self.x_speed * -1
        if self.x > size[0] - self.width:
            self.x = size[0] - self.width
            self.x_speed = self.x_speed * -1
        if self.y <= 0:
            self.y = 0
            self.y_speed = self.y_speed * -1
        if self.y >= size[1] - self.height:
            self.y = size[1] - self.height
            self.y_speed = self.y_speed * -1

    # 아이템 충돌
    def rectangle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


## 게임진행
def game_loop():
    # 음악재생
    global v ,whilegame, explosion_sound, item_sound
    pygame.mixer.pause()
    pygame.mixer.music.stop()
    whilegame.set_volume(v)
    whilegame.play()    
    explosion_sound.set_volume(v)
    item_sound.set_volume(v)

    score = 0
    highscore = 0
    player = Player(size[0]/2, size[1]/2, 1)
    fireballs = []
    difficulty = 1.0    # 난이도(level)
    
    item1 = Item(1) # 비행기 5초간 이속증가 아이템
    item2 = Item(2) # 화면에 나온 운석 제거 아이템
    item3 = Item(3) # 비행기 5초간 크기 감소 아이템

    p_s = 2 # 비행기 속도

    global p_img

    speed = 1   # 게임 속도

    default_font = pygame.font.SysFont('Gill Sans', 28)
    default_font2 = pygame.font.SysFont('Gill Sans',13)
    screen.blit(background_image, [0, 0])

    player.update()
    pygame.display.update()

    # 랭킹구현
    if p_img == 1:
        with open(file_path+"highscore_type1.txt", "r") as f :
            highscore = f.read()
    elif p_img == 2:
        with open(file_path+"highscore_type2.txt", "r") as f :
            highscore = f.read()
    elif p_img == 3:
        with open(file_path+"highscore_type3.txt", "r") as f :
            highscore = f.read()
    elif p_img == 4:
        with open(file_path+"highscore_type4.txt", "r") as f :
            highscore = f.read()

    # 키 조작
    alive = True
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # 키조작, 'p' = pause, 'space_bar' = speed*2, ',' = sound donw, '.' = sound up
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.x_speed = p_s
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.x_speed = -p_s
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.y_speed = p_s
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.y_speed = -p_s
                if event.key == pygame.K_SPACE:
                    speed = 2
                if event.key == pygame.K_COMMA:
                    v = v - 0.005
                    if v < 0 :
                        v = 0
                explosion_sound.set_volume(v)
                item_sound.set_volume(v)
                whilegame.set_volume(v)
                if event.key == pygame.K_PERIOD:
                    v = v + 0.005
                    if v > 1 :
                        v = 1
                explosion_sound.set_volume(v)
                item_sound.set_volume(v)
                whilegame.set_volume(v)
                if event.key == pygame.K_p :
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.x_speed = 0
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    player.x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.y_speed = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.y_speed = 0
                if event.key == pygame.K_SPACE:
                    speed = 1

        screen.blit(background_image, [0, 0])
        draw_text('Score : {}'.format(score),default_font,screen,80,20,yellow)
        draw_text("High Score : "+str(highscore),default_font,screen,680,20,yellow)
        draw_text("Level : "+str(int(difficulty)),default_font,screen,380,20,yellow)
        draw_text('Volume : {}'.format(int(v*200)),default_font2,screen,40,590,white)

        player.bound()
        player.update()

        now = datetime.now()
        DateAndTime = now.strftime('%Y-%m-%d %H:%M:%S')

       # 아이템 생성
        if round(difficulty,1) != 1:
            if round(difficulty,1)%3 == 0:
            # 아이템1 생성
                item1.exist = 1
                item1.useing = 0
            # 아이템2 생성
            elif round(difficulty,1)%3 == 1:
                item2.exist = 1
                item2.useing = 0
            # 아이템3 생성
            elif round(difficulty,1)%3 == 2:
                item3.exist = 1
                item3.useing = 0

        # 아이템 1
        if item1.exist == 1 and item1.useing == 0:
            item1.update()
            if item1.rectangle().colliderect(player.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item1.exeist = 0
                item1.useing = 1
                item1.item1_t = pygame.time.get_ticks()
                p_s = 6

        # 아이템 2
        if item2.exist == 1 and item2.useing == 0:
            item2.update()
            if item2.rectangle().colliderect(player.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item2.exist = 0
                item2.useing = 1
                score += len(fireballs)
                difficulty += len(fireballs)*0.1
                fireballs = []
                item2 = Item(2)

        # 아이템 3
        if item3.exist == 1 and item3.useing == 0:
            item3.update()
            if item3.rectangle().colliderect(player.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item3.exeist = 0
                item3.useing = 1
                item3.item3_t = pygame.time.get_ticks()
                if p_img == 1:
                    p_img = 11
                elif p_img == 2:
                    p_img = 22
                elif p_img == 3:
                    p_img = 33
                elif p_img == 4:
                    p_img = 44
                
        # 운석
        if len(fireballs) < difficulty:
            fireballs.append(Fireball())

        for index, fireball in enumerate(fireballs):
            fireball.update()
            if fireball.rectangle().colliderect(player.rectangle()):
                pygame.mixer.Sound.play(explosion_sound)
                # 랭킹 갱신
                if p_img == 1 or p_img == 11:
                    with open(file_path+"score_type1.csv","a",newline='') as file1 :
                        writer = csv.writer(file1)
                        writer.writerow((score,DateAndTime))
                    if score > int(highscore) :
                        highscore = score
                    with open(file_path+"highscore_type1.txt", "w") as f :
                        f.write(str(highscore))
                elif p_img == 2 or p_img == 22:
                    with open(file_path+"score_type2.csv","a",newline='') as file2 :
                        writer = csv.writer(file2)
                        writer.writerow((score,DateAndTime))
                    if score > int(highscore) :
                        highscore = score
                    with open(file_path+"highscore_type2.txt", "w") as f :
                        f.write(str(highscore))
                elif p_img == 3 or p_img == 33:
                    with open(file_path+"score_type3.csv","a",newline='') as file3 :
                        writer = csv.writer(file3)
                        writer.writerow((score,DateAndTime))
                    if score > int(highscore) :
                        highscore = score
                    with open(file_path+"highscore_type3.txt", "w") as f :
                        f.write(str(highscore))
                elif p_img == 4 or p_img == 44:
                    with open(file_path+"score_type4.csv","a",newline='') as file4 :
                        writer = csv.writer(file4)
                        writer.writerow((score,DateAndTime))
                    if score > int(highscore) :
                        highscore = score
                    with open(file_path+"highscore_type4.txt", "w") as f :
                        f.write(str(highscore))

                pygame.mixer.music.stop()
                death_screen(score)

            if fireball.has_reached_limit:
                fireballs.pop(index)
                score += 1
                difficulty += 0.1

        pygame.display.update()

        if speed == 2:
            clock.tick(120)
        elif speed == 1:
            clock.tick(60)
        
        # 아이템 1
        if item1.useing == 1:
            now = pygame.time.get_ticks()
            if int(now - item1.item1_t) >= 5000:
                p_s = 2
                item1 = Item(1)

        # 아이템 3
        if item3.useing == 1:
            now = pygame.time.get_ticks()
            if int(now - item3.item3_t) >= 5000:
                if p_img == 11:
                    p_img = 1
                elif p_img == 22:
                    p_img = 2
                elif p_img == 33:
                    p_img = 3
                elif p_img == 44:
                    p_img = 4
                item3 = Item(3)
        
# 게임진행 2p일때
def game_loop2():
    global v, whilegame, explosion_sound, item_sound
    pygame.mixer.pause()
    pygame.mixer.music.stop()
    whilegame.set_volume(v)
    whilegame.play()  
    explosion_sound.set_volume(v)
    item_sound.set_volume(v)

    score = 0
    highscore=0

    player = Player(size[0]/3, size[1]/2, 1)
    player_2 = Player(size[0]*2/3, size[1]/2, 2)

    fireballs = []
    difficulty = 1.0

    item1 = Item(1)
    item2 = Item(2)
    item3 = Item(3)

    p_s1 = 2
    p_s2 = 2

    global p_img, p_img2

    speed = 1

    # 랭킹구현
    with open(file_path+"highscore_2P.txt", "r") as f :
        highscore = f.read()

    default_font = pygame.font.SysFont('Gill Sans', 28)
    default_font2 = pygame.font.SysFont('Gill Sans',13)
    screen.blit(background_image, [0, 0])

    player.update()
    player_2.update()
    pygame.display.update()

    alive = True
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 1p키, 2p키 분할               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_2.x_speed = p_s2
                if event.key == pygame.K_LEFT:
                    player_2.x_speed = -p_s2
                if event.key == pygame.K_DOWN:
                    player_2.y_speed = p_s2
                if event.key == pygame.K_UP:
                    player_2.y_speed = -p_s2
                if event.key == pygame.K_COMMA:
                    v = v - 0.005
                    if v < 0 :
                        v = 0
                explosion_sound.set_volume(v)
                item_sound.set_volume(v)
                whilegame.set_volume(v)
                if event.key == pygame.K_PERIOD:
                    v = v + 0.005
                    if v > 1 :
                        v = 1
                explosion_sound.set_volume(v)
                item_sound.set_volume(v)
                whilegame.set_volume(v)
                if event.key == pygame.K_d:
                    player.x_speed = p_s1
                if event.key == pygame.K_a:
                    player.x_speed = -p_s1
                if event.key == pygame.K_s:
                    player.y_speed = p_s1
                if event.key == pygame.K_w:
                    player.y_speed = -p_s1
                if event.key == pygame.K_p :
                    paused()    
                if event.key == pygame.K_SPACE:
                    speed = 2
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player_2.x_speed = 0
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    player.x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_2.y_speed = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.y_speed = 0
                if event.key == pygame.K_SPACE:
                    speed = 1

        screen.blit(background_image, [0, 0])
        draw_text('Score : {}'.format(score),default_font,screen,80,20,yellow)
        draw_text("High Score : "+str(highscore),default_font,screen,680,20,yellow)
        draw_text("level : "+str(int(difficulty)),default_font,screen,380,20,yellow)
        draw_text('Volume : {}'.format(int(v*200)),default_font2,screen,40,590,white)
        player.bound()
        player_2.bound()
        player.update()
        player_2.update()

        now = datetime.now()
        DateAndTime = now.strftime('%Y-%m-%d %H:%M:%S')

        # 아이템 생성
        if round(difficulty,1) != 1:
            if round(difficulty,1)%3 == 0:
            # 아이템1 생성
                item1.exist = 1
                item1.useing = 0
            # 아이템2 생성
            elif round(difficulty,1)%3 == 1:
                item2.exist = 1
                item2.useing = 0
            # 아이템3 생성
            elif round(difficulty,1)%3 == 2:
                item3.exist = 1
                item3.useing = 0

        ## 아이템 1
        if item1.exist == 1 and item1.useing == 0:
            item1.update()
            if player.death == 0 and item1.rectangle().colliderect(player.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item1.exeist = 0
                item1.useing = 1
                item1.item1_t = pygame.time.get_ticks()
                p_s1 = 6
            if player_2.death == 0 and item1.rectangle().colliderect(player_2.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item1.exeist = 0
                item1.useing = 1
                item1.item1_t = pygame.time.get_ticks()
                p_s2 = 6

        ## 아이템 2
        if item2.exist == 1 and item2.useing == 0:
            item2.update()
            if (player.death == 0 and item2.rectangle().colliderect(player.rectangle())) or (player_2.death == 0 and item2.rectangle().colliderect(player_2.rectangle())):
                pygame.mixer.Sound.play(item_sound)
                item2.exist = 0
                item2.useing = 1
                score += len(fireballs)
                difficulty += len(fireballs)*0.1
                fireballs = []
                item2 = Item(2)

        ## 아이템 3
        if item3.exist == 1 and item3.useing == 0:
            item3.update()
            if player.death == 0 and item3.rectangle().colliderect(player.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item3.exeist = 0
                item3.useing = 1
                item3.item3_t = pygame.time.get_ticks()
                if p_img == 1:
                    p_img = 11
                elif p_img == 2:
                    p_img = 22
                elif p_img == 3:
                    p_img = 33
                elif p_img == 4:
                    p_img = 44
            if player_2.death == 0 and item3.rectangle().colliderect(player_2.rectangle()):
                pygame.mixer.Sound.play(item_sound)
                item3.exeist = 0
                item3.useing = 1
                item3.item3_t = pygame.time.get_ticks()
                if p_img2 == 1:
                    p_img2 = 11
                elif p_img2 == 2:
                    p_img2 = 22
                elif p_img2 == 3:
                    p_img2 = 33
                elif p_img2 == 4:
                    p_img2 = 44
                
        # 운석
        if len(fireballs) < difficulty:
            fireballs.append(Fireball())

        for index, fireball in enumerate(fireballs):
            fireball.update()

            if fireball.rectangle().colliderect(player.rectangle()):
                player.death = 1
                player.dead_time = pygame.time.get_ticks()
            elif fireball.rectangle().colliderect(player_2.rectangle()):
                player_2.death = 1
                player_2.dead_time = pygame.time.get_ticks()

            if player.death == 1 & player_2.death == 1:
                pygame.mixer.Sound.play(explosion_sound)
               # 랭킹 갱신
                with open(file_path+"score_2P.csv","a",newline='') as file2P :
                    writer = csv.writer(file2P)
                    writer.writerow((score,DateAndTime))
                if score > int(highscore) :
                    highscore = score
                with open(file_path+"highscore_2P.txt", "w") as f :
                    f.write(str(highscore))

                pygame.mixer.music.stop()
                death_screen(score)

            elif player.death == 1:          
                screen.blit(playerdead, (player.x, player.y))
                if (player.x-20 <= player_2.x <= player.x+20) and (player.y-20 <= player_2.y <= player.y+20):
                    now = pygame.time.get_ticks()
                    if int(now - player.dead_time) >= 3000:
                        player.death = 0
                else:
                    now=0

            elif player_2.death == 1:
                screen.blit(playerdead, (player_2.x, player_2.y))
                if (player_2.x-20 <= player.x <= player_2.x+20) and (player_2.y-20 <= player.y <= player_2.y+20):
                    now = pygame.time.get_ticks()
                    if int(now - player_2.dead_time) >= 3000:
                        player_2.death = 0
                else :
                    now = 0

            if fireball.has_reached_limit:
                fireballs.pop(index)
                score += 1
                difficulty += 0.1

        pygame.display.update()

        if speed == 2:
            clock.tick(120)
        elif speed == 1:
            clock.tick(60)
        
        # 아이템 1
        if item1.useing == 1:
            now = pygame.time.get_ticks()
            if int(now - item1.item1_t) >= 5000:
                p_s1 = 2
                p_s2 = 2
            item1 = Item(1)

        # 아이템 3
        if item3.useing == 1:
            now = pygame.time.get_ticks()
            if int(now - item3.item3_t) >= 5000:
                if p_img == 11:
                    p_img = 1
                elif p_img == 22:
                    p_img = 2
                elif p_img == 33:
                    p_img = 3
                elif p_img == 44:
                    p_img = 4
                elif p_img2 == 11:
                    p_img2 = 1
                elif p_img2 == 22:
                    p_img2 = 2
                elif p_img2 == 33:
                    p_img2 = 3
                elif p_img2 == 44:
                    p_img2 = 4  
                item3 = Item(3)

## 게임 매뉴 구성 부분
# 버튼 구현 함수
def button_img(img,x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    screen.blit(img,[x,y])

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
           action()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, ac,(x,y,w,h))

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
           action()

    smallText = pygame.font.SysFont("Gill Sans MT", 40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

# 1p 모드 선택창
def select_type():
    screen.blit(intro_image, [0, 0])

    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button("Type 1",275,250,95,50,green,black,start_game1_1)
            button("Type 2",430,250,95,50,green,black,start_game1_2)
            button("Type 3",275,450,95,50,green,black,start_game1_3)
            button("Type 4",430,450,95,50,green,black,start_game1_4)
            button_img(type1_big,260,140,120,120,start_game1_1)
            button_img(type2_big,415,140,120,120,start_game1_2)
            button_img(type3_big,260,340,120,120,start_game1_3)
            button_img(type4_big,415,340,120,120,start_game1_4)
            
        pygame.display.update()

# 2p모드 선택창
def select_type2():
    screen.blit(intro_image, [0, 0])
    select_font = pygame.font.SysFont('Gill Sans', 40)
    if choose == 1:
        draw_text('1P choose',select_font,screen,400,100,white)
    elif choose == 2:
        draw_text('2P choose',select_font,screen,400,100,white)

    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button("Type 1",275,250,95,50,green,black,start_game2_1)
            button("Type 2",430,250,95,50,green,black,start_game2_2)
            button("Type 3",275,450,95,50,green,black,start_game2_3)
            button("Type 4",430,450,95,50,green,black,start_game2_4)
            button_img(type1_big,260,140,120,120,start_game2_1)
            button_img(type2_big,415,140,120,120,start_game2_2)
            button_img(type3_big,260,340,120,120,start_game2_3)
            button_img(type4_big,415,340,120,120,start_game2_4)

        pygame.display.update()

# 1p mode일때
def start_game1_1():
    global p_img
    p_img = 1
    main_screen()
def start_game1_2():
    global p_img
    p_img = 2
    main_screen()
def start_game1_3():
    global p_img
    p_img = 3
    main_screen()
def start_game1_4():
    global p_img
    p_img = 4
    main_screen()

# 2p mode 일때
def start_game2_1():
    global p_img, p_img2
    global choose
    if choose == 1:
        p_img = 1
        choose = 2
        select_type2()
    elif choose == 2:
        p_img2 = 1
        main_screen()
def start_game2_2():
    global p_img, p_img2
    global choose
    if choose == 1:
        p_img = 2
        choose = 2
        select_type2()
    elif choose == 2:
        p_img2 = 2
        main_screen()
def start_game2_3():
    global p_img, p_img2
    global choose
    if choose == 1:
        p_img = 3
        choose = 2
        select_type2()
    elif choose == 2:
        p_img2 = 3
        main_screen()
def start_game2_4():
    global p_img, p_img2
    global choose
    if choose == 1:
        p_img = 4
        choose = 2
        select_type2()
    elif choose == 2:
        p_img2 = 4
        main_screen()    

# 랭킹창 보여주기
def select_ranking():
    screen.blit(intro_image, [0, 0])

    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button("Type 1",275,200,95,50,green,black,show_ranking1)
            button("Tpye 2",430,200,95,50,green,black,show_ranking2)
            button("Type 3",275,400,95,50,green,black,show_ranking3)
            button("Type 4",430,400,95,50,green,black,show_ranking4)
            button("2P RANKING",310,480,180,50,green,black,show_ranking2P)
            button_img(type1_big,260,90,120,120,show_ranking1)
            button_img(type2_big,420,90,120,120,show_ranking2)
            button_img(type3_big,260,290,120,120,show_ranking3)
            button_img(type4_big,420,290,120,120,show_ranking4)

        pygame.display.update()

def show_ranking1():
    global p_img
    p_img = 1
    show_ranking()
def show_ranking2():
    global p_img
    p_img = 2
    show_ranking()
def show_ranking3():
    global p_img
    p_img = 3
    show_ranking()
def show_ranking4():
    global p_img
    p_img = 4
    show_ranking()
def show_ranking2P():
    global p_img
    p_img = 0
    show_ranking()

def show_ranking():
    screen.blit(intro_image, [0, 0])
    default_font = pygame.font.SysFont('Gill Sans', 28)
    global p_img
    if p_img == 1:
        f = read_csv(file_path+"score_type1.csv")
        f.columns=['score','time']
        f = f.sort_values(["score"],ascending=[False])
        f.to_csv(file_path+"score_type1.txt",index=False,header=None,sep="\n")
        f = open(file_path+"score_type1.txt")
    elif p_img == 2:
        f = read_csv(file_path+"score_type2.csv")
        f.columns=['score','time']
        f = f.sort_values(["score"],ascending=[False])
        f.to_csv(file_path+"score_type2.txt",index=False,header=None,sep="\n")
        f = open(file_path+"score_type2.txt")
    elif p_img == 3:
        f = read_csv(file_path+"score_type3.csv")
        f.columns=['score','time']
        f = f.sort_values(["score"],ascending=[False])
        f.to_csv(file_path+"score_type3.txt",index=False,header=None,sep="\n")
        f = open(file_path+"score_type3.txt")
    elif p_img == 4:
        f = read_csv(file_path+"score_type4.csv")
        f.columns=['score','time']
        f = f.sort_values(["score"],ascending=[False])
        f.to_csv(file_path+"score_type4.txt",index=False,header=None,sep="\n")
        f = open(file_path+"score_type4.txt")
    else:
        f = read_csv(file_path+"score_2P.csv")
        f.columns=['score','time']
        f = f.sort_values(["score"],ascending=[False])
        f.to_csv(file_path+"score_2P.txt",index=False,header=None,sep="\n")
        f = open(file_path+"score_2P.txt")

    for i in range(20) :
            if i%2 == 0 :
                scoring = f.readline()
                scoring = scoring.rstrip()
                draw_text("Score :"+scoring,default_font,screen,250,160+30+15*(i+1),white)
            elif i%2 == 1 :
                timing = f.readline()
                timing = timing.rstrip()
                draw_text(timing,default_font,screen,500,160+30+15*i,white)

    rank = True
    while rank:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            largeText = pygame.font.SysFont('Creepster-Regular.ttf', 90)
            TextSurf, TextRect = text_objects("RANKING",   largeText)
            TextRect.center = ((size[0]/2),(size[1]/(4.5)))
            screen.blit(TextSurf, TextRect)
            button("Menu",225,500,95,50,green,bright_green,game_intro)
            button("Ranking",325,500,150,50,orange,bright_orange,select_ranking)
            button("Quit",480,500,95,50,red,bright_red, quit_game)

        pygame.display.update()

## 게임 종료
def quit_game():
    pygame.quit()
    sys.exit()

## 게임 매뉴 선택
def game_intro():
    global v, whilegame, explosion_sound, item_sound, choose
    v = 0.4
    pygame.mixer.pause()
    pygame.mixer.music.stop()
    screen.blit(intro_image, [0, 0])
    whilegame = pygame.mixer.Sound(file_path+"whilegame.wav")  
    explosion_sound = pygame.mixer.Sound(file_path+"explosion.wav")
    item_sound = pygame.mixer.Sound(file_path+"item.wav")
    intro_sound = pygame.mixer.Sound(file_path+"intro.wav")
    intro_sound.set_volume(v)
    intro_sound.play()
    choose = 1

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_COMMA:
                    v = v - 0.005
                    if v < 0 :
                        v = 0
                intro_sound.set_volume(v)
                if event.key == pygame.K_PERIOD:
                    v = v + 0.005
                    if v > 1 :
                        v = 1
                intro_sound.set_volume(v)
                
            largeText = pygame.font.SysFont('Creepster-Regular.ttf', 100)
            TextSurf, TextRect = text_objects("Select Menu",   largeText)
            TextRect.center = ((size[0]/2),(size[1]/4))
            screen.blit(TextSurf, TextRect)

            button_img(help_image,705,25,70,70,help_ex)
            button("1 Play",300,230,200,50,green,blue,select_type)
            button("2 Play",300,300,200,50,green,bright_green,select_type2)
            button("Ranking",300,370,200,50,orange,bright_orange,select_ranking)
            button("Quit",300,440,200,50,red,bright_red, quit_game)
            button_img(mute,50,18,40,40,muted)
            button_img(play_sound,17,20,40,40,sound_play)

        pygame.display.update()

# 게임 시작전 화면    
def main_screen():
    screen.fill((0,0,0))
    messages = ["Let's Play!",
                "Ready?",
                "Watch out!",]
    message = messages[randint(0, len(messages) - 1)]
    text = pygame.font.SysFont('Gill Sans', 60)
    text_on_screen = text.render(message, True, (255, 255, 255))
    text_rect = text_on_screen.get_rect()
    text_rect.center = ((size[0]/2),(size[1]/2))
    screen.blit(text_on_screen, text_rect)
    pygame.display.update()
    sleep(2)
    
    global choose
    if choose == 2:
        game_loop2()
    else: 
        game_loop()

# 게임 오버 화면
def death_screen(score):
    screen.fill((0,0,0))
    text = pygame.font.SysFont('Gill Sans', 60)
    messages = ['Is it over yet?',
                'Is that all?',
                'Try harder...',]
    message = messages[randint(0,(len(messages)-1))]
    message_on_screen = text.render(message, True, (255, 255, 255))
    score_message = "Score: {}".format(score)
    score_on_screen = text.render(score_message, True, (255, 255, 255))
    message_rect = message_on_screen.get_rect()
    message_rect.center = ((size[0]/2),(size[1]/2 + 40))
    screen.blit(message_on_screen, message_rect)

    score_rect = score_on_screen.get_rect()
    score_rect.center = ((size[0]/2), (size[1]/2 - 40))
    screen.blit(score_on_screen, score_rect)

    pygame.display.update()
    sleep(2)

    dead()

# 게임 오버후 선택 화면
def dead():
    screen.blit(intro_image, [0, 0])
    
    global choose
    if choose == 2:
        choose = 1
        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                largeText = pygame.font.SysFont('Gill Sans', 90)
                TextSurf, TextRect = text_objects("ONE MORE?",   largeText)
                TextRect.center = ((size[0]/2),(size[1]/3))
                screen.blit(TextSurf, TextRect)

                button("Restart",150,300,200,50,green,bright_orange,select_type2)
                button("Menu",450,300,200,50,green,bright_green,game_intro)
                button("Quit",300,400,200,50,red,bright_red, quit_game)

            pygame.display.update()
    else: 
        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                largeText = pygame.font.SysFont('Gill Sans', 90)
                TextSurf, TextRect = text_objects("ONE MORE?",   largeText)
                TextRect.center = ((size[0]/2),(size[1]/3))
                screen.blit(TextSurf, TextRect)

                button("Restart",150,300,200,50,green,bright_orange,select_type)
                button("Menu",450,300,200,50,green,bright_green,game_intro)
                button("Quit",300,400,200,50,red,bright_red, quit_game)

            pygame.display.update()

# 프로그램 시작
game_intro()



