from data.entities.entity_base import EntityBase
import pygame

class EntityEnemyBase(EntityBase):

    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image, dead_image):
        super().__init__(width, height, tx, ty, image, dead_image)

    def find_player(self, player_pos):
        pass

