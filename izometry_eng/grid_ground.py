import pygame


class Grid:  # Cетка для тайтлов
    width: int
    height: int
    __cell_size_x__: int = 80
    __cell_size_y__: int = 36
    cols_x: int
    cols_y: int
    grid: list = []
    screen: pygame.surface.Surface

    def __init__(self, screen: pygame.surface.Surface, width: int, height: int, cols_x: int, cols_y: int):
        self.width = width
        self.height = height
        self.screen = screen
        self.cols_x = cols_x
        self.cols_y = cols_y
        self.grid = [[0] * cols_y for _ in range(cols_y)]

    def draw_test_rect_ground(self, x: int, y: int):
        """ПРИНИМАЕТ КООРДИНАТЫ ЦЕНТРА ТАЙТЛА"""
        # pygame.draw.rect(self.screen, pygame.Color("0x00FFFF"), (x - a,
        #                  y - z,
        #                  self.__cell_size_x__, self.__cell_size_y__), 1)
        z = self.__cell_size_y__ // 2
        a = self.__cell_size_x__ // 2
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"), (x - a + self.__cell_size_x__ // 5 * 3,
                                                                 y - z), (x - a, y - z + self.__cell_size_y__ // 3), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"),
                         (x - a, y - z + self.__cell_size_y__ // 3), (x - a + self.__cell_size_x__ // 5 * 2,
                                                                      y + z), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"), (x - a + self.__cell_size_x__ // 5 * 2, y + z),
                         (x + a, y - z + self.__cell_size_y__ // 3 * 2), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"), (x + a, y - z + self.__cell_size_y__ // 3 * 2),
                         (x - a + self.__cell_size_x__ // 5 * 3, y - z), 1)
        # СТРАШНО, ОЧЕНЬ СТРАШНО

    def draw_red_ground(self, x: int, y: int):
        """ПРИНИМАЕТ КООРДИНАТЫ ЦЕНТРА ТАЙТЛА"""
        # pygame.draw.rect(self.screen, pygame.Color("0x00FFFF"), (x - a,
        #                  y - z,
        #                  self.__cell_size_x__, self.__cell_size_y__), 1)
        z = self.__cell_size_y__ // 2
        a = self.__cell_size_x__ // 2
        pygame.draw.line(self.screen, pygame.Color("0xFF0000"), (x - a + self.__cell_size_x__ // 5 * 3,
                                                                 y - z), (x - a, y - z + self.__cell_size_y__ // 3), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF0000"),
                         (x - a, y - z + self.__cell_size_y__ // 3), (x - a + self.__cell_size_x__ // 5 * 2,
                                                                      y + z), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF0000"), (x - a + self.__cell_size_x__ // 5 * 2, y + z),
                         (x + a, y - z + self.__cell_size_y__ // 3 * 2), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF0000"), (x + a, y - z + self.__cell_size_y__ // 3 * 2),
                         (x - a + self.__cell_size_x__ // 5 * 3, y - z), 1)
        # СТРАШНО, ОЧЕНЬ СТРАШНО

    def draw_test_wall(self, x, y, side):
        """ПРИНИМАЕТ КООРДИНАТЫ ЦЕНТРА ТАЙТЛА И СТОРОНУ (1 - ПРАВО, ВЕРХ, 2 - ЛЕВО, ВЕРХ"""
        if side == 1:
            z = self.__cell_size_y__ // 2
            a = self.__cell_size_x__ // 2
            pygame.draw.line(self.screen, pygame.Color("0x00FFFF"),
                             (x - a + self.__cell_size_x__ // 5 * 3, y - z), (x - a + self.__cell_size_x__ // 5 * 3,
                                                                              y - z - 100))
            pygame.draw.line(self.screen, pygame.Color("0x00FFFF"),
                             (x - a, y - z + self.__cell_size_y__ // 3),
                             (x - a, y - z + self.__cell_size_y__ // 3 - 100))
            pygame.draw.line(self.screen, pygame.Color("0x00FFFF"), (x - a, y - z + self.__cell_size_y__ // 3 - 100),
                             (x - a + self.__cell_size_x__ // 5 * 3, y - z - 100))
        elif side == 2:
            z = self.__cell_size_y__ // 2
            a = self.__cell_size_x__ // 2
            pygame.draw.line(self.screen, pygame.Color("0x00FFFF"),
                             (x - a + self.__cell_size_x__ // 5 * 3, y - z), (x - a + self.__cell_size_x__ // 5 * 3,
                                                                              y - z - 100))
            pygame.draw.line(self.screen, pygame.Color("0x00FFFF"),
                             (x + a, y - z + self.__cell_size_y__ // 3 * 2),
                             (x + a, y - z + self.__cell_size_y__ // 3 * 2 - 100))
            pygame.draw.line(self.screen, pygame.Color("0x00FFFF"),
                             (x + a, y - z + self.__cell_size_y__ // 3 * 2 - 100),
                             (x - a + self.__cell_size_x__ // 5 * 3, y - z - 100))
