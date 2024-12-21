from data.entities.entity_base import EntityBase
from data.base.load_image import load_image


class Player(EntityBase):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.image = load_image("textures/entities/test_npc.png")
        self.rect = self.image.get_rect()
        self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width

        self.rect.y = 2 * 12 * self.ty + 12 * self.tx
    def Take_control(self):
        pass

