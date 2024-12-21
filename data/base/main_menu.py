import time
import sys
import pygame
import random
import threading

global curr_image


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
    size = weight, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 144
    running = True
    global curr_image
    menu_png = pygame.image.load('textures/arts/main_menu/TheLostDungeon.png')
    menu_png_l = pygame.image.load('textures/arts/main_menu/TheLostDungeon_light.png')
    curr_image = menu_png
    menu_buttons = pygame.image.load('textures/arts/main_menu/Menu_buttons.png')
    t1 = threading.Thread(target=change_image, args=(menu_png, menu_png_l))
    while running:
        screen.blit(curr_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1]:
                    pass
        if random.randint(0, 1000) == 0 and not t1.is_alive():
            t1 = threading.Thread(target=change_image, args=(menu_png, menu_png_l))
            t1.start()
        for _ in range(300):
            screen.fill(pygame.Color('0x008800'), (random.random() * weight, random.random() * height, 50 *
                                                   random.random(), 2))
        screen.blit(menu_buttons, (0, 0))
        pygame.display.flip()

        clock.tick(fps)


if __name__ == "__main__":
    main_menu()