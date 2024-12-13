import pygame


class Grid:  # Cетка для тайтлов
    width: int
    height: int
    __cell_size_x__: int = 36
    __cell_size_y__: int = 80
    screen: pygame.surface.Surface

    def __init__(self, screen: pygame.surface.Surface, width: int, height: int):
        self.width = width
        self.height = height
        self.screen = screen

    def draw_test_rect(self, x: int, y: int):
        """ПРИНИМАЕТ КООРДИНАТЫ ЦЕНТРА ТАЙТЛА"""
