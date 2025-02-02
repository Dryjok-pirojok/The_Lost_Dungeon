import pygame

from data.entities.enemies.entity_enemy_base import EntityEnemyBase


class Test_Npc_Enemy(EntityEnemyBase):

    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image, dead_image):
        super().__init__(width, height, tx, ty, image, dead_image)
        self.current_hp = 20
        self.angry = True


    def update(self, dt, see_player, player_pos, player):
        z = super().update(dt, see_player, player_pos, ((self.tx - player.tx) ** 2 + (self.ty - player.ty) ** 2) ** 0.5)
        return z
