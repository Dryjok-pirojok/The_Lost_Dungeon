from data.entities.entity_base import EntityBase
from data.base.load_image import load_image


class Player(EntityBase):

    def __init__(self, width, height):
        super().__init__(width, height, 0, 0, load_image("textures/entities/test_npc.png"))

    def take_control(self):
        pass

