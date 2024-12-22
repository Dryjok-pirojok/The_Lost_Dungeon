import pygame


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
    current_hp: int
    current_ap: int
    image: pygame.image
    tx_move: int
    ty_move: int
    width: int
    height: int
    start_pos_x: int
    start_pos_y: int
    def __init__(self, width: int, height: int, tx: int, ty: int, image: pygame.image):
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
        
    def update(self, dt):
        if self.tx != self.tx_move or self.ty_move != self.ty:
            if self.tx - self.tx_move < 0 and self.ty == self.ty_move:
                self.rect.x -= 3 * 16 * 10 * dt
                self.rect.y += 1 * 12 * dt * 10
                x, y = self.rect.x, self.rect.y
                x = x - self.width + 20
                z = abs((x - 4 * y / 3) / 64 - int((x - 4 * y / 3) / 64))
                print(z)
                tx = self.tx = - int((x - 4 * y / 3) / 64)
                if z <= 0.1 and self.start_pos_x != tx:
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    print(self.tx, self.ty)
                    self.start_pos_x = self.tx

            elif self.tx - self.tx_move > 0 and self.ty == self.ty_move:
                self.rect.x += 3 * 16 * 10 * dt
                self.rect.y -= 1 * 12 * dt * 10
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x - 4 * y / 3) / 64 - int((x - 4 * y / 3) / 64))
                tx = - int((x - 4 * y / 3) / 64)
                if z <= 0.1 and self.start_pos_x != tx:
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.start_pos_x = self.tx

            elif self.tx == self.tx_move and self.ty - self.ty_move < 0:
                self.rect.x += 2 * 16 * 10 * dt
                self.rect.y += 2 * 12 * 10 * dt
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
                self.rect.x -= 2 * 16 * 10 * dt
                self.rect.y -= 2 * 12 * 10 * dt
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128))
                ty = int((x + 4 * y) / 128)
                if z <= 0.1 and self.start_pos_y != ty:
                    self.ty = int((x + 4 * y) / 128)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.start_pos_y = self.ty

            elif self.ty - self.ty_move < 0 and self.tx - self.tx_move < 0:
                self.rect.x -= 1 * 16 * 10 * dt
                self.rect.y += 3 * 12 * 10 * dt
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128)) + abs((x - 4 * y / 3) / 64 -
                                                                          int((x - 4 * y / 3) / 64))
                ty = int((x + 4 * y) / 128)
                tx = - int((x - 4 * y / 3) / 64)
                if 0.05 <= z <= 0.2 and (self.ty_move == ty or self.tx_move == tx):
                    self.ty = int((x + 4 * y) / 128)
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx

            elif self.ty - self.ty_move > 0 and self.tx - self.tx_move > 0:
                self.rect.x += 1 * 16 * 10 * dt
                self.rect.y -= 3 * 12 * 10 * dt
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128)) + abs((x - 4 * y / 3) / 64 -
                                                                          int((x - 4 * y / 3) / 64))
                ty = int((x + 4 * y) / 128)
                tx = - int((x - 4 * y / 3) / 64)
                if 0.05 <= z <= 0.2 and (self.ty_move == ty or self.tx_move == tx):
                    self.ty = int((x + 4 * y) / 128)
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx

            elif self.ty - self.ty_move > 0 and self.tx - self.tx_move < 0:
                print(self.tx_move, self.ty_move)
                self.rect.x -= 5 * 16 * 10 * dt
                self.rect.y -= 1 * 12 * 10 * dt
                x, y = self.rect.x, self.rect.y
                x = x - self.width
                z = abs((x + 4 * y) / 128 - int((x + 4 * y) / 128)) + abs((x - 4 * y / 3) / 64 -
                                                                          int((x - 4 * y / 3) / 64))
                print((x + 4 * y) / 128 - int((x + 4 * y) / 128), abs((x - 4 * y / 3) / 64 -
                                                                          int((x - 4 * y / 3) / 64)))
                ty = int((x + 4 * y) / 128)
                tx = - int((x - 4 * y / 3) / 64)
                if 0.05 <= z <= 0.8 and (self.ty_move == ty or self.tx_move == tx):
                    self.ty = int((x + 4 * y) / 128)
                    self.tx = - int((x - 4 * y / 3) / 64)
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
                    self.start_pos_y = self.ty
                    self.start_pos_x = self.tx
            # x, y = self.rect.x, self.rect.y
            # x = x - self.width
            # z = abs((x - 4 * y / 3) / 64 - int((x - 4 * y / 3) / 64))
            # print(z)
            # if z <= 0.1 and not (- int((x - 4 * y / 3) / 64) == self.start_pos_x and int((x + 4 * y) / 128)
            #                      == self.start_pos_y):
            #     self.tx = - int((x - 4 * y / 3) / 64)
            #     self.ty = int((x + 4 * y) / 128)
            #     self.rect.y = 2 * 12 * self.ty + 12 * self.tx
            #     self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
            #     self.start_pos_x = self.tx
            #     self.start_pos_y = self.ty







    def draw(self, screen: pygame.Surface, cam_pos_x: int, cam_pos_y: int):
        screen.blit(self.image, (cam_pos_x + self.rect.x - self.rect.width // 2,
                                 cam_pos_y + self.rect.y - self.rect.height))

    def move(self, move_to_tx, move_to_ty):
        self.tx_move = move_to_tx
        self.ty_move = move_to_ty
        self.start_pos_x = self.tx
        self.start_pos_y = self.ty

