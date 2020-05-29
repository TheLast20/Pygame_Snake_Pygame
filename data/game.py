import pygame,random
from data.score import *

#Constante
new_score = False

#Class---------------------------------------------------------
class Pix():
    def __init__(self,x,y):
        self.size = 40
        self.separation = 10
        self.x = x
        self.y = y
        self.coordinate_last = None
        self.color = None
        self.speed = self.size + self.separation
        self.part = None
        self.angle = 0
        self.s_death = pygame.mixer.Sound("resources/sound/death.wav")





    def draw(self,screen):
        if self.part == "Heat":
            self.im = pygame.image.load("resources/imagen/heat.png").convert_alpha()
            self.im = pygame.transform.scale(self.im,[50,50])

            screen.blit(pygame.transform.rotate(self.im,self.angle),[self.x,self.y])
            # pygame.draw.rect(screen, [0, 0, 0], [self.x, self.y, 50, 50])
            # pygame.draw.rect(screen, self.color, [self.x + 5, self.y + 5, 40, 40])
            # # pygame.draw.circle(screen, [255,255,255] ,[self.x + 25, self.y + 25], 10)

        elif self.part == "Body":
            self.im = pygame.image.load("resources/imagen/body.png").convert_alpha()
            self.im = pygame.transform.scale(self.im, [50, 50])
            screen.blit(self.im, [self.x, self.y])

            # pygame.draw.rect(screen, [0, 0, 0], [self.x, self.y, 50, 50])
            # pygame.draw.rect(screen, self.color, [self.x + 5, self.y + 5, 40, 40])
            # pygame.draw.circle(screen, [250, 250, 0], [self.x + 25, self.y + 25], 10)

        elif self.part == "Point":
            self.im = pygame.image.load("resources/imagen/apple.png").convert_alpha()
            self.im = pygame.transform.scale(self.im, [50, 50])
            screen.blit(self.im, [self.x, self.y])



            # pygame.draw.circle(screen, [0, 0, 0], [self.x + 25, self.y + 25], 25)
            # pygame.draw.circle(screen, [250, 0, 0], [self.x + 25, self.y + 25], 20)
            # # pygame.draw.rect(screen, [255, 0, 0], [self.x, self.y, 50, 50])

class Jugador(Pix):
    def __init__(self,x,y,direction):
        super().__init__(x, y)
        self.direction = direction
        self.color = [255,0,0]
        self.score = 0
        self.puntaje = 10

    def movement(self,screen_game):
        if self.direction == "up":
            self.y-= self.speed
            if self.y<screen_game.top:
                self.y = screen_game.bottom - self.speed
        elif self.direction == "down":
            self.y += self.speed
            if self.y >= screen_game.bottom:
                self.y = screen_game.top + self.separation
        elif self.direction == "left":
            self.x -= self.speed
            if self.x < 0:
                self.x = screen_game.right - self.speed
        elif self.direction == "right":
            self.x += self.speed
            if self.x >= screen_game.right:
                self.x = self.separation

class Point(Pix):
    def __init__(self):
        self.x = None
        self.y = None
        super().__init__(self.x, self.y)
        self.color = [0,0,255]
        self.s_point = pygame.mixer.Sound("resources/sound/point.ogg")


    def generate(self,snake,screen_game,part):
        self.part = part
        self.l = []
        for body in snake:
            self.l.append([body.x, body.y])

        self.bandera = True
        while self.bandera:
            self.x = random.randrange(self.separation,screen_game.right - self.speed,self.speed)
            self.y = random.randrange(screen_game.top + self.separation ,screen_game.bottom - self.speed,self.speed)

            if [self.x,self.y] not in self.l:
                self.bandera = False

class Snake(Pix):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.color = [0,255,0]
        self.x_last = None
        self.y_last = None


    def movement(self,coordinate_last):
        self.x_last = self.x
        self.y_last = self.y

        self.x = coordinate_last[0]
        self.y = coordinate_last[1]


#-----------------------------------------------------------------
def colision(jugador,snake):
    for body in snake:
        if (jugador.x,jugador.y) == (body.x,body.y):
            return True

    return False

