import pygame

class ItemBase:
    weight: int
    name: int
    base_id: int
    ref_id: int
    texture_floor: pygame.image
    texture_inv: pygame.image

    def draw_floor(self, screen, position, cam_pos_x, cam_pos_y):
        screen.blit(self.texture_floor, (position[0] + cam_pos_x, position[1] + cam_pos_y))

    def draw_inv(self, screen, position):
        screen.blit(self.texture_floor, (position[0], position[1]))