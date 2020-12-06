from ray_tracing import ray_tracing
from time import time
from pygame.time import Clock
from pygame.display import set_mode,set_caption,flip
from pygame.mouse import set_visible
from pygame.event import get
from pygame.draw import circle
from pygame import init,QUIT,quit,KEYDOWN,K_ESCAPE
from os import environ
from tkinter import Tk
from control import Control
from sys import exit
from settings import WIDTH,HEIGHT,BLACK

if __name__ == '__main__':
    environ['SDL_VIDEO_WINDOW_POS'] = f'{(Tk().winfo_screenwidth() - WIDTH) // 2},' \
                                      f'{(Tk().winfo_screenheight() - HEIGHT) // 4}'
    init()
    set_caption('Ray tracing')
    sc = set_mode((WIDTH, HEIGHT))
    clock = Clock()
    set_visible(False)
    control = Control()

    start = time()
    game = True
    while game:
        start = time()
        for event in get():
            if event.type == QUIT:
                quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                game = False
        control.pressed_keys()
        sc.fill(BLACK)

        for color, xy in ray_tracing(control.key):
            circle(sc, color, xy, SCALE)

        flip()
        clock.tick()
        print(time() - start)
    quit()
    exit()
