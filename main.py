import pygame,random
from data.game import *
from data.intro import *
from data.end import *


pygame.init()
size = (610,510)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")


#
s_game_over = pygame.mixer.Sound("resources/sound/game_over.ogg")

#Genero los lugares de trabajo
screen_score = pygame.Rect(0, 0, size[0], 100)
screen_game = pygame.Rect(0,100,size[0],size[1] -100)
num_screen = 0
n_0, n_2, n_3= 0,0,0

while True:
    if num_screen == 0:
        #Menu principal
        if n_0 == 0:
            Main_menu(screen)
            n_0+=1
        num_screen = controles_main()

    elif num_screen == 1:
        #Juego
        pygame.mixer_music.stop()
        screen.fill([0,150,0])
        pygame.display.update()
        pygame.time.delay(500)
        num_screen,score = game_snake(screen,screen_score,screen_game)
        n_2 = 0


    elif num_screen == 2:
        #Game Over
        if n_2 == 0:
            s_game_over.play()
            efect(screen)
            draw_score(screen,score)
            pygame.time.delay(10)
        num_screen = controles_end()
        n_2+=1
        n_0 = 0

    elif num_screen == 3:
        # Game Over
        efect(screen)
        screen.fill([0,150,0])
        pygame.time.delay(500)
        text = draw_new_score(screen,score)
        write_datos(text, score)
        num_screen = 4

    elif num_screen == 4:
        draw_best_score(screen)
        num_screen = controles_score()
        n_0 = 0









