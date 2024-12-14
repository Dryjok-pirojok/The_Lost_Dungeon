import time

import pygame
import random
import threading


def change_image(screen, m_p, m_pl, m_pr, m_plr):
    k1 = random.randint(1, 15)
    k2 = random.randint(1, 10)
    k3 = random.randint(1, 15)
    for i in range(k1):
        screen.blit(m_pl, m_plr)
        time.sleep(random.randint(1, 100) / 1000)
        screen.blit(m_p, m_pr)
        time.sleep(random.randint(1, 100) / 1000)
    screen.blit(m_pl, m_plr)
    time.sleep(k2 / 10)
    for i in range(k3):
        screen.blit(m_pl, m_plr)
        time.sleep(random.randint(1, 100) / 1000)
        screen.blit(m_p, m_pr)
        time.sleep(random.randint(1, 100) / 1000)





def main_menu():
    pygame.init()
    size = weight, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 144
    running = True
    menu_png = pygame.image.load('textures/arts/main_menu/TheLostDungeon.png')
    menu_png_rect = menu_png.get_rect(bottomright=(weight, height))
    menu_png_l = pygame.image.load('textures/arts/main_menu/TheLostDungeon_light.png')
    menu_png_rect_l = menu_png_l.get_rect(bottomright=(weight, height))
    screen.blit(menu_png, menu_png_rect)
    t1 = threading.Thread(target=change_image, args=(screen, menu_png, menu_png_l, menu_png_rect, menu_png_rect_l))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        if random.randint(0, 10000) == 1000 and not t1.is_alive():
            try:
                t1 = threading.Thread(target=change_image,
                                      args=(screen, menu_png, menu_png_l, menu_png_rect, menu_png_rect_l))
                t1.start()
            except Exception as err:
                print(err)
                pass

        clock.tick(fps)


if __name__ == "__main__":
    main_menu()