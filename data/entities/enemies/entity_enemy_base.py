from data.entities.entity_base import EntityBase
import pygame

class EntityEnemyBase(EntityBase):

    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image, ):
        super().__init__(width, height, tx, ty, image)

    def find_player(self, player_pos):
        pass

