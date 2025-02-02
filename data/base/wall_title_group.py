import pygame
from data.base.id_to_tile_file_name import id_to_image
from data.base.load_image import load_image


class Wall_up(pygame.sprite.Sprite):
    x: int
    y: int
    image: pygame.image
    rect: pygame.rect

    def __init__(self, group: pygame.sprite.Group, tx: int, ty: int, type_sprite, width: int, height: int):
        super().__init__(group)
        self.width = width
        self.height = height
        self.norm_image = load_image(id_to_image[type_sprite[0]], (255, 255, 255))
        self.hided_image = load_image(id_to_image[type_sprite[1]], (255, 255, 255))
        self.image = self.norm_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.tx = tx
        self.ty = ty
        self.x = 2 * 16 * ty - 3 * 16 * tx + self.width - 40
        self.y = 2 * 12 * ty + 12 * tx - self.rect.height - 6
    # def draw(self, screen: pygame.sprite.Group, cam_pos_x: int, cam_pos_y: int):
    #     screen.blit(self.image, (cam_pos_x + self.x, self.y + cam_pos_y))

    def update(self, *args, **kwargs):
        """args из-за pygame имеют вид: (cam_pos_x, cam_pos_y, entities: list), где entities -
        список координат (x, y) видимых сущностей"""
        self.rect.x = self.x + args[0]
        self.rect.y = self.y + args[1]
        for x, y in args[2]:

            if y < self.ty <= y + 2 and abs(self.tx - x) <= 2:
                self.image = self.hided_image
            else:
                self.image = self.norm_image

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def return_tx_and_ty(self):
        return self.tx, self.ty

    def __str__(self):
        return "Wall_up"


class Wall_top(pygame.sprite.Sprite):
    x: int
    y: int
    image: pygame.image
    rect: pygame.rect

    def __init__(self, group: pygame.sprite.Group, tx: int, ty: int, type_sprite, width: int, height: int):
        super().__init__(group)
        self.width = width
        self.height = height
        self.norm_image = load_image(id_to_image[type_sprite[0]], (255, 255, 255))
        self.hided_image = load_image(id_to_image[type_sprite[1]], (255, 255, 255))
        self.image = self.norm_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.tx = tx
        self.ty = ty
        self.x = 2 * 16 * ty - 3 * 16 * tx + self.width + 6
        self.y = 2 * 12 * ty + 12 * tx - self.rect.height - 6
    # def draw(self, screen: pygame.sprite.Group, cam_pos_x: int, cam_pos_y: int):
    #     screen.blit(self.image, (cam_pos_x + self.x, self.y + cam_pos_y))

    def update(self, *args, **kwargs):
        """args из-за pygame имеют вид: (cam_pos_x, cam_pos_y, entities: list), где entities -
        список координат (x, y) видимых сущностей"""
        self.rect.x = self.x + args[0]
        self.rect.y = self.y + args[1]
        for x, y in args[2]:

            if x + 1 < self.ty <= x + 2 and abs(self.ty - y) <= 2:
                self.image = self.hided_image
            else:
                self.image = self.norm_image

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def return_tx_and_ty(self):
        return self.tx, self.ty

    def __str__(self):
        return "Wall_top"
