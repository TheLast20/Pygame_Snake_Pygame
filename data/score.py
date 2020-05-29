import pygame

def extract_datos():
    archivo = open("data/best_score.txt","r")
    lineas = archivo.readlines()
    L = []

    for linea in lineas:
        linea = linea.strip("\n")
        linea = linea.split(":")

        L.append(linea)

    archivo.close()
    return L

def write_datos(name,score):
    l_score = extract_datos()
    n=4
    for linea in l_score[::-1]:
        if score>float(linea[1]):
            num = n
        n-=1

    print(num)

    tup = [name,str(score)]

    l_score.insert(num,tup)

    archivo = open("data/best_score.txt", "w")
    for linea in l_score[:5]:
        w_linea = linea[0]+":"+linea[1]+"\n"
        archivo.write(w_linea)

    archivo.close()




def draw_best_score(screen):

    screen.fill([0, 150, 0])
    # Genero la fuente
    fuente = pygame.font.Font(None, 70)
    screen.blit(fuente.render("BEST SCORE", 0, [0, 0, 0],[255,255,255]), (150, 50))


    List = extract_datos()
    space = 20
    y = 150
    fuente = pygame.font.Font(None, 50)

    for linea in List:
        name = linea[0]
        score = linea[1]
        num_space = space - len(name)-len(score)
        l_space = "."*num_space

        text = name+l_space+score
        screen.blit(fuente.render(text,0,[0,0,0]),(50,y))
        y+=50

    trofeo = pygame.image.load("resources/imagen/trophy.png").convert_alpha()
    screen.blit(pygame.transform.scale(trofeo,[114,140]),[420,200])

    fuente = pygame.font.Font(None, 50)
    screen.blit(fuente.render("Press [T] for return", 0, [0, 0, 0]), (150, 430))

    pygame.display.update()


def controles_score():
    num_screen = 4
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                num_screen = 0

    return num_screen








