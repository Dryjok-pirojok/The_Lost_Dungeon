from data.entities.entity_base import EntityBase
from data.base.load_image import load_image


class Player(EntityBase):

    def __init__(self, width, height, start_pos_x, start_pos_y):
        super().__init__(width, height, start_pos_x, start_pos_y, load_image("textures/entities/test_npc.png"),
                         load_image("textures/entities/test_npc_en_dead.png"))
        self.current_hp = self.max_hp
        self.current_ap = self.max_ap
        self.free_points_char = 0
        self.free_points_abil = 0
        self.curr_xp = 0
        self.need_xp = 0
        self.free_points_char = 2
        self.free_points_abil = 100


    def update(self, dt, see_player, player_pos, player):
        z = super().update(dt, False, None, 0)
        return z

    def take_control(self):
        pass

    def __str__(self):
        return "player"


