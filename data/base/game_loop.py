import pygame
from data.izometry_eng.grid_ground import Grid
import threading
import multiprocessing


def draw_ground_grid(cols_x: int, cols_y: int, grid: Grid, weight: int, cam_pos_x: int, cam_pos_y: int):
    for t in range(cols_x * cols_y):
        tx = t % cols_x
        ty = t // cols_x
        x = 2 * 16 * ty - 3 * 16 * tx
        y = 2 * 12 * ty + 12 * tx
        grid.draw_test_rect_ground(x + weight + cam_pos_x, y + cam_pos_y)


def draw_walls_grid(cols_x: int, cols_y: int, grid: Grid, weight: int, cam_pos_x: int, cam_pos_y: int):
    for t in range(cols_x * cols_y):
        tx = t % cols_x
        ty = t // cols_x
        x = 2 * 16 * ty - 3 * 16 * tx
        y = 2 * 12 * ty + 12 * tx
        if ty == 0:
            grid.draw_test_wall(x + weight + cam_pos_x, y + cam_pos_y, 1)
        if tx == 0:
            grid.draw_test_wall(x + weight + cam_pos_x, y + cam_pos_y, 2)


def Loop():
    pygame.init()
    size = weight, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    grid = Grid(screen, size[0], size[1])
    running = True
    cols_x = 50
    cols_y = 50
    cam_pos_x = -700
    cam_pos_y = -0
    fps = 144
    k = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if k % (144 // 10) == 0:
            screen.fill("black")
            thread_ground = threading.Thread(target=draw_ground_grid, args=(cols_x, cols_y, grid, weight,
                                                                            cam_pos_x, cam_pos_y))
            thread_wall = threading.Thread(target=draw_walls_grid, args=(cols_x, cols_y, grid, weight,
                                                                                  cam_pos_x, cam_pos_y))
            thread_ground.start()
            thread_wall.start()

            thread_wall.join()
            thread_ground.join()
            k = 0

        k += 1
        pygame.display.flip()
        clock.tick(fps)
        print(clock.get_fps())

    pygame.quit()

if __name__ == "__main__":
    Loop()