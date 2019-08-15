import pygame

pygame.init()

display_width = 800
display_height = 600
character_width = 50

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dungeon Game')
clock = pygame.time.Clock()
personImg = pygame.image.load('person.png')


def character(x, y):
    gameDisplay.blit(personImg, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        character(x, y)

        if x > display_width - character_width or x < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(60)
        print(clock.get_fps())


game_loop()
pygame.quit()
quit()
