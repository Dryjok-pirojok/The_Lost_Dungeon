import pygame
from data.izometry_eng.grid_ground import Grid


def Loop():
# pygame setup
    pygame.init()
    size = weight, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    grid = Grid(screen, size[0], size[1])
    running = True
    cols = 100
    cam_pos_x = -1000
    cam_pos_y = -1000
    while running:
        screen.fill("black")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        # fill the screen with a color to wipe away anything from last fram
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for t in range(cols * 100):
            tx = t % cols
            ty = t // cols
            x = 2 * 16 * ty - 3 * 16 * tx
            y = 2 * 12 * ty + 12 * tx
            grid.draw_test_rect(x + weight + cam_pos_x, y + cam_pos_y)
            print(x, y)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.

    pygame.quit()

if __name__ == "__main__":
    Loop()