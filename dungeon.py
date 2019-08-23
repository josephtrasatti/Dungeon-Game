import pygame
import random
import math

pygame.init()

display_width = 600
display_height = 450
character_width = 50

projectile_height = 10
projectile_width = 10


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Dungeon Game')
clock = pygame.time.Clock()
personImg = pygame.image.load('/Users/joeytrasatti/desktop/drawings/robot.png')
projectileImg = pygame.image.load('/Users/joeytrasatti/desktop/drawings/projectile.png')
enemyImg = pygame.image.load('/Users/joeytrasatti/desktop/drawings/enemy.png')


class enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, char_x, char_y):
        char_x += 25
        char_y += 40
        if char_x != self.x and char_y != self.y:
            phi = (abs(char_x - self.x) / (abs(char_x - self.x) + abs(char_y - self.y))) / 2 * math.pi
        else:
            phi = 0
        if char_x != self.x:
            self.x += int(math.sin(phi) * 4 * ((abs(char_x - self.x) / (char_x - self.x))))
        if char_y != self.y:
            self.y += int(math.cos(phi) * 4 * ((abs(char_y - self.y) / (char_y - self.y))))


def mk_enemy(x, y):
    gameDisplay.blit(enemyImg, (x, y))


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
    enemy_stack = []
    score = 0

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
                    y_change = 5
                # Projectile input
                if event.key == pygame.K_RIGHT:
                    proj_right = True
                if event.key == pygame.K_LEFT:
                    proj_left = True
                if event.key == pygame.K_UP:
                    proj_up = True
                if event.key == pygame.K_DOWN:
                    proj_down = True
                # exit condition
                if event.key == pygame.K_ESCAPE:
                    game_exit = True

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

        if not proj_stack or pygame.time.get_ticks() - 400 > proj_stack[-1].start_time:
            if proj_right:
                proj_stack.append(projectile(x, y, 'r', pygame.time.get_ticks()))
            elif proj_left:
                proj_stack.append(projectile(x, y, 'l', pygame.time.get_ticks()))
            elif proj_up:
                proj_stack.append(projectile(x, y, 'u', pygame.time.get_ticks()))
            elif proj_down:
                proj_stack.append(projectile(x, y, 'd', pygame.time.get_ticks()))

        gameDisplay.fill(white)

        character(x, y)
        for proj in proj_stack:
            if pygame.time.get_ticks() - 1000 > proj.start_time:
                proj_stack.pop(0)
            else:
                proj.move()
                mk_projectile(proj.x, proj.y)

        spawn_enemy = random.randint(0, 49)
        if len(enemy_stack) < 3 and spawn_enemy == 1:
            side_pick = random.randint(0, 3)
            if side_pick == 0:
                enemy_stack.append(enemy(x=random.randint(10, 60) * -1, y=random.randint(0, 449)))
            elif side_pick == 1:
                enemy_stack.append(enemy(x=random.randint(609, 659), y=random.randint(0, 449)))
            elif side_pick == 2:
                enemy_stack.append(enemy(x=random.randint(0, 599), y=random.randint(10, 60) * -1))
            else:
                enemy_stack.append(enemy(x=random.randint(0, 599), y=random.randint(459, 609)))

        for e in enemy_stack:
            if x - 15 <= e.x <= x + 65 and y - 15 <= e.y <= y + 90:
                game_exit = True
            else:
                e.move(x, y)
                mk_enemy(e.x, e.y)

        pygame.display.update()

        for proj in proj_stack:
            for i, e in enumerate(enemy_stack):
                if e.x-8 <= proj.x <= e.x+33 and e.y-8 <= proj.y <= e.y+33:
                    enemy_stack.pop(i)
                    score += 1

        clock.tick(30)


game_loop()
pygame.quit()
quit()
