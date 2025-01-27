import pygame

from data.entities.enemies.entity_enemy_base import EntityEnemyBase


class Test_Npc_Enemy(EntityEnemyBase):

    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image,):
        super().__init__(width, height, tx, ty, image)
