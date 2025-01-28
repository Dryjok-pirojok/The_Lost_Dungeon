import pygame
from data.base.id_to_tile_file_name import id_to_image
from data.base.load_image import load_image


class Floor(pygame.sprite.Sprite):
    x: int
    y: int
    image: pygame.image
    rect: pygame.rect

    def __init__(self, group: pygame.sprite.Group, tx: int, ty: int, type_sprite: int, width: int, height: int):
        super().__init__(group)
        self.width = width
        self.height = height
        self.image = load_image(id_to_image[type_sprite], (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = 2 * 16 * ty - 3 * 16 * tx + self.width - 40
        self.y = 2 * 12 * ty + 12 * tx - 18
        self.tx = tx
        self.ty = ty
    # def draw(self, screen: pygame.sprite.Group, cam_pos_x: int, cam_pos_y: int):
    #     screen.blit(self.image, (cam_pos_x + self.x, self.y + cam_pos_y))

    def update(self, *args, **kwargs):
        """args из-за pygame имеют вид: (cam_pos_x, cam_pos_y)"""
        self.rect.x = self.x + args[0]
        self.rect.y = self.y + args[1]

class ChangeLevel(Floor):
    def __init__(self, group: pygame.sprite.Group, tx: int, ty: int, type_sprite: int, width: int, height: int,
                 need_level):
        super().__init__(group, tx, ty, type_sprite, width, height)
        self.change_level = need_level

    def update(self, *args, **kwargs):
        """args из-за pygame имеют вид: (cam_pos_x, cam_pos_y, Player_pos)"""
        self.rect.x = self.x + args[0]
        self.rect.y = self.y + args[1]
        if self.tx == args[2].return_tx_and_ty()[0] and self.ty == args[2].return_tx_and_ty()[1]:
            args[3](self.change_level)
            print(22)
