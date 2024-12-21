import pygame


class EntityBase:
    ref_id: int  # для обращения во время игры, у каждого объекта свой id
    base_id: int  # для создания объектов, у каждого типа объектов свой id
    # (например: лезермен имеет base_id =  10, ref_id = 1069)
    display_name: str
    current_pos_x: int
    current_pos_y: int
    tx: int
    ty: int
    x: int
    y: int
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

    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tx = 0
        self.ty = 0

    def update(self, dt):
        if (self.rect.x != 2 * 16 * self.ty - 3 * 16 * self.tx + self.width or self.rect.y != 2 * 12 * self.ty
                + 12 * self.tx):
            if self.rect.x - 2 * 16 * self.ty + 3 * 16 * self.tx - self.width > 0:
                if abs(self.rect.x - 2 * 16 * self.ty + 3 * 16 * self.tx - self.width) >= 480 * dt:
                    self.rect.x -= 480 * dt
                else:
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
            if self.rect.y - 2 * 12 * self.ty - 12 * self.tx > 0:
                if abs(self.rect.y - 2 * 12 * self.ty - 12 * self.tx) >= 240 * dt:
                    self.rect.y -= 240 * dt
                else:
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx
            if self.rect.x - 2 * 16 * self.ty + 3 * 16 * self.tx - self.width < 0:
                if abs(self.rect.x - 2 * 16 * self.ty + 3 * 16 * self.tx - self.width) >= 320 * dt:
                    self.rect.x += 320 * dt
                else:
                    self.rect.x = 2 * 16 * self.ty - 3 * 16 * self.tx + self.width
            if self.rect.y - 2 * 12 * self.ty - 12 * self.tx < 0:
                if abs(self.rect.y - 2 * 12 * self.ty - 12 * self.tx) >= 240 * dt:
                    self.rect.y += 240 * dt
                else:
                    self.rect.y = 2 * 12 * self.ty + 12 * self.tx

    def draw(self, screen: pygame.Surface, cam_pos_x: int, cam_pos_y: int):
        screen.blit(self.image, (cam_pos_x + self.rect.x - self.rect.width // 2,
                                 cam_pos_y + self.rect.y - self.rect.height))

    def move(self, move_to_tx, move_to_ty):
        self.tx = move_to_tx
        self.ty = move_to_ty

