import sys

import pygame
from data.base.load_image import load_image
from data.izometry_eng.grid_ground import Grid
import threading
import multiprocessing
from data.base.floor_title_group import Floor
from data.entities.player.player import Player
from levels.TEST_LEVELS.test_level_01 import Test_level_01
from data.base.wall_title_group import Wall
from data.entities.enemies.test_npc_enemy import Test_Npc_Enemy
from data.base.config import button_keys, FPS


# def draw_ground_grid(grid: Grid, cam_pos_x: int, cam_pos_y: int):
#     cols_x = grid.cols_x
#     cols_y = grid.cols_y
#     width = grid.width
#     height = grid.height
#
#     for t in range(cols_x * cols_y):
#         tx = t % cols_x
#         ty = t // cols_x
#         x = 2 * 16 * ty - 3 * 16 * tx
#         y = 2 * 12 * ty + 12 * tx
#         x_to_draw = x + width + cam_pos_x
#         y_to_draw = y + cam_pos_y
#         if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
#             grid.draw_test_rect_ground(x + width + cam_pos_x, y + cam_pos_y)


def selected_title(grid: Grid, weight: int, cam_pos_x: int, cam_pos_y: int, tx: int, ty: int):
    x = 2 * 16 * ty - 3 * 16 * tx
    y = 2 * 12 * ty + 12 * tx
    grid.draw_red_ground(x + weight + cam_pos_x, y + cam_pos_y)


# def draw_walls_grid(grid: Grid, cam_pos_x: int, cam_pos_y: int, side: int = 0):
#     cols_x = grid.cols_x
#     cols_y = grid.cols_y
#     width = grid.width
#     height = grid.height
#     for t in range(cols_x * cols_y):
#         tx = t % cols_x
#         ty = t // cols_x
#         x = 2 * 16 * ty - 3 * 16 * tx
#         y = 2 * 12 * ty + 12 * tx
#         x_to_draw = x + width + cam_pos_x
#         y_to_draw = y + cam_pos_y
#         if ty == 0:
#             if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
#                 grid.draw_test_wall(x_to_draw, y_to_draw, 1)
#         if tx == 0:
#             if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
#                 grid.draw_test_wall(x_to_draw, y_to_draw, 2)


def Loop():
    icon = load_image("textures/arts/icon.bmp", colorkey=(255, 255, 255))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("The Lost Dungeon")
    pygame.init()
    size = weight, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    player = Player(weight, height, 0, 1)
    running = True
    level = Test_level_01
    cols_x = level.col_x
    cols_y = level.col_y
    cam_pos_x = 0
    cam_pos_y = 0
    grid = Grid(screen, size[0], size[1], cols_x, cols_y)
    fps = FPS
    k = 0
    base_x = 0
    base_y = 0
    ev_x = 0
    ev_y = 0
    right_button = False
    left_button = False
    tx = 0
    ty = 0
    dt = 0
    floor_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    entities = []
    for t in range(cols_x * cols_y):
        tx = t % cols_x
        ty = t // cols_x
        Floor(floor_sprites, tx, ty, level.cells[t], weight, height)
    Wall(wall_sprites, 0, 1, (3, 4), weight, height)
    test_npc = Test_Npc_Enemy(weight, height, 3, 3, load_image("textures/entities/test_npc_en.png"))
    entities.append(player)
    entities.append(test_npc)
    to_draw = {}

    for i in range(0, level.col_y):
        to_draw[i] = []
    for i in wall_sprites:
        z = i.return_tx_and_ty()[1]
        to_draw[z].append(i)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_RIGHT:
                    right_button = True
                    base_x = event.pos[0]
                    base_y = event.pos[1]
                    ev_x = event.pos[0]
                    ev_y = event.pos[1]
                if event.button == pygame.BUTTON_LEFT:

                    player.move(tx, ty)
                    left_button = True

            if event.type == pygame.MOUSEMOTION:
                if right_button:
                    ev_x = event.pos[0]
                    ev_y = event.pos[1]
                    cam_pos_x = cam_pos_x + (base_x - ev_x)
                    cam_pos_y = cam_pos_y + (base_y - ev_y)
                    base_x = event.pos[0]
                    base_y = event.pos[1]
                else:
                    x, y = event.pos[0], event.pos[1]
                    x = x - cam_pos_x - weight
                    y = y - cam_pos_y
                    x -= 8
                    y += 20
                    tx = - int((x - 4 * y / 3) / 64)
                    ty = int((x + 4 * y) / 128)
                    if tx < 0:
                        tx = 0
                    if ty < 0:
                        ty = 0
                    if tx > level.col_x - 1:
                        tx = level.col_x - 1
                    if ty > level.col_y - 1:
                        ty = level.col_y - 1
            if event.type == pygame.KEYDOWN:
                if event.key == button_keys["inventory"]:
                    print("inventory key pressed")

                if event.key == button_keys["console"]:
                    print("console key pressed")

                if event.key == button_keys["menu"]:
                    print("menu key pressed")


            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_RIGHT:
                    right_button = False
                if event.button == pygame.BUTTON_LEFT:
                    left_button = False
        screen.fill("black")
        # thread_ground = threading.Thread(target=draw_ground_grid, args=(grid, cam_pos_x, cam_pos_y))
        # thread_wall = threading.Thread(target=draw_walls_grid, args=(grid, cam_pos_x, cam_pos_y))
        # thread_ground.start()
        # thread_ground.join()
        # thread_wall.start()
        #
        # thread_wall.join()
        floor_sprites.update(cam_pos_x, cam_pos_y)
        floor_sprites.draw(screen)
        wall_sprites.update(cam_pos_x, cam_pos_y, [player.return_tx_and_ty()])
        selected_title(grid, weight, cam_pos_x, cam_pos_y, tx, ty)
        for i in entities:
            to_draw[i.return_tx_and_ty()[1]].append(i)
        for key, items in to_draw.items():
            for i in items:
                if str(i) == "NPC":
                    i.draw(screen, cam_pos_x, cam_pos_y)
                    to_draw[key].remove(i)
                else:
                    i.draw(screen)
        player.update(dt)
        pygame.display.flip()
        clock.tick(fps)
        dt = clock.tick(fps) / 1000
    pygame.quit()


if __name__ == "__main__":
    Loop()
