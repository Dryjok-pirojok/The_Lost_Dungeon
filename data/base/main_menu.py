import time
import sys
import pygame
import random
import threading
from data.base.config import *
import multiprocessing
global curr_image
from data.base.game_loop import Game_main
from data.base.load_image import load_image


def change_image(m_p, m_pl):
    k1 = random.randint(1, 15)
    k2 = random.randint(1, 10)
    k3 = random.randint(1, 15)
    global curr_image
    for i in range(k1):
        curr_image = m_pl
        time.sleep(random.randint(1, 100) / 1000)
        curr_image = m_p
        time.sleep(random.randint(1, 100) / 1000)
    curr_image = m_pl
    time.sleep(k2 / 10)
    for i in range(k3):
        curr_image = m_pl
        time.sleep(random.randint(1, 100) / 1000)
        curr_image = m_p
        time.sleep(random.randint(1, 100) / 1000)


def main_menu():
    pygame.init()
    size = wight, height = SIZE
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 144
    running = True
    global curr_image
    icon = load_image("textures/arts/icon.bmp", colorkey=(255, 255, 255))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("The Lost Dungeon Launcher (don't close this window)")
    menu_png = load_image('textures/arts/main_menu/TheLostDungeon.png')
    menu_png_l = load_image('textures/arts/main_menu/TheLostDungeon_light.png')
    menu_png = pygame.transform.scale(menu_png, (wight, height))
    menu_png_l = pygame.transform.scale(menu_png_l, (wight, height))
    delta_w = wight / 1920
    delta_h = height / 1080
    curr_image = menu_png
    menu_buttons = pygame.image.load('textures/arts/main_menu/Menu_buttons.png')
    menu_buttons = pygame.transform.scale(menu_buttons, (1127 * delta_w, 838 * delta_h))
    t1 = threading.Thread(target=change_image, args=(menu_png, menu_png_l))
    while running:
        screen.blit(curr_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if 271 * delta_w <= event.pos[0] <= 770 * delta_w and 310 * delta_h <= event.pos[1] <= 409 * delta_h:
                        queue = multiprocessing.Queue()
                        process_draw = multiprocessing.Process(target=Game_main, args=(queue,))
                        process_math = multiprocessing.Process()
                        process_draw.start()
                        process_draw.join()
                        global curr_level
                        while True:
                            if not process_draw.is_alive():
                               break
                    if 271 * delta_w <= event.pos[0] <= 770 * delta_w and 739 * delta_h <= event.pos[1] <= 837 * delta_h:
                        sys.exit()




        if random.randint(0, 1000) == 0 and not t1.is_alive():
            t1 = threading.Thread(target=change_image, args=(menu_png, menu_png_l))
            t1.start()
        for _ in range(300):
            screen.fill(pygame.Color('0x008800'), (random.random() * wight, random.random() * height, 50 *
                                                   random.random(), 2))
        screen.blit(menu_buttons, (0, 0))
        pygame.display.flip()

        clock.tick(fps)


if __name__ == "__main__":
    main_menu()