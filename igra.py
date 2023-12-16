import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

main_kapibara = pygame.image.load("img1/kapibara.jpg")
main_kapibara = pygame.transform.scale(main_kapibara, (200,200))
main_fon = pygame.image.load("img1/fon.jpg")
main_fon = pygame.transform.scale(main_fon, (800,600))
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120
speed = 2
x_kapibara, y_kapibara = 10, 80

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


        screen.blit(main_fon, (0,0))
        text = font.render("play!!", True, (0, 0, 100))
        screen.blit(text, (x, y))
        text2 = font2.render("Welcome to game2!!", True, (110, 10, 100))
        screen.blit(text2, (x1, y1))
        textadsf = font.render("Welcome to game3!!", True, (110, 110, 100))
        screen.blit(textadsf, (x2, y2))


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            x_kapibara += speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            y_kapibara += speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            y_kapibara -= speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            x_kapibara -= speed


        screen.blit(main_kapibara, (x_kapibara, y_kapibara))

        pygame.display.update()
