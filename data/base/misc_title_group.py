import pygame
from data.base.load_image import load_image
from data.base.id_to_tile_file_name import id_to_image
import random


class Misc(pygame.sprite.Sprite):
    x: int
    y: int
    image: pygame.image
    rect: pygame.rect
    anim: list
    curr_anim: int

    def __init__(self, group: pygame.sprite.Group, tx: int, ty: int, type_sprite: int, width: int, height: int,
                 anim: list = None):
        super().__init__(group)
        self.width = width
        self.height = height
        self.tx = tx
        self.ty = ty
        self.anim = []
        if anim:
            for i in anim:
                self.anim.append(load_image(id_to_image[i], (255, 255, 255)))
                self.curr_anim = random.randint(0, len(self.anim) - 1)
            self.image = self.anim[self.curr_anim]
        else:
            self.curr_anim = -1
            self.image = load_image(id_to_image[type_sprite], (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = 2 * 16 * ty - 3 * 16 * tx + self.width - 40
        self.y = 2 * 12 * ty + 12 * tx + 18 - self.rect.height

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, *args, **kwargs):
        """args из-за pygame имеют вид: (cam_pos_x, cam_pos_y)"""
        self.rect.x = self.x + args[0]
        self.rect.y = self.y + args[1]
        if self.anim:
            if random.randint(0, 1000) == 100:
                self.curr_anim += 1
                if self.curr_anim == len(self.anim):
                    self.curr_anim = 0
                self.image = self.anim[self.curr_anim]



class Chest(Misc):

    def __init__(self, group: pygame.sprite.Group, tx: int, ty: int, type_sprite: int, width: int, height: int, player,
                 anim: list = None, inventory={}, ):
        super().__init__(group, tx, ty, type_sprite, width, height, anim)
        if inventory is None:
            inventory = {}
        self.past_left_button = False
        self.player = player
        self.inventory = False



    def update(self, *args, **kwargs):
        """args из-за pygame имеют вид: (cam_pos_x, cam_pos_y, mouse_pos, left_button)"""
        super().update(args[0], args[1])
        mouse_pos = args[-2]
        if mouse_pos:
            if self.rect.collidepoint(mouse_pos) and args[-1] and self.past_left_button != args[-1]:
                for key, item in self.player.inventory:
                    for i in range(item):
                        self.player.add_to_inventory(i)



