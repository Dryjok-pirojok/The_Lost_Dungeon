import pygame
from data.izometry_eng.grid_ground import Grid
import threading
import multiprocessing


def draw_ground_grid(grid: Grid, cam_pos_x: int, cam_pos_y: int):
    cols_x = grid.cols_x
    cols_y = grid.cols_y
    width = grid.width
    height = grid.height

    for t in range(cols_x * cols_y):
        tx = t % cols_x
        ty = t // cols_x
        x = 2 * 16 * ty - 3 * 16 * tx
        y = 2 * 12 * ty + 12 * tx
        x_to_draw = x + width + cam_pos_x
        y_to_draw = y + cam_pos_y
        if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
            grid.draw_test_rect_ground(x + width + cam_pos_x, y + cam_pos_y)


def selected_title(grid: Grid, weight: int, cam_pos_x: int, cam_pos_y: int, tx: int, ty: int):
    x = 2 * 16 * ty - 3 * 16 * tx
    y = 2 * 12 * ty + 12 * tx
    grid.draw_red_ground(x + weight + cam_pos_x, y + cam_pos_y)


def draw_walls_grid(grid: Grid, cam_pos_x: int, cam_pos_y: int, side: int = 0):
    cols_x = grid.cols_x
    cols_y = grid.cols_y
    width = grid.width
    height = grid.height
    for t in range(cols_x * cols_y):
        tx = t % cols_x
        ty = t // cols_x
        x = 2 * 16 * ty - 3 * 16 * tx
        y = 2 * 12 * ty + 12 * tx
        x_to_draw = x + width + cam_pos_x
        y_to_draw = y + cam_pos_y
        if ty == 0:
            if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
                grid.draw_test_wall(x_to_draw, y_to_draw, 1)
        if tx == 0:
            if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
                grid.draw_test_wall(x_to_draw, y_to_draw, 2)


def Loop():
    pygame.init()
    size = weight, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    cols_x = 100
    cols_y = 100
    cam_pos_x = 0
    cam_pos_y = 0
    grid = Grid(screen, size[0], size[1], cols_x, cols_y)
    fps = 144
    k = 0
    base_x = 0
    base_y = 0
    right_button = False
    left_button = False
    moved = False
    tx = 0
    ty = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_RIGHT:
                    right_button = True
                    base_x = event.pos[0]
                    base_y = event.pos[1]
                if event.button == pygame.BUTTON_LEFT:
                    left_button = True

            if event.type == pygame.MOUSEMOTION:
                if right_button:
                    x = event.pos[0]
                    y = event.pos[1]
                    cam_pos_x = cam_pos_x + (base_x - x)
                    cam_pos_y = cam_pos_y + (base_y - y)
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
                    moved = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_RIGHT:
                    right_button = False
                if event.button == pygame.BUTTON_LEFT:
                    left_button = False
        if k % fps == 0 or right_button or moved:
            screen.fill("black")
            thread_ground = threading.Thread(target=draw_ground_grid, args=(grid, cam_pos_x, cam_pos_y))
            thread_wall = threading.Thread(target=draw_walls_grid, args=(grid, cam_pos_x, cam_pos_y))
            thread_ground.start()
            thread_ground.join()
            selected_title(grid, weight, cam_pos_x, cam_pos_y, tx, ty)
            thread_wall.start()

            thread_wall.join()
            moved = False
            k = 0
        k += 1
        pygame.display.flip()

        clock.tick(fps)
        print(clock.get_fps())
    pygame.quit()

if __name__ == "__main__":
    Loop()