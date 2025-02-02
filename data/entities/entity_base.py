import random

import pygame
from data.items.item_base import ItemBase
from data.izometry_eng.A_star import a_star

global a12
global delta

class EntityBase:
    ref_id: int  # для обращения во время игры, у каждого объекта свой id
    base_id: int  # для создания объектов, у каждого типа объектов свой id
    # (например: лезермен имеет base_id =  10, ref_id = 1069)
    display_name: str
    tx: int
    ty: int
    rect: pygame.rect
    # characteristics
    strength: int
    luck: int
    agility: int
    voice: int
    endurance: int
    # charact. end
    inventory: dict
    current_hp: float
    current_ap: int
    image: pygame.image
    tx_move: int
    ty_move: int
    width: int
    height: int
    start_pos_x: int
    start_pos_y: int
    curr_pos_float_x: float
    curr_pos_float_y: float
    move_is_done: bool
    max_hp: int
    is_dead: bool
    max_ap: int
    # abilities start
    melee: int
    crushing: int
    fists: int
    lash: int
    firearms: int
    one_handed: int
    two_handed: int
    heavy_gun: int
    grenades: int
    speech: int
    steal: int
    repair: int
    science: int
    # abilities end
    add_to_melee: int
    add_to_crushing: int
    add_to_fists: int
    add_to_lash: int
    add_to_firearms: int
    add_to_one_handed: int
    add_to_two_handed: int
    add_to_heavy_gun: int
    add_to_grenades: int
    add_to_speech: int
    add_to_steal: int
    add_to_repair: int
    add_to_science: int
    angry: bool
    level: int

    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image, dead_image,
                 left_hand=None, right_hand=None, characteristics=(5, 5, 5, 5, 5), level=1,):
        self.width = width
        self.height = height
        self.tx = tx
        self.ty = ty
        self.tx_move = tx
        self.ty_move = ty
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
        self.rect.y = 2 * 12 * self.ty + 12 * self.tx
        self.curr_pos_float_x = float(self.rect.x)
        self.curr_pos_float_y = float(self.rect.y)
        self.x = 0
        self.y = 0
        self.move_is_done = True
        self.inventory = {}
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.selected_hand = self.right_hand
        self.strength = characteristics[0]
        self.luck = characteristics[1]
        self.agility = characteristics[2]
        self.voice = characteristics[3]
        self.endurance = characteristics[4]
        self.add_to_melee = 0
        self.add_to_crushing = 0
        self.add_to_fists = 0
        self.add_to_lash = 0
        self.add_to_firearms = 0
        self.add_to_one_handed = 0
        self.add_to_two_handed = 0
        self.add_to_heavy_gun = 0
        self.add_to_grenades = 0
        self.add_to_speech = 0
        self.add_to_steal = 0
        self.add_to_repair = 0
        self.add_to_science = 0
        self.level = 1
        self.calculate_abilities()
        self.angry = False
        self.dead_image = dead_image
        self.is_dead = False
        self.current_hp = self.max_hp
        self.current_ap = self.max_ap
        self.move_list = []


    def update(self, dt, see_player, player_pos, distance):
        if self.move_is_done and self.move_list:
            self.move(self.move_list[0][0], self.move_list[0][1])
            self.move_list.pop(0)
        if self.tx != self.tx_move or self.ty_move != self.ty:
            if self.tx - self.tx_move < 0 and self.ty == self.ty_move:
                self.curr_pos_float_x -= 3 * 16 * dt * 10
                self.curr_pos_float_y += 1 * 12 * dt * 10
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x - 4 * y / 3) / 64 - int((x - 4 * y / 3) / 64))
                tx = self.tx = - int((x - 4 * y / 3) / 64)
                if z <= 0.1 and self.start_pos_x != tx:
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_x = self.tx



            elif self.tx - self.tx_move > 0 and self.ty == self.ty_move:
                self.curr_pos_float_x += 3 * 16 * 10 * dt
                self.curr_pos_float_y -= 1 * 12 * dt * 10
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x - 4 * y / 3) / 64 - int((x - 4 * y / 3) / 64))
                tx = - int((x - 4 * y / 3) / 64)
                if z <= 0.1 and self.start_pos_x != tx:
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_x = self.tx


            elif self.tx == self.tx_move and self.ty - self.ty_move < 0:
                self.curr_pos_float_x += 2 * 16 * 10 * dt
                self.curr_pos_float_y += 2 * 12 * 10 * dt
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128))
                ty = int((x + 4 * y) / 128)
                if z <= 0.1 and self.start_pos_y != ty:
                    self.ty = int((x + 4 * y) / 128)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.start_pos_y = self.ty


            elif self.tx == self.tx_move and self.ty - self.ty_move > 0:
                self.curr_pos_float_x -= 2 * 16 * 10 * dt
                self.curr_pos_float_y -= 2 * 12 * 10 * dt
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128))
                ty = int((x + 4 * y) / 128)
                if z <= 0.1 and self.start_pos_y != ty:
                    self.ty = int((x + 4 * y) / 128)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_y = self.ty


            elif self.ty - self.ty_move < 0 and self.tx - self.tx_move < 0:
                self.curr_pos_float_x -= 1 * 16 * 10 * dt
                self.curr_pos_float_y += 3 * 12 * 10 * dt
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128)) + abs((x - 4 * y / 3) / 64 -
                                                                          int((x - 4 * y / 3) / 64))
                ty = int((x + 4 * y) / 128)
                tx = - int((x - 4 * y / 3) / 64)
                if z <= 0.2 and (self.start_pos_y != ty and self.start_pos_x != tx):
                    self.ty = int((x + 4 * y) / 128)
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx


            elif self.ty - self.ty_move > 0 and self.tx - self.tx_move > 0:
                self.curr_pos_float_x += 1 * 16 * 10 * dt
                self.curr_pos_float_y -= 3 * 12 * 10 * dt
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128)) + abs((x - 4 * y / 3) / 64 -
                                                                          int((x - 4 * y / 3) / 64))
                ty = int((x + 4 * y) / 128)
                tx = - int((x - 4 * y / 3) / 64)

                if z <= 0.2 and (self.start_pos_y != ty or self.start_pos_x != tx):
                    self.ty = int((x + 4 * y) / 128)
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx


            elif self.ty - self.ty_move > 0 > self.tx - self.tx_move:
                self.curr_pos_float_x -= 5 * 16 * 10 * dt
                self.curr_pos_float_y -= 1 * 12 * 10 * dt
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y

                x, y = self.curr_pos_float_x, self.curr_pos_float_y
                x = x - self.width
                x -= 8
                y += 20
                ty = int((x + 4 * y) / 128)
                tx = -int((x - 4 * y / 3) / 64)
                x += 8
                y -= 20
                z = abs(2 * 16 * ty - 3 * 16 * tx - x) + abs(2 * 12 * ty + 12 * tx - y)
                if z <= 5 and (self.start_pos_y != ty and self.start_pos_x != tx):
                    self.ty = ty
                    self.tx = tx
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx

            elif self.ty - self.ty_move < 0 < self.tx - self.tx_move:
                self.curr_pos_float_x += 5 * 16 * 10 * dt
                self.curr_pos_float_y += 1 * 12 * 10 * dt
                self.rect.x = self.curr_pos_float_x
                self.rect.y = self.curr_pos_float_y
                x, y = self.curr_pos_float_x, self.curr_pos_float_y
                x = x - self.width
                x -= 8
                y += 20
                ty = int((x + 4 * y) / 128)
                tx = -int((x - 4 * y / 3) / 64)
                x += 8
                y -= 20
                z = abs(2 * 16 * ty - 3 * 16 * tx - x) + abs(2 * 12 * ty + 12 * tx - y)
                if z <= 5 and (self.start_pos_y != ty and self.start_pos_x != tx):
                    self.ty = ty
                    self.tx = tx
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx


        if self.tx_move == self.tx and self.ty_move == self.ty:
            self.move_is_done = True

        self.see_player = see_player
        self.pl_pos = player_pos
        if self.see_player and self.angry and distance <= 5 + self.agility and not self.is_dead:
            return "start", self

    def draw(self, screen: pygame.Surface, cam_pos_x: int, cam_pos_y: int):
        screen.blit(self.image, (cam_pos_x + self.rect.x - self.rect.width // 2,
                                 cam_pos_y + self.rect.y - self.rect.height))

    def move(self, move_to_tx, move_to_ty):
        if self.move_is_done:
            self.tx_move = move_to_tx
            self.ty_move = move_to_ty
            self.start_pos_x = self.tx
            self.start_pos_y = self.ty
            self.move_is_done = False


    def damage(self, dmg: float):
        self.current_hp -= dmg
        z = [False, None]
        if self.current_hp <= 0:
            z[0] = True
            z[1] = self.death()
        return z

    def heal(self, heal: float):
        self.current_hp += heal
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def death(self):
        self.is_dead = True
        self.image = self.dead_image
        return (self.tx, self.ty, self.inventory)

    def add_to_inventory(self, item: ItemBase, count=1):
        try:
            self.inventory[item] = count + self.inventory[item]

        except KeyError:
            self.inventory[item] = 1

    def remove_from_inventory(self, item: ItemBase, count=1):
        try:
            self.inventory[item] = self.inventory[item] - count
            if self.inventory[item] == 0:
                self.inventory.pop(item)
        except Exception as err:
            pass

    def return_tx_and_ty(self):
        return self.tx, self.ty

    def __str__(self):
        return "NPC"

    def return_inv(self):
        return self.inventory

    def tp_to(self, tx, ty):
        self.tx = tx
        self.ty = ty
        self.start_pos_x = tx
        self.start_pos_y = ty
        self.tx_move = tx
        self.ty_move = ty
        self.move_is_done = True
        self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
        self.rect.y = 2 * 12 * self.ty + 12 * self.tx
        self.curr_pos_float_x = float(self.rect.x)
        self.curr_pos_float_y = float(self.rect.y)


    def calculate_abilities(self):
        self.melee = int(self.strength * 2.5 + self.add_to_melee + self.luck)
        self.crushing = int(self.strength * 3 + self.agility + self.endurance + self.add_to_crushing
                            + self.luck)
        self.fists = int(self.strength * 2 + self.agility * 1.5 + self.endurance * 1.0 + self.add_to_fists
                         + self.luck)
        self.lash = int(self.strength * 1.5 + self.agility * 2.5 + self.endurance * 1.5 + self.add_to_lash
                        + self.luck)
        self.firearms = int(self.agility * 2.5 + self.add_to_firearms + self.luck)
        self.one_handed = int(self.strength + self.agility * 3.5 + self.add_to_one_handed + self.luck)
        self.two_handed = int(self.strength * 1.5 + self.agility * 2 + self.endurance * 0.5 + self.add_to_two_handed +
                              self.luck)
        self.heavy_gun = int(self.strength + self.agility * 1.5 + self.endurance * 0.5 + self.add_to_heavy_gun +
                             self.luck)
        self.grenades = int(self.strength + self.agility * 3 + self.endurance + self.add_to_grenades + self.luck)
        self.speech = int(self.voice * 4 + self.luck + self.add_to_speech)
        self.steal = int(self.agility * 3 + self.endurance + self.add_to_steal + self.luck)
        self.repair = int(self.strength * 2 + self.agility * 2 + self.luck * 1.5 + self.add_to_repair)
        self.science = int(self.voice * 3 + self.luck + self.endurance + self.add_to_science)

        self.max_ap = int(5 + self.agility * 0.5)
        self.max_hp = int(20 + self.endurance * 2 + self.level * 5 * int(self.endurance * 0.5))

    def start_fight(self):
        return self

    def fight(self, grid, player, level_grid):
        arg = []
        if self.selected_hand:
            if self.selected_hand.type == "attackable":
                dis = player.selected_hand.range

            else:
                dis = 1
        else:
            dis = 1
        test_attack = grid.test_can_attack(player.return_tx_and_ty(), self.return_tx_and_ty(), dis)
        if test_attack:
            arg = self.attack(player)
            if arg:
                if not arg[-1]:
                    self.current_ap = 0

        else:
            if not self.move_list:
                z = a_star(level_grid, self.return_tx_and_ty(), (player.return_tx_and_ty()[0],
                                                                 player.return_tx_and_ty()[1] + 1))
                print(z)
                if z:
                    self.current_ap -= dis
                    self.go_to(z[1:])
                else:
                    self.current_ap = 0


        if arg:
            return arg[0]

    def attack(self, other, chance=50):
        global a12
        global delta
        if self != other:
            new_text = ""
            is_dead = False
            arg = None
            attacked = False
            if str(other) == "NPC" or str(other) == "player":
                if self.selected_hand:
                    if self.selected_hand.type == "attackable":
                        if self.current_ap - self.selected_hand.use_ap >= 0:
                            class_1, class_2 = self.selected_hand.class_firearm
                            delta = self
                            a12 = 0
                            exec(f"a12 = a12 + delta.{class_1} // 2", globals())
                            exec(f"a12 = a12 + delta.{class_2} ", globals())
                            chance = a12 + self.luck
                            dmg = random.randint(self.selected_hand.min_damage, self.selected_hand.max_damage)
                            new_text = f"{str(self)} нанесли {dmg} единиц урона"
                            if random.randint(0, 100) <= self.luck + self.selected_hand.crit_chance:
                                dmg = int(dmg * random.uniform(1 + (self.luck / 10), 5 + 2 * (self.luck / 10)))
                                new_text = f"Крит. {str(self)} нанесли {dmg} единиц урона"

                            if random.randint(0, 100) <= chance:
                                is_dead, arg = other.damage(dmg)
                            else:
                                new_text = "промах"
                            self.current_ap -= self.selected_hand.use_ap
                            attacked = True
                        else:
                            new_text = f"{str(self)} Недостаточно очков действия"
                            attacked = False

                else:
                    if self.current_ap - 2 >= 0:
                        chance = self.melee // 2 + self.fists + self.luck
                        dmg = random.randint(4, 10)
                        new_text = f"{str(self)} нанесли {dmg} единиц урона"
                        if random.randint(0, 100) <= self.luck + 10:
                            dmg = int(dmg * random.uniform(1 + (self.luck / 10), 5 + 2 * (self.luck / 10)))
                            new_text = f"Крит. {str(self)} нанесли {dmg} единиц урона"
                        if random.randint(0, 100) <= chance:
                            is_dead, arg = other.damage(dmg)
                        else:
                            new_text = "промах"
                        self.current_ap -= 2
                        attacked = True
                    else:
                        new_text = f"{str(self)} очков действия"
                        attacked = False

            return new_text, is_dead, arg, attacked

    def stop_moving(self):
        self.start_pos_x = self.tx
        self.start_pos_y = self.ty
        self.tx_move = self.tx
        self.ty_move = self.ty
        self.move_is_done = True
        self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
        self.rect.y = 2 * 12 * self.ty + 12 * self.tx
        self.curr_pos_float_x = float(self.rect.x)
        self.curr_pos_float_y = float(self.rect.y)

    def go_to(self, data: list):
        self.move_list = data


