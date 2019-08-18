import pygame

pygame.init()

display_width = 400
display_height = 300
character_width = 50

projectile_height = 10
projectile_width = 10


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dungeon Game')
clock = pygame.time.Clock()
personImg = pygame.image.load('/Users/joeytrasatti/desktop/drawings/robot.png')
projectileImg = pygame.image.load(
    '/Users/joeytrasatti/desktop/drawings/projectile.png')
enemyImg = pygame.image.load('/Users/joeytrasatti/desktop/drawings/enemy.png')


class enemy():
    def __init__():
        print('place holder')


def character(x, y):
    gameDisplay.blit(personImg, (x, y))


def mk_projectile(x, y):
    gameDisplay.blit(projectileImg, (x, y))


class projectile():
    def __init__(self, x, y, direction, start_time):
        self.x = x + 37
        self.y = y + 50
        self.direction = direction
        self.start_time = start_time

    def move(self):
        if self.direction == 'r':
            self.x += 10
        elif self.direction == 'l':
            self.x -= 10
        elif self.direction == 'd':
            self.y += 10
        else:
            self.y -= 10


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)
    x_change = 0
    y_change = 0
    game_exit = False
    proj_stack = []
    proj_left = False
    proj_right = False
    proj_up = False
    proj_down = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_w:
                    y_change = -5
                if event.key == pygame.K_s:
                    # Projectile input
                    y_change = 5
                if event.key == pygame.K_RIGHT:
                    proj_right = True
                if event.key == pygame.K_LEFT:
                    proj_left = True
                if event.key == pygame.K_UP:
                    proj_up = True
                if event.key == pygame.K_DOWN:
                    proj_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    proj_right = False
                if event.key == pygame.K_LEFT:
                    proj_left = False
                if event.key == pygame.K_UP:
                    proj_up = False
                if event.key == pygame.K_DOWN:
                    proj_down = False

        x += x_change
        y += y_change
        # Add 'Last proj' timer so that a proj can only be sent out every 200 ms
        if len(proj_stack) < 5:
            if proj_right:
                proj_stack.append(projectile(
                    x, y, 'r', pygame.time.get_ticks()))
            elif proj_left:
                proj_stack.append(projectile(
                    x, y, 'l', pygame.time.get_ticks()))
            elif proj_up:
                proj_stack.append(projectile(
                    x, y, 'u', pygame.time.get_ticks()))
            elif proj_down:
                proj_stack.append(projectile(
                    x, y, 'd', pygame.time.get_ticks()))

        gameDisplay.fill(white)

        character(x, y)
        for proj in proj_stack:
            if pygame.time.get_ticks() - 1000 > proj.start_time:
                proj_stack.pop()
            else:
                proj.move()
                mk_projectile(proj.x, proj.y)

        # if x > display_width - character_width or x < 0:
        #     game_exit = True

        pygame.display.update()
        clock.tick(30)


game_loop()
pygame.quit()
quit()
