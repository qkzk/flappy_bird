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
    screen.draw.filled_rect(f, "YELLOW")


def draw_walls():
    for wall in walls:
        x = wall[0]
        y = wall[1]
        t = Rect((x, 0), (GAP_WIDTH, y))
        screen.draw.filled_rect(t, "GREEN")


def draw():
    screen.fill("BLUE")
    draw_bird()
    draw_walls()
    screen.draw.text(str(score), (20, 100), color="RED", fontsize=60)


def update():
    global bird, speed, walls, score
    calc_speed()
    check_keys()
    move_walls()
    dead = check_collision(bird, walls) or is_out(bird)
    if dead:
        bird = init_bird()
        speed = init_speed()
        score = init_score()


def is_out(bird):
    pass


def check_collision(bird, walls):
    pass


def bird_hit_wall(bird, wall):
    pass


def calc_speed():
    pass


def check_keys():
    pass


def move_walls():
    pass


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
