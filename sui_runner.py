import pygame
import csv
import math
import random
import os
import time
from pygame import mixer

#Name enter
print('____________________________')
uname = input('ENTER USERNAME : ')
print('____________________________')

curr_time = time.strftime("%H:%M:%S", time.localtime())

play_game = False


#Terminal menu
while True:
    print('\n1. PLAY GAME')
    print('2. VIEW HIGHSCORE')
    print('3. VIEW YOUR SCORES')
    print('4. EXIT')
    ch = input('\nENTER YOUR CHOICE : ')
    if ch == '1':
      play_game = True
      break

    elif ch == '2':
      highscore = 0
      highscore_name = ''
      with open('scores.csv','r') as fh:
        reader = csv.reader(fh)
        for rec in reader:
          if len(rec)!=0:
            if int(rec[1]) >= int(highscore):
              highscore = rec[1]
              highscore_name = rec[0]
        print('HIGHSCORE : ',highscore)
        print('( played by ',highscore_name,' at ',curr_time,' )')
        
    
    elif ch == '3':
        with open('scores.csv','r') as fh:
          reader = csv.reader(fh)
          print('YOUR SCORES')
          print('-----------')
          for rec in reader:
            if len(rec)!=0:
              if rec[0] == uname:
                print(rec[1], ' at ' , curr_time)
          

    elif ch == '4':
        os._exit(0)

    else:
      print('INVALID CHOICE!!')
      continue

if play_game:
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 60

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 700

    #create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #caption and dp
    pygame.display.set_caption("Endless Scroll")


    #load image
    bg = pygame.image.load("front.jpeg").convert()
    game_bg = pygame.image.load("bg.jpeg").convert()
    you_lose = pygame.image.load('lose.png').convert()
    bg_width = bg.get_width() 
    bg_rect = bg.get_rect()

    #game run status variable
    run = False

    # BGM

    menu_bgm = mixer.Sound('main menu.mp3')
    game_bgm = mixer.Sound('bg(4).mp3')
    if run == False :
        menu_bgm.play() 

    #define game variables

    scroll = 0
    FPS = 70


    tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

    #Score add
    def score_add(score):
      with open('scores.csv','a') as fh:
        writer = csv.writer(fh)
        writer.writerow([uname,score,curr_time])  
             
    #Event handler
    def event_handler():
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          os._exit()
          
        if event.type == pygame.KEYDOWN:                          #Keydown check
          if event.key == pygame.K_ESCAPE: 
            os._exit()



    #GAME OVER
    def game_over(score_value):
        game_bgm = mixer.Sound('game_over.mp3')
        game_bgm.play()
        pygame.display.flip()
        for i in range(3,0,-1):
          screen.blit(you_lose, (0, 0))
          score = font.render('YOU SCORED : ' + str(score_value), True, (0,0,0))
          screen.blit(score, (750, 600))
          exit_time = font.render('Game exits in  ' + str(i) +' sec', True, (0,0,0))
          screen.blit(exit_time, (750, 550))
          pygame.display.flip()
          event_handler()
          pygame.time.delay(1000)
        
                

        
            
    #draw scrolling background
    def infinite_scroll():
      global scroll
      for i in range(0, tiles):
        screen.blit(game_bg, (i * bg_width + scroll, 0))

      clock.tick(FPS)

      #scroll background
      scroll -= 5

      #reset scroll
      if abs(scroll) > bg_width:      #scroll = image width ==> image out of screen
        scroll = 0

    #Score
    def show_score(x, y,score):
        score = font.render('SCORE : ' + str(score), True, (0,0,0))
        screen.blit(score, (x, y))

    #collision 
    def isCollision(x1, y1, x2, y2):
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if distance < 30:
            return True
        else:
            return False


    #Opening screen

    count = 0
    startgame_x = 380
    startgame_y = 600
    while True:
      
      count+=1
      screen.blit(bg, (0, 0))
      screen.blit(bg, (bg_width, 0))

      font = pygame.font.Font('freesansbold.ttf', 45)

      if count%20 == 0:
        score = font.render('PRESS SPACE TO START ', True, (0, 0, 0))
        screen.blit(score, (startgame_x, startgame_y))
      else:
        score = font.render('PRESS SPACE TO START ', True, (128,128,128))
        screen.blit(score, (startgame_x, startgame_y))
      pygame.display.flip()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE: 
            os._exit()       
          if event.key == pygame.K_SPACE:
            run = True
            break                  
            
        if event.type == pygame.QUIT:
          os._exit()

      if run == False:
        continue
      else:
        break


    #-----------
    #Game screen
    #-----------
    #Sun
    sun = pygame.image.load('Sun.png')


    #player coordinates and variables
    player_x = 100
    player_y = 550
    y_change = 0 
    gravity = 2
    jump = False
    score = 0
    player = pygame.image.load('dadada.png')

    #Defender
    game_speed = 15
    interval = 1
    def_y = 550
    def_img = []
    def_x = []
    defender = pygame.image.load('331.png')

    for i in range(1000):
      if i%100 == 0:
        def_img.append(defender)
        def_x.append(random.randint(1280,1500))

    cnt = 1
    #Game loop
    while run:
        cnt+=1
        seconds = pygame.time.get_ticks()/1000
        #bg
        infinite_scroll()

        #bgm
        game_bgm.play()
      
        #Sprite - player
        screen.blit(player,(player_x,player_y))
        

        #player movement mechanics
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    os._exit()
                if event.key == pygame.K_SPACE and y_change == 0:
                    y_change = 30
                    jump = True
                    
                    
        if jump == True :
          player_y -= y_change
          y_change -= gravity

        if player_y > 550:
          player_y = 550
          y_change = 0
          jump = False

        
        #speed increase
        if seconds % 10 == 0:
          game_speed += 8
          FPS += 30
        
        #sun
        if cnt % 10 == 0:
          screen.blit(sun,(50,50))
        else:
          screen.blit(sun,(60,60))
        

        #Defenders
        i = 0
        if seconds% random.random() == 0:  
            screen.blit(def_img[i],(def_x[i],def_y)) 
            def_x[i] -= game_speed
            collision_enemy = isCollision(def_x[i], 550,100, player_y)
            if def_x[i] == player_x:
              score += 10
            if collision_enemy == True:
                break
                run = False
        else:
            screen.blit(def_img[i],(def_x[i],def_y)) 
            def_x[i] -= game_speed
            collision_enemy = isCollision(def_x[i], 550,100, player_y)
            if def_x[i] == player_x:
              score += 10
            if collision_enemy == True:
                game_bgm.stop()
                break
                run = False
            if def_x[i] < -100:
                def_x[i] = random.randint(1280,1500)
            
            i+=1

        show_score(1000, 80,int(seconds))

        pygame.display.flip()

    score_add(int(seconds))
    game_over(int(seconds))


    pygame.quit()