def screen_update(screen,screen_score, screen_game,score):

    #Draw BackGround
    size = screen.get_size()
    screen.fill([0, 150, 0])
    pygame.draw.rect(screen, [0,0,0], screen_score, 10)
    pygame.draw.rect(screen, [0, 0, 0], screen_game, 10)

    type = pygame.font.Font(None, 60)
    text = "Score: {}".format(score)
    text = type.render(text,0,[255,255,255])
    screen.blit(text, [30, 30])

    text = "Best Score: {}".format(sup_point(score))
    text = type.render(text, 0, [255, 255, 255])
    screen.blit(text, [270, 30])
    pygame.display.update()


def sup_point(score):
    global new_score
    L = extract_datos()

    if score < float(L[4][1]):
        return L[4][1]

    elif score < float(L[3][1]):
        new_score = True
        return L[3][1]

    elif score < float(L[2][1]):
        new_score = True
        return L[2][1]

    elif score < float(L[1][1]):
        new_score = True
        return L[1][1]

    elif score < float(L[0][1]):
        new_score = True
        return L[0][1]



#----------------------------------------------------------------

def game_snake(screen,screen_score,screen_game):

    pygame.mixer_music.load("resources/music/game.mp3")
    pygame.mixer_music.play()

    # Genero al jugador
    jugador = Jugador(160, 160, "up")
    # Genero al snake
    snake = []
    x, y = jugador.x, jugador.y


    for body in range(2):
        s = Snake(x, y)
        if body == 0:
            s.part = "Heat"
        else:
            s.part = "Body"
        x -= 50
        snake.append(s)

    # Genero el primer point
    point = Point()
    point.generate(snake, screen_game, "Point")

    # Genero al reloj
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    run = True
    pause = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_a and  jugador.direction != "right":
                    jugador.direction = "left"
                    snake[0].angle = 90

                elif event.key == pygame.K_LEFT and  jugador.direction != "right":
                    jugador.direction = "left"
                    snake[0].angle = 90

                elif event.key == pygame.K_d and jugador.direction != "left":
                    jugador.direction = "right"
                    snake[0].angle = 270

                elif event.key == pygame.K_RIGHT and jugador.direction != "left":
                    jugador.direction = "right"
                    snake[0].angle = 270

                elif event.key == pygame.K_w and jugador.direction != "down" :
                    jugador.direction = "up"
                    snake[0].angle = 0

                elif event.key == pygame.K_UP and jugador.direction != "down" :
                    jugador.direction = "up"
                    snake[0].angle = 0

                elif event.key == pygame.K_s and jugador.direction != "up":
                    jugador.direction = "down"
                    snake[0].angle = 180

                elif event.key == pygame.K_DOWN and jugador.direction != "up":
                    jugador.direction = "down"
                    snake[0].angle = 180

                elif event.key == pygame.K_p:
                    pause = True


                elif event.key == pygame.K_r:
                    pause = False


        if not pause:
            screen_update(screen, screen_score, screen_game,jugador.score)
            point.draw(screen)
            jugador.movement(screen_game)




            if (jugador.x, jugador.y) == (point.x, point.y):
                point.s_point.play()
                snake[0].part = "Body"
                body = Snake(point.x, point.y)
                body.part = "Heat"
                snake.insert(0, body)
                point.generate(snake, screen_game, "Point")
                jugador.score += jugador.puntaje
                for body in snake:
                    body.draw(screen)
                pygame.display.update()


            elif colision(jugador, snake):
                pygame.mixer_music.stop()
                pygame.time.delay(10)
                jugador.s_death.play()
                x, y = [jugador.x, jugador.y]
                for body in snake:
                    body.movement((x, y))
                    body.draw(screen)
                    x, y = body.x_last, body.y_last
                    pygame.display.update()

                snake[0].draw(screen)
                pygame.display.update()

                pygame.time.delay(1000)
                run = False

            else:
                x, y = [jugador.x, jugador.y]
                for body in snake:
                    body.movement((x, y))
                    body.draw(screen)
                    x, y = body.x_last, body.y_last
                    pygame.display.update()
            clock.tick(10)
    if new_score:
        valor = 3
    else:
        valor = 2

    return valor,jugador.score