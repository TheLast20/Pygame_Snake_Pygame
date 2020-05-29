import pygame


#---------------------------------------------------------------------------------------------------------------
#Constante
S = [(115,30),(100,30),(85,30),(70,30),(55,30),
     (55,45),
     (55,60),
      (55,75),(70,75),(85,75),(100,75),(115,75),
     (115,90),
     (115,105),
     (115,120),(100,120),(85,120),(70,120),(55,120)]
N = [(160,120),(160,105),(160,90),(160,75),(160,60),
     (175,75),(190,90),(205,105),
     (220,120),(220,105),(220,90),(220,75),(220,60)]
A = [(265,120),(265,105),(265,90),(265,75),(265,60),
     (280,60),(295,60),(310,60),
    (3250,60),(325,75),(325,90),(325,105),(325,120),
    (280,90),(295,90),(310,90)]
K = [(370,120),(370,105),(370,90),(370,75),(370,60),
     (385,90),(400,90),(415,75,415,105),(430,120,430,60)]
E = [(475,120),(475,105),(475,90),(475,75),(475,60),
    (490,60),(505,60),(520,60),(535,60),
    (490,90),(505,90),(520,90),(535,60),
    (490,120),(505,120),(520,120),(535,120),]


def controles_main():
    num_screen = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                num_screen = 1

            if event.key == pygame.K_t:
                num_screen = 4

    return num_screen


def Grafico_Snake(screen):
    l_snake = S+N+A+K+E
    for x in l_snake:
        if len(x)==2:
            rect = pygame.Rect(x[0],x[1],15,15)
            pygame.draw.rect(screen,[210,210,0],rect)
            pygame.display.update()
            pygame.time.delay(30)
        else:
            rect1 = pygame.Rect(x[0],x[1],15,15)
            rect2 = pygame.Rect(x[2], x[3], 15, 15)
            pygame.draw.rect(screen,[210,210,0],rect1)
            pygame.draw.rect(screen,[210,210,0],rect2)
            pygame.display.update()
            pygame.time.delay(30)

def Main_menu(screen):
    screen.fill([0, 150, 0])
    pygame.mixer_music.load("resources/music/intro.mp3")
    pygame.mixer_music.play()

    Grafico_Snake(screen)

    im_snake = pygame.image.load("resources/imagen/snake.png").convert_alpha()
    im_snake = pygame.transform.scale(im_snake,[150,150])
    screen.blit(im_snake, [450, 380])
    pygame.display.update()


    type = pygame.font.Font(None,40)
    texto1 = "Press [space] to start the game "
    texto2 = "Press [P] to pause the game "
    texto3 = "Press [R] to resume the game "
    texto4 = "Press [T] for the best scores"
    T = [texto1,texto2,texto3,texto4]

    pos = 200

    for tex in T:
        t = type.render(tex,0,[0,20,0])
        screen.blit(t, [50, pos])
        pos+=60

    pygame.display.update()


