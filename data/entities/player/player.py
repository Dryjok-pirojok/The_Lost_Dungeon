from data.entities.entity_base import EntityBase
from data.base.load_image import load_image


class Player(EntityBase):

    def __init__(self, width, height, start_pos_x, start_pos_y):
        super().__init__(width, height, start_pos_x, start_pos_y, load_image("textures/entities/test_npc.png"),)

    def take_control(self):
        pass

