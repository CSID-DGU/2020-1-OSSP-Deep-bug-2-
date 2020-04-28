'''
ELLAK - Python lab
Avoid the Rocks v1.0.2
 '''
import pygame
import random
import time
import sys

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

# Load the background image
background_image = pygame.image.load("background.jpg").convert()

pygame.display.set_caption("ELLAK - Pyhton Course - Avoid The Rocks v1.0.2")
clock = pygame.time.Clock()
playerImg = pygame.image.load("spaceship.png")
fireballImg = pygame.image.load("meteor.png")

display_color = (255, 255, 255)

# 비행기 크기는 다르게 설정함. 크기에 따라 움직임이는 방법이 달라짐
# 비행기 속도는 일정, 아이템 먹을때만 빨라지거나 느려짐
class Player(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    speed_bonus = 0
    width = 40
    height = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y
# 비행기의 속도를 조절할 수 있는 요소
    def update(self):
        if self.x_speed > 0:
            self.x_speed += self.speed_bonus
        elif self.x_speed < 0:
            self.x_speed -= self.speed_bonus

        if self.y_speed > 0:
            self.y_speed += self.speed_bonus
        elif self.y_speed < 0:
            self.y_speed -= self.speed_bonus

        self.x += self.x_speed
        self.y += self.y_speed
        screen.blit(playerImg, (self.x, self.y))
# 비행기위 위치를 업데이트 하는 과정
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

    def rectangle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

#운석 속도는 레벨에 따라 점점 빨라지게
# 아이템 먹으면 빨라지거나 느려짐
class Fireball(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    width = 40
    height = 40
    has_reached_limit = False #This will let us know if it can de-spawn
    side = 0

    # 암석 스폰 위치
    def __init__(self):
        self.side = random.randint(1,4)
        # 1 - left
        # 2 - top
        # 3 - right
        # 4 - bottom

        # 왼쪽에서 스폰. 위아래는 랜덤출력. 운석의 속도는 10으로 고정
        # 그 밑에도 출력되는 방향만 다르고 나머진 동일
        if self.side == 1:
            self.x = -60 # get to the left of the window
            self.y = random.randint(0, size[1]-self.height)
            self.x_speed = 10

        elif self.side == 2:
            self.x = random.randint(0, size[0]-self.width)
            self.y = -60
            self.y_speed = 10

        elif self.side == 3:
            self.x = size[0] + 60
            self.y = random.randint(0, size[1]-self.height)
            self.x_speed = -10

        elif self.side == 4:
            self.x = random.randint(0, size[0]-self.width)
            self.y = size[1] + 60
            self.y_speed = -10
    #암석 속도 조절 파트
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        screen.blit(fireballImg, (self.x, self.y))
        if self.side == 1 and self.x > size[0]:
            self.has_reached_limit = True
        if self.side == 2 and self.y > size[1]:
            self.has_reached_limit = True
        if self.side == 3 and self.x < -40:
            self.has_reached_limit = True
        if self.side == 4 and self.y < -40:
            self.has_reached_limit = True

    def rectangle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# 게임 속도 조절 클래스 구현 필요



# 아이템 클래스 구현 필요
    # 비행기 속도 빨라지는 아이템

    # 운석속도 느려지는 아이템



# 랭킹 관련 클래스 구현 필요


# 2p 일떄 게임 따로 구현 필요
def game_loop():
    player = Player(size[0]/2, size[1]/2)
    fireballs = []
    difficulty = 1.0

    # 스코어 변수 스크린에 나타나도록 구현 필요
    score = 0

    # 게임 진행동안 배경
    screen.blit(background_image, [0, 0])

    player.update()
    pygame.display.update()

    base_time = time.time()
    current_time = time.time()
    elapsed_time = 0

    alive = True
    while alive:
        # 키입력 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.x_speed = 2
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.x_speed = -2
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.y_speed = 2
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.y_speed = -2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.x_speed = 0
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    player.x_speed = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.y_speed = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.y_speed = 0

        # 키 입력 받은 비행기 움직이도록 하는 코드
        screen.blit(background_image, [0, 0])

        player.bound()
        player.update()

        # 운석 나오게 하는 코드
        if len(fireballs) < difficulty:
            fireballs.append(Fireball())

        for index, fireball in enumerate(fireballs):
            fireball.update()

            # 운석과 충돌하여 게임 종료 코드
            if fireball.rectangle().colliderect(player.rectangle()):
                death_screen(score)

            # 운석이 사라질 경우 점수와 난이도 높이면서 진행
            if fireball.has_reached_limit:
                fireballs.pop(index)
                score += 1
                difficulty += 0.1
                player.speed_bonus += 0.01
                print (score)
                print (player.speed_bonus)

        pygame.display.update()
        clock.tick(50)

def main_screen():
    # 시작전 로딩화면 구현 필요
        # 사진 or 동영상

    # 게임 선택 매뉴화면 구현 필요
        # 게임시작 -> 비행기 선택 -> 게임시작
        # 2P 모드 -> 비행기 선택 -> 게임시작
        # 랭킹 확인 -> 매뉴로 되돌아가기
            # 매뉴에 따라서 다른 게임 시작, 랭킹 필요함


    # 게임 시작 로딩화면
    screen.fill((0,0,0))
    messages = ["Let's Play!",
                "Ready?",
                "Watch out!",]
    message = messages[random.randint(0, len(messages) - 1)]
    text = pygame.font.Font('freesansbold.ttf', 60)
    text_on_screen = text.render(message, True, (255, 255, 255))
    text_rect = text_on_screen.get_rect()
    text_rect.center = ((size[0]/2),(size[1]/2))
    screen.blit(text_on_screen, text_rect)
    pygame.display.update()
    time.sleep(2)

    # 게임 시작
    game_loop()

def death_screen(score):
    screen.fill((0,0,0))
    text = pygame.font.Font('freesansbold.ttf', 60)
    messages = ['Is it over yet?',
                'Is that all?',
                'Try harder...',]
    message = messages[random.randint(0,(len(messages)-1))]
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
    time.sleep(2)

    # 게임이 자동으로 재시작됨 -> 사용자가 재시작하도록 변경 필요
    main_screen()

main_screen()
