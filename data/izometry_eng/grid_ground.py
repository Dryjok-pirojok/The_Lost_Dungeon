import pygame


def peres_1(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def peresek(a, b):
    A, B = a
    C, D = b
    return peres_1(A, C, D) != peres_1(B, C, D) and peres_1(A, B, C) != peres_1(A, B, D)


class Grid:  # Cетка для тайтлов
    width: int
    height: int
    __cell_size_x__: int = 80
    __cell_size_y__: int = 36
    cols_x: int
    cols_y: int
    grid: list = []
    screen: pygame.surface.Surface

    def __init__(self, width: int, height: int, cols_x: int, cols_y: int, map_w: tuple = ()):
        self.width = width
        self.height = height
        self.cols_x = cols_x
        self.cols_y = cols_y
        self.grid = [[0] * cols_y for _ in range(cols_y)]
        self.map_w = map_w

    def test_can_walk(self, start_pos, end_pos):
        pass

    def test_can_see(self, pos_1, pos_2):
        pos_1_x = pos_1[0] + 0.5
        pos_1_y = pos_1[1] + 0.5

        pos_2_x = pos_2[0] + 0.5
        pos_2_y = pos_2[1] + 0.5
        otrezok = ((pos_1_x, pos_1_y), (pos_2_x, pos_2_y))
        if self.map_w:
            for i in self.map_w:
                if i[2] != "1":
                    otrezok_2 = ((i[0], i[1]), (i[0] + 1, i[1]))

                else:
                    otrezok_2 = ((i[0] + 1, i[1]), (i[0] + 1, i[1] - 1))
                z = peresek(otrezok, otrezok_2)
                if z and not i[4]:
                    return False

        return True

    def test_can_attack(self, pos_1, pos_2, distance):
        pos_1_x = pos_1[0] + 0.5
        pos_1_y = pos_1[1] + 0.5

        pos_2_x = pos_2[0] + 0.5
        pos_2_y = pos_2[1] + 0.5
        if ((pos_1_x - pos_2_x) ** 2 + (pos_1_y - pos_2_y) ** 2) ** 0.5 > distance:
            return False
        otrezok = ((pos_1_x, pos_1_y), (pos_2_x, pos_2_y))
        if self.map_w:
            for i in self.map_w:
                if i[2] != "1":
                    otrezok_2 = ((i[0], i[1]), (i[0] + 1, i[1]))

                else:
                    otrezok_2 = ((i[0] + 1, i[1]), (i[0] + 1, i[1] - 1))
                z = peresek(otrezok, otrezok_2)
                if z and not i[5]:
                    return False
        return True
