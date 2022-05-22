import pygame
import random

pygame.init()
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brush")
clock = pygame.time.Clock() #FPS

game_font = pygame.font.Font(None, 40)
bad_num = str(random.randint(1, 5))
good_num = str(random.randint(1, 5))

#배경
background = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/background.png")

#게임오버
gameover = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/gameover.png")

#캐릭터
character = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - (character_height * 2 + 30)

#캐릭터 이동
to_x = 0
character_speed = 0.5

#먹어야 하는 것
bad = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/bad"+bad_num+".png")
bad_size = bad.get_rect().size
bad_width = bad_size[0]
bad_height = bad_size[1]
bad_x_pos = random.randint(0, screen_width - bad_width)
bad_y_pos = 0
bad_speed = random.randint(20, 40) / 10

#안먹어도 되는 것
good = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/good"+good_num+".png")
good_size = good.get_rect().size
good_width = good_size[0]
good_height = good_size[1]
good_x_pos = random.randint(0, screen_width - good_width)
good_y_pos = 0
good_speed = random.randint(20, 40) / 10

#라이프 회복
toothbrush = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/toothbrush.png")
toothbrush_size = toothbrush.get_rect().size
toothbrush_width = toothbrush_size[0]
toothbrush_height = toothbrush_size[1]
toothbrush_x_pos = random.randint(0, screen_width - toothbrush_width)
toothbrush_y_pos = random.randint(-3000, -1000)
toothbrush_speed = random.randint(20, 40) / 10

#라이프
life_num = 5
life = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/life"+str(life_num)+".png")
life_size = life.get_rect().size
life_height = life_size[1]
life_x_pos = 0
life_y_pos = screen_height - life_height



running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #← 입력
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #→ 입력
                to_x += character_speed
                    
        if event.type == pygame.KEYUP: #키보드 입력 해제
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
               
    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    bad_y_pos += bad_speed
    if bad_y_pos > screen_height:
        bad_y_pos = -(bad_height / 2)
        bad_x_pos = random.randint(0, screen_width - bad_width)
        bad_speed = random.randint(20, 40) / 10
        bad_num = str(random.randint(1, 5))
        bad = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/bad"+bad_num+".png")
        life_num -= 1
        if life_num > 0:
            life = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/life"+str(life_num)+".png")
        
    good_y_pos += good_speed
    if good_y_pos > screen_height:
        good_y_pos = -(good_height / 2)
        good_x_pos = random.randint(0, screen_width - good_width) 
        good_speed = random.randint(20, 40) / 10
        good_num = str(random.randint(1, 5))
        good = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/good"+good_num+".png")
        
    toothbrush_y_pos += toothbrush_speed
    if toothbrush_y_pos > screen_height:
        toothbrush_y_pos = random.randint(-3000, -1000)
        toothbrush_x_pos = random.randint(0, screen_width - toothbrush_width)
        toothbrush_speed = random.randint(20, 40) / 10

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    bad_rect = bad.get_rect()
    bad_rect.left = bad_x_pos
    bad_rect.top = bad_y_pos
    
    good_rect = good.get_rect()
    good_rect.left = good_x_pos
    good_rect.top = good_y_pos
    
    toothbrush_rect = toothbrush.get_rect()
    toothbrush_rect.left = toothbrush_x_pos
    toothbrush_rect.top = toothbrush_y_pos
    
    #충돌
    if character_rect.colliderect(bad_rect):
        bad_y_pos = -(bad_height / 2)
        bad_x_pos = random.randint(0, screen_width - bad_width)
        bad_speed = random.randint(20, 40) / 10
        bad_num = str(random.randint(1, 5))
        bad = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/bad"+bad_num+".png")
        
    if character_rect.colliderect(good_rect):
        good_y_pos = -(good_height / 2)
        good_x_pos = random.randint(0, screen_width - good_width) 
        good_speed = random.randint(20, 40) / 10
        good_num = str(random.randint(1, 5))
        good = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/good"+good_num+".png")
        
    if character_rect.colliderect(toothbrush_rect):
        print("toothbrush와 충돌")
        toothbrush_y_pos = random.randint(-3000, -1000)
        toothbrush_x_pos = random.randint(0, screen_width - toothbrush_width)
        toothbrush_speed = random.randint(20, 40) / 10
        if life_num < 5:
            life_num += 1
        if life_num > 0:
            life = pygame.image.load("C:/Users/82103/Desktop/백석/3-1/파이썬 프로그래밍/팀프로젝트/images/life"+str(life_num)+".png")
        
        
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(bad, (bad_x_pos, bad_y_pos))
    screen.blit(good, (good_x_pos, good_y_pos))
    screen.blit(toothbrush, (toothbrush_x_pos, toothbrush_y_pos))
    screen.blit(life, (life_x_pos, life_y_pos))
    
    
    #게임 오버
    if life_num == 0:
        screen.blit(gameover, (0, 0))
        running = False

    
    pygame.display.update()
    
#딜레이
pygame.time.delay(5000)

pygame.quit()