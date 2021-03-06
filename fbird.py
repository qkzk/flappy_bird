import pgzrun
from random import randint


def init_bird():
    return 200


def init_speed():
    return -1


def init_walls():
    return [[200, 200, False], [500, 300, False]]


def init_score():
    return 0


def draw_bird():
    f = Rect((100, bird), (GAP, GAP))
    screen.draw.filled_rect(f, 'YELLOW')


def draw_walls():
    for wall in walls:
        x = wall[0]
        y = wall[1]
        t = Rect((x, 0), (GAP_WIDTH, y))
        b = Rect((x, y + GAP_HEIGHT), (GAP_WIDTH, HEIGHT - y + GAP_HEIGHT))
        screen.draw.filled_rect(t, 'GREEN')
        screen.draw.filled_rect(b, 'GREEN')


def draw():
    screen.fill('BLUE')
    draw_bird()
    draw_walls()
    screen.draw.text(str(score), (20, 100), color='RED', fontsize=60)


def update():
    global bird, speed, walls, score
    calc_speed()
    check_keys()
    move_walls()
    dead = check_collision()
    if is_out() or dead:
        bird = init_bird()
        speed = init_speed()
        score = init_score()


def is_out():
    if bird > HEIGHT or bird < 0:
        return True
    return False


def check_collision():
    global walls, score
    f = Rect((100, bird), (GAP, GAP))
    dead = False
    for wall in walls:
        x = wall[0]
        y = wall[1]
        passed = wall[2]
        t = Rect((x, 0), (GAP_WIDTH, y))
        b = Rect((x, y + GAP_HEIGHT), (GAP_WIDTH, HEIGHT - y + GAP_HEIGHT))
        if bird > x + GAP_WIDTH and not passed:
            wall[2] = True
            score += 1
            print(score)
        if f.colliderect(t) or f.colliderect(b):
            dead = True
    return dead


def calc_speed():
    global bird, speed
    speed += GRAVITY
    if speed >= MAX_SPEED:
        speed = MAX_SPEED
    if speed <= -MAX_SPEED:
        speed = -MAX_SPEED
    bird += speed


def check_keys():
    global speed
    if keyboard.space or keyboard.up:
        speed = -5


def move_walls():
    global walls
    for wall in walls:
        wall[0] -= 1
        if wall[0] <= - 200:
            wall[0] = 500
            wall[1] = 100 * randint(1, 3)
            wall[2] = False
            print(walls)


# globals
bird = init_bird()
speed = init_speed()
walls = init_walls()
score = init_score()

# constants
WIDTH = 400
HEIGHT = 600
GAP = 30
GAP_WIDTH = 3 * GAP
GAP_HEIGHT = 7 * GAP
GRAVITY = 1
MAX_SPEED = 20
pgzrun.go()
