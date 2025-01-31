import pygame
from data.items.item_base import ItemBase

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

    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image, left_hand=None, right_hand=None):
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



    def update(self, dt):
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
                if z <= 0.2 and (self.ty_move == ty or self.tx_move == tx):
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

                if z <= 0.2 and (self.ty_move == ty or self.tx_move == tx):
                    self.ty = int((x + 4 * y) / 128)
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.curr_pos_float_x = self.rect.x
                    self.curr_pos_float_y = self.rect.y
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx


            elif self.ty - self.ty_move > 0 and self.tx - self.tx_move < 0:
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

            elif self.ty - self.ty_move < 0 and self.tx - self.tx_move > 0:
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

    def draw(self, screen: pygame.Surface, cam_pos_x: int, cam_pos_y: int):
        screen.blit(self.image, (cam_pos_x + self.rect.x - self.rect.width // 2,
                                 cam_pos_y + self.rect.y - self.rect.height))

    def move(self, move_to_tx, move_to_ty):
        if self.tx_move == self.tx and self.ty_move == self.ty:
            self.move_is_done = True
        if self.move_is_done:
            self.tx_move = move_to_tx
            self.ty_move = move_to_ty
            self.start_pos_x = self.tx
            self.start_pos_y = self.ty
            self.move_is_done = False

    def damage(self, dmg: float):
        self.current_hp -= dmg
        if self.current_hp <= 0:
            self.death()

    def heal(self, heal: float):
        self.current_hp += heal
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def death(self):
        self.is_dead = True

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
