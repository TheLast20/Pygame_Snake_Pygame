import pygame,random

def efect(screen):
    l = []
    size = screen.get_size()
    for i in range(800):
        bandera = True
        while bandera:
            x = random.randrange(0,size[0],20)
            y = random.randrange(0,size[1],20)
            if (x,y) not in l:
                bandera = False
                l.append((x,y))
                r = pygame.Rect(x,y,20,20)
                pygame.draw.rect(screen,[0, 150, 0],r)
                pygame.display.update()
                pygame.time.delay(2)

def draw_score(screen,score):
    screen.fill([0, 150, 0])

    type = pygame.font.Font(None,100)
    text = "You Lose"
    t = type.render(text, 0, [0, 0, 0])
    screen.blit(t, [150, 20])

    type = pygame.font.Font(None, 40)
    texto1 = "Your Score: {}".format(str(score))
    texto3 = "Press [SPACE] to play again "
    texto4 = "Press [M] to return"

    T = [texto1,texto3, texto4]

    pos = 370

    for tex in T:
        t = type.render(tex, 0, [0, 0, 0])
        screen.blit(t, [70, pos])
        pos += 40


    im_snake = pygame.image.load("resources/imagen/snake_sad.png").convert_alpha()
    im_snake = pygame.transform.scale(im_snake,[250,175+50])
    screen.blit(im_snake,[180,110])

    pygame.display.update()


def controles_end():
    num_screen = 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                num_screen = 1

            if event.key == pygame.K_m:
                num_screen = 0

    return num_screen


def draw_new_score(screen,score):
    nombre = ""
    run = True
    while run:
        screen.fill([0, 150, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:

                if len(nombre) > 0:
                    if event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:len(nombre) - 1]

                    if event.key == pygame.K_RETURN :
                        return nombre


                if len(nombre) <= 12:
                    if event.key == pygame.K_a:
                        nombre += "A"
                    elif event.key == pygame.K_b:
                        nombre += "B"
                    elif event.key == pygame.K_c:
                        nombre += "C"
                    elif event.key == pygame.K_d:
                        nombre += "D"
                    elif event.key == pygame.K_e:
                        nombre += "E"
                    elif event.key == pygame.K_f:
                        nombre += "F"
                    elif event.key == pygame.K_g:
                        nombre += "G"
                    elif event.key == pygame.K_h:
                        nombre += "H"
                    elif event.key == pygame.K_i:
                        nombre += "I"
                    elif event.key == pygame.K_j:
                        nombre += "J"
                    elif event.key == pygame.K_k:
                        nombre += "K"
                    elif event.key == pygame.K_l:
                        nombre += "L"
                    elif event.key == pygame.K_m:
                        nombre += "M"
                    elif event.key == pygame.K_n:
                        nombre += "N"
                    elif event.key == pygame.K_o:
                        nombre += "O"
                    elif event.key == pygame.K_p:
                        nombre += "P"
                    elif event.key == pygame.K_q:
                        nombre += "Q"
                    elif event.key == pygame.K_r:
                        nombre += "R"
                    elif event.key == pygame.K_s:
                        nombre += "S"
                    elif event.key == pygame.K_t:
                        nombre += "T"
                    elif event.key == pygame.K_u:
                        nombre += "U"
                    elif event.key == pygame.K_v:
                        nombre += "V"
                    elif event.key == pygame.K_w:
                        nombre += "W"
                    elif event.key == pygame.K_x:
                        nombre += "X"
                    elif event.key == pygame.K_y:
                        nombre += "Y"
                    elif event.key == pygame.K_z:
                        nombre += "Z"
                    elif event.key == pygame.K_SPACE:
                        nombre += " "

                    elif event.key == pygame.K_0:
                        nombre += "0"
                    elif event.key == pygame.K_1:
                        nombre += "1"
                    elif event.key == pygame.K_2:
                        nombre += "2"
                    elif event.key == pygame.K_3:
                        nombre += "3"
                    elif event.key == pygame.K_4:
                        nombre += "4"
                    elif event.key == pygame.K_5:
                        nombre += "5"
                    elif event.key == pygame.K_6:
                        nombre += "6"
                    elif event.key == pygame.K_7:
                        nombre += "7"
                    elif event.key == pygame.K_8:
                        nombre += "8"
                    elif event.key == pygame.K_9:
                        nombre += "9"


        type = pygame.font.Font(None, 70)
        screen.blit(type.render(nombre, 0, [0, 0, 0], [255, 255, 255]), [100, 280])


        type = pygame.font.Font(None, 80)
        text = "Congratulations"
        t = type.render(text, 0, [0, 0, 0],[255,255,255])
        screen.blit(t, [80, 20])

        type = pygame.font.Font(None, 40)
        texto1 = "New best score: {}".format(str(score))
        screen.blit(type.render(texto1, 0, [0, 0, 0]), [20,140])

        type = pygame.font.Font(None, 40)
        texto1 = "Please, write your nickname (max10 letter)"
        screen.blit(type.render(texto1, 0, [0, 0, 0]), [20, 180])


        type = pygame.font.Font(None, 40)
        texto1 = "Press [Enter] to enter your data"
        screen.blit(type.render(texto1, 0, [0, 0, 0]), [20, 430])

        pygame.display.update()


