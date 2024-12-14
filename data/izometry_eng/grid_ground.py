import pygame


class Grid:  # Cетка для тайтлов
    width: int
    height: int
    __cell_size_x__: int = 80
    __cell_size_y__: int = 36
    screen: pygame.surface.Surface

    def __init__(self, screen: pygame.surface.Surface, width: int, height: int):
        self.width = width
        self.height = height
        self.screen = screen

    def draw_test_rect(self, x: int, y: int):
        """ПРИНИМАЕТ КООРДИНАТЫ ЦЕНТРА ТАЙТЛА"""
        # pygame.draw.rect(self.screen, pygame.Color("0x00FFFF"), (x - self.__cell_size_x__ // 2,
        #                  y - self.__cell_size_y__ // 2,
        #                  self.__cell_size_x__, self.__cell_size_y__), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"),
                         (x - self.__cell_size_x__ // 2 + self.__cell_size_x__ // 5 * 3,
                          y - self.__cell_size_y__ // 2), (x - self.__cell_size_x__ // 2,
                                                      y - self.__cell_size_y__ // 2 + self.__cell_size_y__ // 3), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"),
                         (x - self.__cell_size_x__ // 2,
                          y - self.__cell_size_y__ // 2 + self.__cell_size_y__ // 3), (x - self.__cell_size_x__ // 2
                          + self.__cell_size_x__ // 5 * 2, y + self.__cell_size_y__ // 2), 1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"),
                         (x - self.__cell_size_x__ // 2
                          + self.__cell_size_x__ // 5 * 2, y + self.__cell_size_y__ // 2),
                         (x + self.__cell_size_x__ // 2, y - self.__cell_size_y__ // 2 +
                          self.__cell_size_y__ // 3 * 2),1)
        pygame.draw.line(self.screen, pygame.Color("0xFF00FF"),
                         (x + self.__cell_size_x__ // 2, y - self.__cell_size_y__ // 2 +
                          self.__cell_size_y__ // 3 * 2),
                         (x - self.__cell_size_x__ // 2 + self.__cell_size_x__ // 5 * 3,
                          y - self.__cell_size_y__ // 2), 1)
