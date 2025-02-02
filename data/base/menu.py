import pygame
from data.base.load_image import load_image


def show_menu(screen: pygame.surface.Surface, wight, height, mouse_pos, mouse_left_button):
    screen.blit(load_image("textures/arts/interface/menu.png"), (wight // 2 - 150, height // 2 - 300))

    if wight // 2 - 150 + 51 <= mouse_pos[0] <= wight // 2 - 150 + 250 and height // 2 - 300 + 66 <= mouse_pos[1] <= \
            height // 2 - 300 + 115 and mouse_left_button:
        return 2

    elif wight // 2 - 150 + 51 <= mouse_pos[0] <= wight // 2 - 150 + 250 and height // 2 - 300 + 385 <= mouse_pos[1] <=\
            height // 2 - 300 + 434 and mouse_left_button:
        return 1

    elif wight // 2 - 150 + 51 <= mouse_pos[0] <= wight // 2 - 150 + 250 and height // 2 - 300 + 125 <= mouse_pos[1] <=\
            height // 2 - 300 + 174 and mouse_left_button:
        return 3

    elif wight // 2 - 150 + 51 <= mouse_pos[0] <= wight // 2 - 150 + 250 and height // 2 - 300 + 189 <= mouse_pos[1] <=\
            height // 2 - 300 + 238 and mouse_left_button:
        return 4

    elif wight // 2 - 150 + 51 <= mouse_pos[0] <= wight // 2 - 150 + 250 and height // 2 - 300 + 257 <= mouse_pos[1] <=\
            height // 2 - 300 + 306 and mouse_left_button:
        return 5

    elif wight // 2 - 150 + 51 <= mouse_pos[0] <= wight // 2 - 150 + 250 and height // 2 - 300 + 321 <= mouse_pos[1] <=\
            height // 2 - 300 + 370 and mouse_left_button:
        return 6

    return 0
